from flask import Blueprint, render_template, request, jsonify
from app.services.ai_service import ai_service, AIServiceError
from app.database import lead_ekle, tum_leadler

web_bp = Blueprint("web", __name__)

api_bp = Blueprint("api",__name__, url_prefix="/api")

@web_bp.route("/")
def index():
    return render_template("index.html")

@web_bp.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@api_bp.route("/sohbet", methods=["POST"])
def sohbet():
    veri = request.get_json() or {}
    mesaj = veri.get("mesaj")
    gecmis = veri.get("gecmis", [])

    if not mesaj:
        return jsonify({"basari":False, "hata":"Mesaj boş olamaz"}), 400

    try:
        cevap = ai_service.yanit_uret(mesaj,gecmis)
        return jsonify({"basari":True, "cevap": cevap}) 

    except AIServiceError as e:
        return jsonify({"basari": False, "hata":(str(e))}), 503

@api_bp.route("/leads",methods=["POST"])
def yeni_lead():
    veri = request.get_json() or {}
    isim = veri.get("isim")
    telefon = veri.get("telefon")
    mesaj = veri.get("mesaj")

    if not isim:
        return jsonify({"basari":False, "hata":"İsim boş olamaz"}), 400
    elif not telefon:
        return jsonify({"basari":False, "hata":"Telefon boş olamaz"}), 400

    lead_ekle(isim,telefon,mesaj)
    return jsonify({"basari": True}), 201

@api_bp.route("/leads",methods=["GET"])
def lead_cekme():
    leadler = tum_leadler()

    lead_list = [dict(lead) for lead in leadler]

    return jsonify({"basari":True,"leadler":lead_list})