"""
Proje Başlığı: Basit Bir Proje Yönetim Sistemi Uygulaması
Öğrenci: İsmail Eren Arslan

"""

from datetime import datetime

class ProjeYonetimSistemi:
    def __init__(self):
        # Dictionary ve List veri yapıları kullanılıyor
        self.projeler = {}  # {proje_id: proje_bilgileri}
        self.takim_uyeleri = {}  # {uye_id: uye_bilgileri}
        self.gorevler = {}  # {gorev_id: gorev_bilgileri}
        self.proje_sayaci = 0
        self.uye_sayaci = 0
        self.gorev_sayaci = 0
    
    # ========== PROJE YÖNETİMİ ==========
    
    def yeni_proje_olustur(self, proje_adi, baslangic_tarihi, bitis_tarihi):
        """Yeni proje oluşturma"""
        try:
            baslangic = datetime.strptime(baslangic_tarihi, "%d/%m/%Y")
            bitis = datetime.strptime(bitis_tarihi, "%d/%m/%Y")
            
            if bitis < baslangic:
                print(" Hata: Bitiş tarihi başlangıç tarihinden önce olamaz!")
                return None
            
            self.proje_sayaci += 1
            proje_id = f"PRJ{self.proje_sayaci:03d}"
            
            self.projeler[proje_id] = {
                'id': proje_id,
                'ad': proje_adi,
                'baslangic_tarihi': baslangic_tarihi,
                'bitis_tarihi': bitis_tarihi,
                'gorevler': []  # Bu projeye ait görev ID'leri
            }
            
            print(f" Proje başarıyla oluşturuldu!")
            print(f"Proje ID: {proje_id}")
            print(f"Proje Adı: {proje_adi}")
            print(f"Başlangıç: {baslangic_tarihi}, Bitiş: {bitis_tarihi}")
            return proje_id
            
        except ValueError:
            print(" Hata: Tarih formatı hatalı! (GG/AA/YYYY formatında giriniz)")
            return None
    
    def projeleri_listele(self):
        """Tüm projeleri görüntüleme"""
        if not self.projeler:
            print(" Henüz proje oluşturulmamış.")
            return
        
        print("\n" + "="*60)
        print(" PROJELER LİSTESİ")
        print("="*60)
        for proje_id, proje in self.projeler.items():
            print(f"\nProje ID: {proje_id}")
            print(f"Proje Adı: {proje['ad']}")
            print(f"Başlangıç: {proje['baslangic_tarihi']}")
            print(f"Bitiş: {proje['bitis_tarihi']}")
            print(f"Görev Sayısı: {len(proje['gorevler'])}")
            print("-" * 60)
    
    # ========== TAKIM ÜYELERİ YÖNETİMİ ==========
    
    def takim_uyesi_ekle(self, ad, soyad, pozisyon):
        """Takım üyesi ekleme"""
        self.uye_sayaci += 1
        uye_id = f"UYE{self.uye_sayaci:03d}"
        
        self.takim_uyeleri[uye_id] = {
            'id': uye_id,
            'ad': ad,
            'soyad': soyad,
            'pozisyon': pozisyon,
            'gorevler': []  # Bu üyeye atanan görev ID'leri
        }
        
        print(f" Takım üyesi başarıyla eklendi!")
        print(f"Üye ID: {uye_id}")
        print(f"Ad Soyad: {ad} {soyad}")
        print(f"Pozisyon: {pozisyon}")
        return uye_id
    
    def takim_uyesi_sil(self, uye_id):
        """Takım üyesi silme"""
        if uye_id not in self.takim_uyeleri:
            print(f" Hata: {uye_id} ID'li üye bulunamadı!")
            return False
        
        uye = self.takim_uyeleri[uye_id]
        
        # Üyeye atanmış görevleri kontrol et
        if uye['gorevler']:
            print(f"  Uyarı: {uye['ad']} {uye['soyad']} üyesine atanmış {len(uye['gorevler'])} görev var.")
            print("Bu görevler ataması kaldırılacak.")
            
            # Görevlerden üye atamasını kaldır
            for gorev_id in uye['gorevler']:
                if gorev_id in self.gorevler:
                    self.gorevler[gorev_id]['atanan_uye'] = None
        
        # Üyeyi sil
        silinen_uye = self.takim_uyeleri.pop(uye_id)
        print(f" {silinen_uye['ad']} {silinen_uye['soyad']} başarıyla silindi!")
        return True
    
    def takim_uyelerini_goruntule(self):
        """Takım üyelerini görüntüleme"""
        if not self.takim_uyeleri:
            print(" Henüz takım üyesi eklenmemiş.")
            return
        
        print("\n" + "="*60)
        print(" TAKIM ÜYELERİ LİSTESİ")
        print("="*60)
        for uye_id, uye in self.takim_uyeleri.items():
            print(f"\nÜye ID: {uye_id}")
            print(f"Ad Soyad: {uye['ad']} {uye['soyad']}")
            print(f"Pozisyon: {uye['pozisyon']}")
            print(f"Atanan Görev Sayısı: {len(uye['gorevler'])}")
            print("-" * 60)
    
    # ========== GÖREV YÖNETİMİ ==========
    
    def yeni_gorev_tanimla(self, proje_id, gorev_adi, son_teslim_tarihi, atanan_uye_id=None):
        """Yeni görev tanımlama ve görev atama"""
        if proje_id not in self.projeler:
            print(f" Hata: {proje_id} ID'li proje bulunamadı!")
            return None
        
        if atanan_uye_id and atanan_uye_id not in self.takim_uyeleri:
            print(f" Hata: {atanan_uye_id} ID'li üye bulunamadı!")
            return None
        
        try:
            datetime.strptime(son_teslim_tarihi, "%d/%m/%Y")
        except ValueError:
            print(" Hata: Tarih formatı hatalı! (GG/AA/YYYY formatında giriniz)")
            return None
        
        self.gorev_sayaci += 1
        gorev_id = f"TSK{self.gorev_sayaci:03d}"
        
        self.gorevler[gorev_id] = {
            'id': gorev_id,
            'proje_id': proje_id,
            'ad': gorev_adi,
            'son_teslim_tarihi': son_teslim_tarihi,
            'atanan_uye': atanan_uye_id,
            'durum': 'Bekliyor'  # Varsayılan durum
        }
        
        # Projeye görevi ekle
        self.projeler[proje_id]['gorevler'].append(gorev_id)
        
        # Eğer atama yapıldıysa, üyeye görevi ekle
        if atanan_uye_id:
            self.takim_uyeleri[atanan_uye_id]['gorevler'].append(gorev_id)
        
        print(f" Görev başarıyla oluşturuldu!")
        print(f"Görev ID: {gorev_id}")
        print(f"Görev Adı: {gorev_adi}")
        print(f"Son Teslim: {son_teslim_tarihi}")
        if atanan_uye_id:
            uye = self.takim_uyeleri[atanan_uye_id]
            print(f"Atanan Kişi: {uye['ad']} {uye['soyad']}")
        return gorev_id
    
    def gorevi_ata(self, gorev_id, uye_id):
        """Görevi bir takım üyesine atama"""
        if gorev_id not in self.gorevler:
            print(f" Hata: {gorev_id} ID'li görev bulunamadı!")
            return False
        
        if uye_id not in self.takim_uyeleri:
            print(f" Hata: {uye_id} ID'li üye bulunamadı!")
            return False
        
        gorev = self.gorevler[gorev_id]
        eski_uye = gorev['atanan_uye']
        
        # Eski üyeden görevi kaldır
        if eski_uye and eski_uye in self.takim_uyeleri:
            if gorev_id in self.takim_uyeleri[eski_uye]['gorevler']:
                self.takim_uyeleri[eski_uye]['gorevler'].remove(gorev_id)
        
        # Yeni üyeye görevi ata
        gorev['atanan_uye'] = uye_id
        if gorev_id not in self.takim_uyeleri[uye_id]['gorevler']:
            self.takim_uyeleri[uye_id]['gorevler'].append(gorev_id)
        
        uye = self.takim_uyeleri[uye_id]
        print(f" {gorev['ad']} görevi {uye['ad']} {uye['soyad']} üyesine atandı!")
        return True
    
    def gorev_durumu_guncelle(self, gorev_id, yeni_durum):
        """Görev durumu belirleme (Bekliyor, Yapılıyor, Tamamlandı)"""
        if gorev_id not in self.gorevler:
            print(f" Hata: {gorev_id} ID'li görev bulunamadı!")
            return False
        
        gecerli_durumlar = ['Bekliyor', 'Yapılıyor', 'Tamamlandı']
        if yeni_durum not in gecerli_durumlar:
            print(f" Hata: Geçersiz durum! Geçerli durumlar: {', '.join(gecerli_durumlar)}")
            return False
        
        eski_durum = self.gorevler[gorev_id]['durum']
        self.gorevler[gorev_id]['durum'] = yeni_durum
        
        print(f" Görev durumu güncellendi!")
        print(f"Görev: {self.gorevler[gorev_id]['ad']}")
        print(f"{eski_durum} → {yeni_durum}")
        return True
    
    # ========== RAPORLAMA ==========
    
    def projedeki_gorevleri_goruntule(self, proje_id):
        """Bir projedeki tüm görevleri görüntüleme"""
        if proje_id not in self.projeler:
            print(f" Hata: {proje_id} ID'li proje bulunamadı!")
            return
        
        proje = self.projeler[proje_id]
        gorev_listesi = proje['gorevler']
        
        print("\n" + "="*80)
        print(f" PROJE GÖREVLERİ: {proje['ad']}")
        print("="*80)
        
        if not gorev_listesi:
            print("Bu projede henüz görev bulunmuyor.")
            return
        
        for gorev_id in gorev_listesi:
            if gorev_id in self.gorevler:
                gorev = self.gorevler[gorev_id]
                print(f"\nGörev ID: {gorev_id}")
                print(f"Görev Adı: {gorev['ad']}")
                print(f"Son Teslim: {gorev['son_teslim_tarihi']}")
                print(f"Durum: {gorev['durum']}")
                
                if gorev['atanan_uye']:
                    uye = self.takim_uyeleri[gorev['atanan_uye']]
                    print(f"Atanan: {uye['ad']} {uye['soyad']}")
                else:
                    print("Atanan: Henüz atanmadı")
                print("-" * 80)
    
    def uyeye_atanan_gorevleri_goruntule(self, uye_id):
        """Her üyeye atanan görevleri görüntüleme"""
        if uye_id not in self.takim_uyeleri:
            print(f" Hata: {uye_id} ID'li üye bulunamadı!")
            return
        
        uye = self.takim_uyeleri[uye_id]
        gorev_listesi = uye['gorevler']
        
        print("\n" + "="*80)
        print(f" ÜYE GÖREVLERİ: {uye['ad']} {uye['soyad']} ({uye['pozisyon']})")
        print("="*80)
        
        if not gorev_listesi:
            print("Bu üyeye henüz görev atanmamış.")
            return
        
        for gorev_id in gorev_listesi:
            if gorev_id in self.gorevler:
                gorev = self.gorevler[gorev_id]
                proje = self.projeler[gorev['proje_id']]
                
                print(f"\nGörev ID: {gorev_id}")
                print(f"Görev Adı: {gorev['ad']}")
                print(f"Proje: {proje['ad']}")
                print(f"Son Teslim: {gorev['son_teslim_tarihi']}")
                print(f"Durum: {gorev['durum']}")
                print("-" * 80)
    
    def gecikmis_gorevleri_kontrol_et(self):
        """Gecikmiş durumdaki görevleri kontrol etme"""
        bugun = datetime.now()
        gecikmis_gorevler = []
        
        for gorev_id, gorev in self.gorevler.items():
            # Eğer görev tamamlanmadıysa ve son teslim tarihi geçtiyse
            if gorev['durum'] != 'Tamamlandı':
                son_teslim = datetime.strptime(gorev['son_teslim_tarihi'], "%d/%m/%Y")
                if son_teslim < bugun:
                    gecikmis_gorevler.append(gorev_id)
        
        print("\n" + "="*80)
        print("  GECİKMİŞ GÖREVLER")
        print("="*80)
        
        if not gecikmis_gorevler:
            print(" Gecikmiş görev bulunmuyor!")
            return
        
        print(f"Toplam {len(gecikmis_gorevler)} gecikmiş görev bulundu:\n")
        
        for gorev_id in gecikmis_gorevler:
            gorev = self.gorevler[gorev_id]
            proje = self.projeler[gorev['proje_id']]
            
            son_teslim = datetime.strptime(gorev['son_teslim_tarihi'], "%d/%m/%Y")
            gecikme_gun = (bugun - son_teslim).days
            
            print(f"Görev ID: {gorev_id}")
            print(f"Görev Adı: {gorev['ad']}")
            print(f"Proje: {proje['ad']}")
            print(f"Son Teslim: {gorev['son_teslim_tarihi']}")
            print(f"Durum: {gorev['durum']}")
            print(f"Gecikme: {gecikme_gun} gün")
            
            if gorev['atanan_uye']:
                uye = self.takim_uyeleri[gorev['atanan_uye']]
                print(f"Atanan: {uye['ad']} {uye['soyad']}")
            else:
                print("Atanan: Henüz atanmadı")
            print("-" * 80)


