import time

class BazCrypte:
    """
    BazCrypte: Collatz Sanısı ve XOR entropisi kullanan
    özelleştirilmiş sözde rastgele sayı üreteci (PRNG).
    """
    
    def __init__(self, ana_cekirdek, yedek_cekirdek):
        # Başlangıç tohumlarını (seeds) alıyoruz
        self.deger_a = ana_cekirdek
        self.deger_b = yedek_cekirdek
        self.baslangic_a = ana_cekirdek  # Referans için sakla
        self.baslangic_b = yedek_cekirdek

    def _collatz_adim(self, sayi):
        """Bir sayıya Collatz kuralını uygular ve yeni değeri döndürür."""
        if sayi % 2 == 0:
            return sayi // 2
        else:
            return 3 * sayi + 1

    def _dongu_kirici(self):
        """
        Sayılar 4-2-1 döngüsüne girerse sistemi tazelemek için
        zaman tabanlı dinamik bir yenileme yapar.
        """
        zaman_damgasi = int(time.time() * 1000)
        self.deger_a = (zaman_damgasi % 9973) + 7   # 9973 bir asal sayıdır
        self.deger_b = (zaman_damgasi % 9967) + 13  # 9967 bir asal sayıdır

    def rastgele_bit_uret(self, bit_uzunlugu=1024):
        """
        Belirtilen uzunlukta rastgele bit dizisi (string) üretir.
        Yöntem: Trend Analizi (Artış/Azalış) XOR Parite (Tek/Çift)
        """
        bit_havuzu = ""
        
        while len(bit_havuzu) < bit_uzunlugu:
            onceki_a = self.deger_a
            
            # Her iki kanalı (channel) ilerlet
            self.deger_a = self._collatz_adim(self.deger_a)
            self.deger_b = self._collatz_adim(self.deger_b)
            
       
            
            # 1. Kanal A: Sayı yükseldi mi düştü mü? (Trend analizi)
            # Yükseliş kaos yaratır, düşüş düzen yaratır.
            kanal_a_bit = 1 if self.deger_a > onceki_a else 0
            
            # 2. Kanal B: Sayı Tek mi Çift mi? (Klasik modülo)
            kanal_b_bit = 1 if self.deger_b % 2 == 0 else 0
            
            # 3. Karıştırma: İki farklı mantığı XOR kapısından geçir
            sonuc_bit = kanal_a_bit ^ kanal_b_bit
            
            bit_havuzu += str(sonuc_bit)
            
            # Eğer 1'e ulaştıysak döngüden kurtar
            if self.deger_a == 1 or self.deger_b == 1:
                self._dongu_kirici()
                
        return bit_havuzu

    def rsa_icin_sayi_uret(self, bit_uzunlugu):
        """
        Üretilen bitleri doğrudan tam sayıya (integer) çevirir.
        RSA p ve q adayları için kullanılır.
        """
        binary_data = self.rastgele_bit_uret(bit_uzunlugu)
        return int(binary_data, 2)

if __name__ == "__main__":
    print("--- BazCrypte RNG Sistemi Başlatılıyor ---\n")
    
    # Kullanıcıdan veya sistemden alınan tohumlar

    rng_sistemi = BazCrypte(ana_cekirdek=1903, yedek_cekirdek=2024)
    
    # 1. Adım: Binary (İkili) Üretim
    bit_uzunlugu = 16 
    ham_veri = rng_sistemi.rastgele_bit_uret(bit_uzunlugu)
    
    # 2. Adım: Decimal (Onluk) Çevirim
    rsa_adayi = rng_sistemi.rsa_icin_sayi_uret(bit_uzunlugu)
    
    print(f"Hedef Bit Uzunluğu : {bit_uzunlugu}")
    print(f"Üretilen Ham Veri  : {ham_veri}")
    print(f"RSA Aday Sayısı    : {rsa_adayi}")
    print("-" * 40)
