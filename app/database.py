import sqlite3

def get_db():
    db = sqlite3.connect("smartlead.db")
    db.row_factory = sqlite3.Row
    return db 

def init_db(app):
    db = get_db()

    db.execute("""
            CREATE TABLE IF NOT EXISTS leads(
            id integer PRIMARY KEY AUTOINCREMENT,
            isim text NOT NULL,
            telefon text NOT NULL,
            mesaj text,
            tarih TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
    """)

    db.commit()
    db.close()

def lead_ekle(isim, telefon, mesaj):
    db = get_db()

    db.execute("""
        INSERT INTO leads(isim, telefon, mesaj) values (?, ?, ?)
    """, (isim, telefon, mesaj))

    db.commit()
    db.close()

def tum_leadler():
    db = get_db()

    sonuc = db.execute("""
    SELECT * 
    FROM leads 
    ORDER BY tarih DESC
    """)

    leadler = sonuc.fetchall()

    db.close()

    return leadler
