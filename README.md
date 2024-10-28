# Hava Durumu Uygulaması

Bu uygulama, OpenWeatherMap API’sini kullanarak bir şehrin güncel hava durumu bilgisini tkinter arayüzünde görüntüler. Kullanıcı, şehir adını girerek sıcaklık, nem ve hava durumu açıklamasını görüntüleyebilir.

## Özellikler

- Basit bir arayüz
- Şehir adına göre güncel hava durumu bilgisi (sıcaklık, nem, açıklama)


## Gereksinimler

Bu uygulamanın çalışabilmesi için aşağıdaki gereksinimler karşılanmalıdır:

- **Python 3.x** sürümü
- **tkinter**: Genellikle Python ile birlikte gelir.
- **requests** modülü: Bu modülü kurmak için aşağıdaki komutu çalıştırın:

  ```bash
  pip install requests
  ```

## Kurulum

1. **OpenWeatherMap API Key alın**: [OpenWeatherMap](https://home.openweathermap.org/users/sign_up) sitesine üye olup ücretsiz bir API anahtarı alabilirsiniz.

2. **API anahtarınızı ekleyin**: `main.py` dosyasında, `API_KEY` değişkenine kendi API anahtarınızı ekleyin:

   ```python
   API_KEY = "Sizin_API_Anahtarınız"
   ```

3. **Dosyaları İndirin veya Kopyalayın**: `main.py` ve `ui.py` dosyalarını aynı dizinde bulundurduğunuzdan emin olun.

## Kullanım

### 1. `ui.py` Dosyasını Çalıştırın

Uygulamayı başlatmak için terminalde aşağıdaki komutu çalıştırın:

```bash
python ui.py
```

### 2. Arayüzde Şehir Adını Girin

Açılan arayüzde bir şehir adı girin (ingilizce olmalı.) ve "Göster" butonuna tıklayın. Hava durumu bilgileri, kısa süre içinde ekranda görüntülenecektir.

## Proje Yapısı

- **main.py**: Hava durumu verilerini almak için OpenWeatherMap API’yi kullanan modül. Şehir adını kullanarak hava durumu verilerini döndürür.
- **ui.py**: Tkinter arayüzü ile kullanıcı etkileşimini ve görsel bilgiyi sağlar. Bu dosya, API'den veri çekme işlemini iş parçacıkları ile yaparak arayüzün donmasını engeller.

## Örnek Çıktı

Girilen şehir adına göre, hava durumu şu formatta gösterilir:

```
Istanbul
Sıcaklık: 24°C
Nem: 60%
Durum: few clouds
```

## Sorun Giderme

- **"Hava durumu bulunamadı veya şehir geçersiz."**: Şehir adı yanlış girilmiş olabilir veya API yanıt vermiyor olabilir. Doğru şehir adıyla tekrar deneyin ve API anahtarının geçerli olduğundan emin olun.

---