# ========== ANA MENÜ VE KULLANICI ARAYÜZÜ ==========

def ana_menu():
    """Ana menü"""
    sistem = ProjeYonetimSistemi()
    
    while True:
        print("\n" + "="*60)
        print(" PROJE YÖNETİM SİSTEMİ")
        print("="*60)
        print("1. Proje Yönetimi")
        print("2. Takım Üyeleri Yönetimi")
        print("3. Görev Yönetimi")
        print("4. Raporlama")
        print("0. Çıkış")
        print("="*60)
        
        secim = input("Seçiminiz (0-4): ").strip()
        
        if secim == "1":
            proje_menu(sistem)
        elif secim == "2":
            takim_menu(sistem)
        elif secim == "3":
            gorev_menu(sistem)
        elif secim == "4":
            raporlama_menu(sistem)
        elif secim == "0":
            print("\n Programdan çıkılıyor... Güle güle!")
            break
        else:
            print(" Geçersiz seçim! Lütfen 0-4 arası bir sayı girin.")


def proje_menu(sistem):
    """Proje yönetimi menüsü"""
    while True:
        print("\n" + "-"*60)
        print(" PROJE YÖNETİMİ")
        print("-"*60)
        print("1. Yeni Proje Oluştur")
        print("2. Projeleri Listele")
        print("0. Ana Menüye Dön")
        
        secim = input("Seçiminiz: ").strip()
        
        if secim == "1":
            print("\n--- Yeni Proje Oluşturma ---")
            ad = input("Proje Adı: ").strip()
            baslangic = input("Başlangıç Tarihi (GG/AA/YYYY): ").strip()
            bitis = input("Bitiş Tarihi (GG/AA/YYYY): ").strip()
            sistem.yeni_proje_olustur(ad, baslangic, bitis)
            
        elif secim == "2":
            sistem.projeleri_listele()
            
        elif secim == "0":
            break
        else:
            print(" Geçersiz seçim!")


