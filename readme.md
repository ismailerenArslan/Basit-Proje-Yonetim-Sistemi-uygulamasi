#  Basit Proje Yönetim Sistemi

## 📋 İçindekiler
- [Proje Hakkında](#-proje-hakkında)
- [Özellikler](#-özellikler)
- [Kurulum](#-kurulum)
- [Kullanım](#-kullanım)
- [Veri Yapıları](#-veri-yapıları)
- [Fonksiyon Referansı](#-fonksiyon-referansı)
- [Örnekler](#-örnekler)
- [Hata Çözümleri](#-hata-çözümleri)
- [Geliştirme Notları](#-geliştirme-notları)

---

## 📖 Proje Hakkında

Bu proje, **Basit Bir Proje Yönetim Sistemi** uygulamasıdır. Kullanıcıların projelerini, takım üyelerini ve görevleri etkili bir şekilde yönetmesine olanak tanır.

### 🎯 Amaç
Kullanıcının takım üyelerini, projeleri, görevleri ve zamanlamayı yönetmesine olanak tanıyan bir program oluşturmak.

### 👨‍💻 Geliştirici Bilgileri
- **Proje Adı:** Basit Proje Yönetim Sistemi
- **Programlama Dili:** Python 3.x
- **Geliştirme Tarihi:** 2025
- **Öğrenci:** İsmail Eren Arslan


---

## ✨ Özellikler

### 1️⃣ Proje Yönetimi
- ✅ Yeni proje oluşturma
- ✅ Genel zaman planlaması (başlangıç ve bitiş tarihi) tanımlama
- ✅ Projeleri listeleme ve görüntüleme
- ✅ Otomatik proje ID oluşturma (PRJ001, PRJ002, ...)

### 2️⃣ Takım Üyeleri Yönetimi
- ✅ Takım üyesi ekleme (ad, soyad, pozisyon)
- ✅ Takım üyesi silme
- ✅ Takım üyelerini görüntüleme
- ✅ Otomatik üye ID oluşturma (UYE001, UYE002, ...)
- ✅ Üye silindiğinde atanmış görevlerin otomatik kontrolü

### 3️⃣ Görev Yönetimi
- ✅ Yeni görev tanımlama
- ✅ Her görev için son teslim tarihi (deadline) belirleme
- ✅ Görevi bir takım üyesine atama
- ✅ Görev durumu belirleme (Bekliyor, Yapılıyor, Tamamlandı)
- ✅ Otomatik görev ID oluşturma (TSK001, TSK002, ...)
- ✅ Görev durumunu güncelleme

### 4️⃣ Raporlama
- ✅ Bir projedeki tüm görevleri görüntüleme
- ✅ Her üyeye atanan görevleri görüntüleme
- ✅ Gecikmiş görevleri kontrol etme (durum ve son teslim tarihi karşılaştırması)
- ✅ Gecikme süresini gün olarak hesaplama

---

## 💾 Kurulum

### Gereksinimler
- Python 3.6 veya üzeri
- Standart Python kütüphaneleri (ek kurulum gerekmez)

### Kurulum Adımları

1. **Dosyayı İndirin**
   ```bash
   # Projeyi bilgisayarınıza indirin
   ```

2. **Python Kurulumunu Kontrol Edin**
   ```bash
   python --version
   # veya
   python3 --version
   ```

3. **Programı Çalıştırın**
   ```bash
   python proje_yonetim_sistemi.py
   # veya
   python3 proje_yonetim_sistemi.py
   ```

---

## 🎮 Kullanım

### Ana Menü

Program başlatıldığında aşağıdaki ana menü ile karşılaşırsınız:

```
 PROJE YÖNETİM SİSTEMİ
============================================================
1. Proje Yönetimi
2. Takım Üyeleri Yönetimi
3. Görev Yönetimi
4. Raporlama
0. Çıkış
============================================================
```

### 1. Proje Yönetimi

#### Yeni Proje Oluşturma
```
Proje Adı: Web Sitesi Geliştirme
Başlangıç Tarihi (GG/AA/YYYY): 01/01/2025
Bitiş Tarihi (GG/AA/YYYY): 30/06/2025
```

**Çıktı:**
```
 Proje başarıyla oluşturuldu!
Proje ID: PRJ001
Proje Adı: Web Sitesi Geliştirme
Başlangıç: 01/01/2025, Bitiş: 30/06/2025
```

#### Projeleri Listeleme
Tüm projeleri detaylı bilgileriyle birlikte görüntüler:
- Proje ID
- Proje Adı
- Başlangıç ve Bitiş Tarihleri
- Görev Sayısı

### 2. Takım Üyeleri Yönetimi

#### Takım Üyesi Ekleme
```
Ad: Ahmet
Soyad: Yılmaz
Pozisyon: Frontend Developer
```

**Çıktı:**
```
 Takım üyesi başarıyla eklendi!
Üye ID: UYE001
Ad Soyad: Ahmet Yılmaz
Pozisyon: Frontend Developer
```

#### Takım Üyesi Silme
```
Silinecek Üye ID: UYE001
```

**Uyarı:** Eğer üyeye atanmış görevler varsa, uyarı verilir ve görev atamaları kaldırılır.

#### Takım Üyelerini Görüntüleme
Tüm takım üyelerini listeler:
- Üye ID
- Ad Soyad
- Pozisyon
- Atanan Görev Sayısı

### 3. Görev Yönetimi

#### Yeni Görev Tanımlama
```
Proje ID: PRJ001
Görev Adı: Ana Sayfa Tasarımı
Son Teslim Tarihi (GG/AA/YYYY): 15/02/2025
Şimdi bir üyeye atamak ister misiniz? (E/H): E
Atanacak Üye ID: UYE001
```

**Çıktı:**
```
 Görev başarıyla oluşturuldu!
Görev ID: TSK001
Görev Adı: Ana Sayfa Tasarımı
Son Teslim: 15/02/2025
Atanan Kişi: Ahmet Yılmaz
```

#### Görevi Üyeye Atama
Daha önce atanmamış veya farklı bir üyeye atanmış görevi yeni bir üyeye atayabilirsiniz.

```
Görev ID: TSK001
Atanacak Üye ID: UYE002
```

#### Görev Durumunu Güncelleme
```
Görev ID: TSK001
Durum Seçenekleri: Bekliyor, Yapılıyor, Tamamlandı
Yeni Durum: Yapılıyor
```

**Çıktı:**
```
 Görev durumu güncellendi!
Görev: Ana Sayfa Tasarımı
Bekliyor → Yapılıyor
```

### 4. Raporlama

#### Projedeki Görevleri Görüntüleme
```
Proje ID: PRJ001
```

Belirtilen projedeki tüm görevleri detaylı olarak listeler:
- Görev ID
- Görev Adı
- Son Teslim Tarihi
- Durum
- Atanan Kişi

#### Üyeye Atanan Görevleri Görüntüleme
```
Üye ID: UYE001
```

Belirtilen üyeye atanan tüm görevleri listeler:
- Görev ID
- Görev Adı
- Proje Adı
- Son Teslim Tarihi
- Durum

#### Gecikmiş Görevleri Kontrol Etme
Otomatik olarak bugünün tarihini alır ve şu görevleri listeler:
- Durumu "Tamamlandı" olmayan
- Son teslim tarihi geçmiş
- Kaç gün geciktiğini gösteren

**Çıktı Örneği:**
```
 GECİKMİŞ GÖREVLER
============================================================
Toplam 2 gecikmiş görev bulundu:

Görev ID: TSK001
Görev Adı: Ana Sayfa Tasarımı
Proje: Web Sitesi Geliştirme
Son Teslim: 15/01/2025
Durum: Yapılıyor
Gecikme: 14 gün
Atanan: Ahmet Yılmaz
```

---

## 🗂️ Veri Yapıları

Program, Python'un **Dictionary** ve **List** veri yapılarını kullanır.

### Projeler Dictionary
```python
self.projeler = {
    'PRJ001': {
        'id': 'PRJ001',
        'ad': 'Web Sitesi Geliştirme',
        'baslangic_tarihi': '01/01/2025',
        'bitis_tarihi': '30/06/2025',
        'gorevler': ['TSK001', 'TSK002']  # Bu projeye ait görev ID'leri (list)
    }
}
```

### Takım Üyeleri Dictionary
```python
self.takim_uyeleri = {
    'UYE001': {
        'id': 'UYE001',
        'ad': 'Ahmet',
        'soyad': 'Yılmaz',
        'pozisyon': 'Frontend Developer',
        'gorevler': ['TSK001', 'TSK003']  # Bu üyeye atanan görev ID'leri (list)
    }
}
```

### Görevler Dictionary
```python
self.gorevler = {
    'TSK001': {
        'id': 'TSK001',
        'proje_id': 'PRJ001',
        'ad': 'Ana Sayfa Tasarımı',
        'son_teslim_tarihi': '15/02/2025',
        'atanan_uye': 'UYE001',
        'durum': 'Yapılıyor'  # Bekliyor / Yapılıyor / Tamamlandı
    }
}
```

---

## 📚 Fonksiyon Referansı

### ProjeYonetimSistemi Sınıfı

#### Proje Yönetimi Fonksiyonları

```python
yeni_proje_olustur(proje_adi, baslangic_tarihi, bitis_tarihi)
```
- **Parametreler:**
  - `proje_adi` (str): Proje adı
  - `baslangic_tarihi` (str): GG/AA/YYYY formatında
  - `bitis_tarihi` (str): GG/AA/YYYY formatında
- **Döndürür:** Proje ID veya None (hata durumunda)
- **Örnek:** `sistem.yeni_proje_olustur("Web Projesi", "01/01/2025", "30/06/2025")`

```python
projeleri_listele()
```
- Tüm projeleri konsola yazdırır
- **Döndürür:** None

#### Takım Üyeleri Yönetimi Fonksiyonları

```python
takim_uyesi_ekle(ad, soyad, pozisyon)
```
- **Parametreler:**
  - `ad` (str): Üye adı
  - `soyad` (str): Üye soyadı
  - `pozisyon` (str): Pozisyon/Görev
- **Döndürür:** Üye ID
- **Örnek:** `sistem.takim_uyesi_ekle("Ahmet", "Yılmaz", "Developer")`

```python
takim_uyesi_sil(uye_id)
```
- **Parametreler:**
  - `uye_id` (str): Silinecek üye ID'si
- **Döndürür:** True/False
- **Not:** Üyeye atanmış görevler varsa, atamalar kaldırılır

```python
takim_uyelerini_goruntule()
```
- Tüm takım üyelerini konsola yazdırır

#### Görev Yönetimi Fonksiyonları

```python
yeni_gorev_tanimla(proje_id, gorev_adi, son_teslim_tarihi, atanan_uye_id=None)
```
- **Parametreler:**
  - `proje_id` (str): Projenin ID'si
  - `gorev_adi` (str): Görev adı
  - `son_teslim_tarihi` (str): GG/AA/YYYY formatında
  - `atanan_uye_id` (str, opsiyonel): Atanacak üye ID'si
- **Döndürür:** Görev ID veya None
- **Örnek:** `sistem.yeni_gorev_tanimla("PRJ001", "Tasarım", "15/02/2025", "UYE001")`

```python
gorevi_ata(gorev_id, uye_id)
```
- **Parametreler:**
  - `gorev_id` (str): Görev ID'si
  - `uye_id` (str): Üye ID'si
- **Döndürür:** True/False

```python
gorev_durumu_guncelle(gorev_id, yeni_durum)
```
- **Parametreler:**
  - `gorev_id` (str): Görev ID'si
  - `yeni_durum` (str): "Bekliyor", "Yapılıyor" veya "Tamamlandı"
- **Döndürür:** True/False

#### Raporlama Fonksiyonları

```python
projedeki_gorevleri_goruntule(proje_id)
```
- **Parametreler:**
  - `proje_id` (str): Proje ID'si
- Projedeki tüm görevleri detaylı olarak yazdırır

```python
uyeye_atanan_gorevleri_goruntule(uye_id)
```
- **Parametreler:**
  - `uye_id` (str): Üye ID'si
- Üyeye atanan tüm görevleri detaylı olarak yazdırır

```python
gecikmis_gorevleri_kontrol_et()
```
- Gecikmiş görevleri otomatik olarak bulur ve listeler
- Gecikme süresini gün olarak hesaplar

---

## 💡 Örnekler

### Örnek Kullanım Senaryosu

```python
# Sistem oluştur
sistem = ProjeYonetimSistemi()

# 1. Proje oluştur
proje_id = sistem.yeni_proje_olustur(
    "E-Ticaret Sitesi", 
    "01/02/2025", 
    "30/06/2025"
)

# 2. Takım üyeleri ekle
ahmet_id = sistem.takim_uyesi_ekle("Ahmet", "Yılmaz", "Frontend Developer")
mehmet_id = sistem.takim_uyesi_ekle("Mehmet", "Demir", "Backend Developer")
ayse_id = sistem.takim_uyesi_ekle("Ayşe", "Kaya", "UI/UX Designer")

# 3. Görevler oluştur ve ata
gorev1 = sistem.yeni_gorev_tanimla(
    proje_id, 
    "Ana Sayfa Tasarımı", 
    "15/02/2025", 
    ayse_id
)

gorev2 = sistem.yeni_gorev_tanimla(
    proje_id, 
    "Ürün Listesi API", 
    "20/02/2025", 
    mehmet_id
)

gorev3 = sistem.yeni_gorev_tanimla(
    proje_id, 
    "Responsive Tasarım", 
    "25/02/2025", 
    ahmet_id
)

# 4. Görev durumlarını güncelle
sistem.gorev_durumu_guncelle(gorev1, "Yapılıyor")
sistem.gorev_durumu_guncelle(gorev2, "Tamamlandı")

# 5. Raporlar
sistem.projedeki_gorevleri_goruntule(proje_id)
sistem.uyeye_atanan_gorevleri_goruntule(ahmet_id)
sistem.gecikmis_gorevleri_kontrol_et()
```

---

##  Hata Çözümleri

### Sık Karşılaşılan Hatalar

#### 1. Tarih Format Hatası
```
 Hata: Tarih formatı hatalı! (GG/AA/YYYY formatında giriniz)
```
**Çözüm:** Tarihleri GG/AA/YYYY formatında girin. Örnek: 15/02/2025

#### 2. Geçersiz Proje/Üye/Görev ID
```
 Hata: PRJ999 ID'li proje bulunamadı!
```
**Çözüm:** Önce ilgili öğeleri listeleyin ve doğru ID'yi kullanın.

#### 3. Bitiş Tarihi Hatası
```
 Hata: Bitiş tarihi başlangıç tarihinden önce olamaz!
```
**Çözüm:** Bitiş tarihinin başlangıç tarihinden sonra olduğundan emin olun.

#### 4. Geçersiz Durum
```
 Hata: Geçersiz durum! Geçerli durumlar: Bekliyor, Yapılıyor, Tamamlandı
```
**Çözüm:** Sadece belirtilen üç durumdan birini kullanın.

### Programın Çalışmaması

1. **Python versiyonunu kontrol edin:**
   ```bash
   python --version
   ```
   Python 3.6 veya üzeri olmalı.

2. **Dosya yolunu kontrol edin:**
   Terminalin doğru klasörde olduğundan emin olun.

3. **Karakter kodlama sorunları:**
   Türkçe karakterler için terminalde UTF-8 kodlaması olmalı.

---

## 🔧 Geliştirme Notları

### Kullanılan Veri Yapıları
- **Dictionary (dict):** Proje, üye ve görev verilerini saklamak için
- **List (list):** Her proje ve üyeye ait görev ID'lerini saklamak için

### Özellikler
- ✅ Dosya kullanımı yok (isteğe bağlı)
- ✅ Tüm veriler bellekte (RAM) saklanır
- ✅ Program kapatıldığında veriler silinir
- ✅ Türkçe karakter desteği
- ✅ Otomatik ID oluşturma sistemi
- ✅ Tarih validasyonu
- ✅ Hata kontrolü ve kullanıcı dostu mesajlar

### Gelecek Geliştirmeler (Opsiyonel)
- [ ] Verileri dosyaya kaydetme (JSON, CSV veya pickle)
- [ ] Görev öncelik sistemi
- [ ] Alt görev desteği
- [ ] Görev yorumları
- [ ] Grafik kullanıcı arayüzü (GUI)
- [ ] Excel raporları
- [ ] E-posta bildirimleri
- [ ] Gantt chart görselleştirmesi

---

## 📄 Lisans

Bu proje eğitim amaçlı geliştirilmiştir.

---

## 📞 İletişim

Sorularınız için:
- **Öğrenci:** İsmail Eren Arslan
- **E-posta:** ismailerenarslan@gmail.com


---

## 🙏 Teşekkürler

Bu projeyi kullandığınız için teşekkür ederiz! Başarılar dileriz! 🎉

---

**Son Güncelleme:** 29 Ocak 2025