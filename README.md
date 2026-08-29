# SmartLead AI

## Proje Hakkında

SmartLead AI, Loshito platformu için geliştirilen Flask tabanlı bir backend uygulamasıdır.
Uygulama, kullanıcıların yapay zekâ destekli sohbet sistemi üzerinden Loshito hakkında bilgi almasını ve iletişim formu üzerinden lead bilgilerinin kaydedilmesini sağlar.
Kaydedilen lead bilgileri Wix üzerinde oluşturulan yönetim panelinden görüntülenebilir.

## Özellikler

- Yapay zekâ destekli sohbet sistemi
- Loshito hakkında kullanıcı sorularına AI ile yanıt verme
- Kullanıcı iletişim bilgilerinin ve mesajlarının kaydedilmesi
- Lead verilerinin SQLite veritabanında saklanması
- Yönetim paneli üzerinden kayıtlı leadlerin görüntülenmesi
- Wix ve Flask backend arasında API iletişimi
- API ve hassas bilgilerin ortam değişkenleri ile yönetilmesi
- Hata kontrolü ve API yanıt doğrulaması

## Kullanılan Teknolojiler

- Python
- Flask
- SQLite
- Groq API
- Wix Velo
- JavaScript
- Render
- Git & GitHub

## Kurulum ve Çalıştırma

1. Projeyi bilgisayarınıza klonlayın:
2. 
   ```bash
  git clone <repository-url>
  cd smartlead-ai

2.Sanal ortam oluşturun:

  python -m venv venv

3.Sanal ortamı etkinleştirin:

  Windows:
    venv\Scripts\activate

4.Gerekli kütüphaneleri yükleyin:

  pip install -r requirements.txt

5.Proje ana dizininde .env dosyası oluşturun ve gerekli ortam değişkenlerini ekleyin:

  GROQ_API_KEY=your_api_key
  BUSINESS_CONTEXT=your_business_context

6.Uygulamayı çalıştırın:
  
  python run.py

7. Sunucunun çalıştığını kontrol etmek için tarayıcıdan aşağıdaki adresi açın:

   http://127.0.0.1:5000/health

   Aşağıdaki gibi bir yanıt alıyorsanız backend başarıyla çalışıyor demektir:

   ```json
  {
    "status": "ok"
  }

## Canlı Bağlantılar

- **Loshito Wix Sitesi:** https://hamizogluseymen.wixsite.com/loshito
- **Yönetim Paneli:** https://hamizogluseymen.wixsite.com/loshito/y%C3%B6netim-paneli
- **Render Backend:** https://smartlead-ai-12ap.onrender.com
- **Backend Sağlık Kontrolü:** https://smartlead-ai-12ap.onrender.com/health
