# BazCrypte: Collatz Tabanlı Kriptografik RSA

![Language](https://img.shields.io/badge/language-Python-blue.svg) ![Algorithm](https://img.shields.io/badge/algorithm-Collatz%20Conjecture-orange) ![License](https://img.shields.io/badge/license-MIT-green)

**BazCrypte**, ünlü **Collatz Sanısı (3n+1 Problemi)** ve **XOR Kaos Teorisi** kullanılarak geliştirilmiş özgün bir Sözde Rastgele Sayı Üreteci (PRNG) algoritmasıdır. 

Bu proje, RSA şifreleme algoritmasında kullanılmak üzere yüksek entropiye sahip anahtar adayları (büyük tamsayılar) üretmek amacıyla tasarlanmıştır.

## 🚀 Projenin Amacı

Standart Collatz tabanlı üreteçler genellikle sadece sayının tek/çift (parite) durumuna bakar. Bu durum, kriptografik açıdan tahmin edilebilir desenler oluşturabilir. 

**BazCrypte** algoritması ise bu sorunu çözmek için **3 Katmanlı Hibrit Mimari** kullanır:

1.  **Çift Çekirdek (Dual-Core Seed):** Algoritma tek bir sayı yerine, birbirini etkileyen iki farklı başlangıç tohumu ile çalışır.
2.  **Trend ve Parite Analizi:** * *Kanal A:* Sayının artış/azalış trendini (Volatility) analiz eder.
    * *Kanal B:* Sayının modülo 2 (Tek/Çift) durumunu analiz eder.
3.  **XOR Karıştırma (Mixing):** İki farklı kanaldan gelen veriler XOR kapısından geçirilerek istatistiksel sapmalar yok edilir ve kaos artırılır.


## Algoritmanın pseuudo code ;
## 🧩 Algoritma Sözde Kodu (Pseudo-Code)

Aşağıdaki sözde kod, **BazCrypte** algoritmasının temel çalışma mantığını ve özgün **Hibrit XOR** yapısını özetler:


CLASS BazCrypte:
    GİRDİ: Seed_A (Başlangıç Sayısı 1), Seed_B (Başlangıç Sayısı 2)

    FONKSİYON CollatzAdımı(n):
        EĞER n Çift İSE:
            DÖNDÜR n / 2
        DEĞİLSE:
            DÖNDÜR 3 * n + 1

    FONKSİYON DöngüKırıcı():
        // Sayılar 1'e ulaşıp 4-2-1 döngüsüne girerse sistemi tazele
        zaman = ŞU_ANKİ_MİLİSANİYE()
        Seed_A = (zaman MOD 9973) + 7   // Asal sayı ile modülasyon
        Seed_B = (zaman MOD 9967) + 13

    FONKSİYON RastgeleBitÜret(uzunluk):
        bit_havuzu = ""

        DÖNGÜ (bit_havuzu uzunluğu < istenen_uzunluk):
            eski_A = Seed_A
            
            // 1. ADIM: Yörünge İlerlemesi
            Seed_A = CollatzAdımı(Seed_A)
            Seed_B = CollatzAdımı(Seed_B)

            // 2. ADIM: Hibrit Analiz (ÖZGÜN KATMAN)
            // Kanal A: Trend Analizi (Artış var mı?)
            Bit_1 = 1 EĞER (Seed_A > eski_A) DEĞİLSE 0
            
            // Kanal B: Parite Analizi (Çift mi?)
            Bit_2 = 1 EĞER (Seed_B MOD 2 == 0) DEĞİLSE 0

            // 3. ADIM: Kaos Karıştırma (XOR Gate)
            Sonuç_Bit = Bit_1 XOR Bit_2
            
            bit_havuzu'na Sonuç_Bit ekle

            // 4. ADIM: Güvenlik Kontrolü
            EĞER (Seed_A == 1 VEYA Seed_B == 1):
                DöngüKırıcı()

        DÖNDÜR bit_havuzu

## Algoritma çıktısı
==================================================
      BAZCRYPTE - RSA KEY GENERATOR SYSTEM      
==================================================

Lütfen RSA anahtar üretimi için başlangıç tohumlarını giriniz.
(Farklı tohumlar, farklı şifreleme anahtarları üretir.)

>> 1. Çekirdek Sayısı (Örn: 1903): 200
>> 2. Çekirdek Sayısı (Örn: 2024): 320

[SİSTEM] Kaos motoru başlatılıyor...
[SİSTEM] 32 bitlik rastgele sayı üretiliyor...

----------------------------------------
SONUÇ RAPORU:
1. Üretilen Binary Dizi (BitStream):
   11101001010000111011111110111000
----------------------------------------
2. RSA İçin Aday Sayı (Decimal):
   3913531320
----------------------------------------
[BAŞARILI] Sayı RSA algoritmasına gönderilmeye hazır.


## 📐 Matematiksel Arkaplan

Sistem, temel olarak Collatz fonksiyonu üzerinde çalışır:

$$f(n) = \begin{cases} n/2 & \text{eğer } n \equiv 0 \pmod{2} \\ 3n+1 & \text{eğer } n \equiv 1 \pmod{2} \end{cases}$$

Algoritma, bu yörünge sırasında oluşan kaotik sıçramaları "bit" (0 veya 1) olarak toplar ve RSA algoritması için uygun formata (Decimal Integer) dönüştürür.

### Özellikler
* **Döngü Kırıcı (Loop Breaker):** Collatz'ın meşhur 4-2-1 döngüsüne girildiğinde sistem, zaman damgası ve asal sayılarla (9973, 9967) kendini dinamik olarak yeniler.
* **Esnek Bit Uzunluğu:** İstenilen uzunlukta (16 bit, 1024 bit, 2048 bit vb.) anahtar üretebilir.

## 🛠 Kurulum ve Kullanım

Projeyi bilgisayarınıza klonlayın:


git clone [https://github.com/KULLANICI_ADIN/BazCrypte.git](https://github.com/KULLANICI_ADIN/BazCrypte.git)
cd BazCrypte
'''

Algoritmayı çalıştırmak için:

python bazcrypte.py kodunu çalıştırın


