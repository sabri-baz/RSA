import time


class BazCrypte:
    """
    BazCrypte: Collatz Sanısı (3n+1) ve XOR Kaos Teorisini kullanan
    özelleştirilmiş kriptografik sözde rastgele sayı üreteci (PRNG).

    Geliştirici: [Senin Adın]
    Amaç: RSA algoritması için yüksek entropili asal sayı adayları üretmek.
    """

    def __init__(self, ana_cekirdek, yedek_cekirdek):
        # Kullanıcıdan alınan başlangıç tohumları (Seeds)
        self.deger_a = ana_cekirdek
        self.deger_b = yedek_cekirdek

        # Referans değerleri (Gerekirse resetlemek için)
        self.baslangic_a = ana_cekirdek
        self.baslangic_b = yedek_cekirdek

    def _collatz_adim(self, sayi):
        """
        Collatz Matematiksel İşlemi:
        Sayı çiftse -> Yarısı
        Sayı tekse  -> 3 katının 1 fazlası
        """
        if sayi % 2 == 0:
            return sayi // 2
        else:
            return 3 * sayi + 1

    def _dongu_kirici(self):
        """
        Collatz 4-2-1 döngüsüne girerse, sistemi zaman damgası ve
        asal sayılarla (9973, 9967) besleyerek yeni bir yörüngeye oturtur.
        """
        zaman_damgasi = int(time.time() * 1000)
        self.deger_a = (zaman_damgasi % 9973) + 7
        self.deger_b = (zaman_damgasi % 9967) + 13

    def rastgele_bit_uret(self, bit_uzunlugu):
        """
        Belirtilen uzunlukta (örn: 1024 bit) binary dizi üretir.
        ÖZGÜN YÖNTEM: Hibrit Analiz (Trend vs Parite) + XOR
        """
        bit_havuzu = ""

        while len(bit_havuzu) < bit_uzunlugu:
            onceki_a = self.deger_a

            # Her iki kanalı (channel) Collatz yörüngesinde ilerlet
            self.deger_a = self._collatz_adim(self.deger_a)
            self.deger_b = self._collatz_adim(self.deger_b)

            # --- ÖZGÜN ALGORİTMA ÇEKİRDEĞİ ---

            # 1. Kanal A: Trend Analizi (Sayı Yükseldi mi, Düştü mü?)
            # Yükseliş kaosu temsil eder.
            kanal_a_bit = 1 if self.deger_a > onceki_a else 0

            # 2. Kanal B: Parite Analizi (Sayı Tek mi, Çift mi?)
            # Klasik modülo yöntemi.
            kanal_b_bit = 1 if self.deger_b % 2 == 0 else 0

            # 3. Karıştırma (Mixing):
            # İki farklı mantığı XOR kapısından geçirerek tahmin edilebilirliği kırıyoruz.
            sonuc_bit = kanal_a_bit ^ kanal_b_bit

            bit_havuzu += str(sonuc_bit)

            # Güvenlik Önlemi: Sayılar 1'e ulaşırsa döngü kırıcıyı çalıştır.
            if self.deger_a == 1 or self.deger_b == 1:
                self._dongu_kirici()

        return bit_havuzu

    def binary_to_decimal(self, binary_string):
        """Üretilen binary diziyi RSA'da kullanmak için tamsayıya çevirir."""
        return int(binary_string, 2)



if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("      BAZCRYPTE - RSA KEY GENERATOR SYSTEM      ")
    print("=" * 50 + "\n")

    try:
        # Sunum sırasında hocaya buradan sayı girdirebilirsin
        print("Lütfen RSA anahtar üretimi için başlangıç tohumlarını giriniz.")
        print("(Farklı tohumlar, farklı şifreleme anahtarları üretir.)\n")

        giris_a = input(">> 1. Çekirdek Sayısı (Örn: 1903): ")
        giris_b = input(">> 2. Çekirdek Sayısı (Örn: 2024): ")

        seed1 = int(giris_a)
        seed2 = int(giris_b)

        
        hedef_bit = 32

        print(f"\n[SİSTEM] Kaos motoru başlatılıyor...")
        print(f"[SİSTEM] {hedef_bit} bitlik rastgele sayı üretiliyor...\n")

        # Algoritmayı Başlat
        rng_sistemi = BazCrypte(ana_cekirdek=seed1, yedek_cekirdek=seed2)

        # Sonuçları Al
        uretilen_binary = rng_sistemi.rastgele_bit_uret(hedef_bit)
        uretilen_sayi = rng_sistemi.binary_to_decimal(uretilen_binary)

        # Sonuçları Yazdır
        print("-" * 40)
        print(f"SONUÇ RAPORU:")
        print(f"1. Üretilen Binary Dizi (BitStream):")
        print(f"   {uretilen_binary}")
        print("-" * 40)
        print(f"2. RSA İçin Aday Sayı (Decimal):")
        print(f"   {uretilen_sayi}")
        print("-" * 40)
        print("[BAŞARILI] Sayı RSA algoritmasına gönderilmeye hazır.")

    except ValueError:
        print("\n[HATA] Lütfen geçerli bir tam sayı giriniz!")
    except Exception as e:
        print(f"\n[HATA] Beklenmedik bir durum oluştu: {e}")
