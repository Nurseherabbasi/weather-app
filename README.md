# Hava Durumu Uygulaması

## Proje Açıklaması

Bu proje, Flask kullanarak bir hava durumu uygulaması oluşturur. Kullanıcılar şehir ve ülke kodunu girerek hava durumu bilgilerini alabilirler. Uygulama, OpenWeatherMap API'sini kullanarak hava durumu verilerini getirir ve kullanıcıya gösterir.

## Proje Bağımlılıkları

Bu proje aşağıdaki Python paketlerine ihtiyaç duyar:

- Flask==2.2.2
- requests==2.28.2
- werkzeug==2.2.2

## Kurulum ve Kullanım

### Manuel Kurulum

1. Proje dosyalarını bilgisayarınıza indirin veya klonlayın:

    git clone https://github.com/kullaniciadi/proje-adi.git

2. Proje dizinine gidin:

    cd proje-adi

3. Python sanal ortamı oluşturun ve etkinleştirin:

    python -m venv venv
    source venv/bin/activate  # Linux,Mac için
    venv\Scripts\activate     # Windows için

4. Gereken bağımlılıkları yükleyin:

    pip install -r requirements.txt

5. Uygulamayı başlatın:

    python weather.py

6. Tarayıcınızı açın ve `http://127.0.0.1:5000` adresine gidin.

### API Anahtarları

OpenWeatherMap API anahtarınızı `weather.py` dosyasında `API_KEY` değişkenine girmeniz gerekmektedir.


### Docker Kullanarak Kurulum

1. Docker imajını oluşturun:

    docker build -t flask .

2. Docker konteynerini başlatın:

    docker run -p 5000:5000 flask

3. Tarayıcınızı açın ve `http://localhost:5000` adresine gidin.

### Docker Compose Kullanarak Kurulum

1. Docker compos imajını oluşturun ve başlatın:
   
    docker compose up --build

## Proje Yapısı

- `weather.py`: Flask uygulaması ve hava durumu API entegrasyonu
- `weather.html`: Uygulamanın ön yüzü için HTML dosyası
- `requirements.txt`: Python bağımlılıkları
- `Dockerfile`: Docker imajını oluşturmak için kullanılan dosya
- `docker-compose.yml`: Docker Compose yapılandırma dosyası

## Lisans

Bu proje MIT Lisansı ile lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasına bakın.
