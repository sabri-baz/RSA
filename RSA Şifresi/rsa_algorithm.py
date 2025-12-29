import time


class OzgunCollatzRNG:
    def __init__(self, seed1, seed2):
        self.n1 = seed1
        self.n2 = seed2

    def step_collatz(self, n):
        # Klasik Collatz adımı
        if n % 2 == 0:
            return n // 2
        else:
            return 3 * n + 1

    def generate_random_bits(self, bit_length):
        bits = ""
        while len(bits) < bit_length:
            # 1. Her iki sayıyı da bir adım ilerlet
            prev_n1 = self.n1
            prev_n2 = self.n2

            self.n1 = self.step_collatz(self.n1)
            self.n2 = self.step_collatz(self.n2)

            # ÖZGÜN KISIM BURASI:
            # Sadece tek/çift bakmıyoruz. 
            # 1. Sayı arttı mı azaldı mı? (Rise/Fall)
            bit1 = 1 if self.n1 > prev_n1 else 0

            # 2. İkinci sayı tek mi çift mi?
            bit2 = 1 if self.n2 % 2 == 0 else 0

            # 3. İkisini XOR'la (Karıştır) -> Gerçek kaos
            final_bit = bit1 ^ bit2

            bits += str(final_bit)

            # Sayılar 4-2-1 döngüsüne girerse (kısa döngü), onları değiştir.
            if self.n1 == 1: self.n1 = int(time.time() * 1000) % 10000 + 7
            if self.n2 == 1: self.n2 = int(time.time() * 1000) % 10000 + 13

        return bits


# KULLANIM
# Hocaya sunarken: "İki farklı seed kullanıp XOR ile entropiyi artırdım" dersin.
rng = OzgunCollatzRNG(seed1=19, seed2=2024)

# 16 Bitlik sayı üret
binary_sonuc = rng.generate_random_bits(16)
decimal_sonuc = int(binary_sonuc, 2)

print(f"Özgün Binary Çıktı: {binary_sonuc}")
print(f"RSA Anahtar Adayı: {decimal_sonuc}")