def takim_menu(sistem):
    """Takım üyeleri yönetimi menüsü"""
    while True:
        print("\n" + "-"*60)
        print("👥 TAKIM ÜYELERİ YÖNETİMİ")
        print("-"*60)
        print("1. Takım Üyesi Ekle")
        print("2. Takım Üyesi Sil")
        print("3. Takım Üyelerini Görüntüle")
        print("0. Ana Menüye Dön")
        
        secim = input("Seçiminiz: ").strip()
        
        if secim == "1":
            print("\n--- Yeni Takım Üyesi Ekleme ---")
            ad = input("Ad: ").strip()
            soyad = input("Soyad: ").strip()
            pozisyon = input("Pozisyon: ").strip()
            sistem.takim_uyesi_ekle(ad, soyad, pozisyon)
            
        elif secim == "2":
            print("\n--- Takım Üyesi Silme ---")
            uye_id = input("Silinecek Üye ID: ").strip()
            sistem.takim_uyesi_sil(uye_id)
            
        elif secim == "3":
            sistem.takim_uyelerini_goruntule()
            
        elif secim == "0":
            break
        else:
            print(" Geçersiz seçim!")


def gorev_menu(sistem):
    """Görev yönetimi menüsü"""
    while True:
        print("\n" + "-"*60)
        print(" GÖREV YÖNETİMİ")
        print("-"*60)
        print("1. Yeni Görev Tanımla")
        print("2. Görevi Üyeye Ata")
        print("3. Görev Durumunu Güncelle")
        print("0. Ana Menüye Dön")
        
        secim = input("Seçiminiz: ").strip()
        
        if secim == "1":
            print("\n--- Yeni Görev Tanımlama ---")
            proje_id = input("Proje ID: ").strip()
            gorev_adi = input("Görev Adı: ").strip()
            son_teslim = input("Son Teslim Tarihi (GG/AA/YYYY): ").strip()
            atama = input("Şimdi bir üyeye atamak ister misiniz? (E/H): ").strip().upper()
            
            uye_id = None
            if atama == "E":
                uye_id = input("Atanacak Üye ID: ").strip()
            
            sistem.yeni_gorev_tanimla(proje_id, gorev_adi, son_teslim, uye_id)
            
        elif secim == "2":
            print("\n--- Görev Atama ---")
            gorev_id = input("Görev ID: ").strip()
            uye_id = input("Atanacak Üye ID: ").strip()
            sistem.gorevi_ata(gorev_id, uye_id)
            
        elif secim == "3":
            print("\n--- Görev Durumu Güncelleme ---")
            gorev_id = input("Görev ID: ").strip()
            print("Durum Seçenekleri: Bekliyor, Yapılıyor, Tamamlandı")
            yeni_durum = input("Yeni Durum: ").strip()
            sistem.gorev_durumu_guncelle(gorev_id, yeni_durum)
            
        elif secim == "0":
            break
        else:
            print(" Geçersiz seçim!")


