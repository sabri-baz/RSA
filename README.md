# BazCrypte: Collatz Tabanlı Kriptografik RNG

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