def raporlama_menu(sistem):
    """Raporlama menüsü"""
    while True:
        print("\n" + "-"*60)
        print(" RAPORLAMA")
        print("-"*60)
        print("1. Projedeki Görevleri Görüntüle")
        print("2. Üyeye Atanan Görevleri Görüntüle")
        print("3. Gecikmiş Görevleri Kontrol Et")
        print("0. Ana Menüye Dön")
        
        secim = input("Seçiminiz: ").strip()
        
        if secim == "1":
            proje_id = input("Proje ID: ").strip()
            sistem.projedeki_gorevleri_goruntule(proje_id)
            
        elif secim == "2":
            uye_id = input("Üye ID: ").strip()
            sistem.uyeye_atanan_gorevleri_goruntule(uye_id)
            
        elif secim == "3":
            sistem.gecikmis_gorevleri_kontrol_et()
            
        elif secim == "0":
            break
        else:
            print(" Geçersiz seçim!")


# Programı çalıştır
if __name__ == "__main__":
    print("""
    ╔═══════════════════════════════════════════════════════════╗
    ║                                                           ║
    ║        PROJE YÖNETİM SİSTEMİ                              ║
    ║        Basit Bir Proje Yönetim Sistemi Uygulaması         ║
    ║                                                           ║
    ╚═══════════════════════════════════════════════════════════╝
    """)
    ana_menu()
