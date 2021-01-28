#   BEYAZ KAGIT

# SORU 1

kenar_A = 5
kenar_B = 10
print("kenar A :", kenar_A)
print("kenar B :", kenar_B)

cevre = 2 * (kenar_A + kenar_B)
print("dikdortgenin cevresi :", cevre)

alan = kenar_A * kenar_B
print("dikdortgenin alani :", alan)

#   SORU 2
# 1 paund = 0.45 kg

kilogram = 10

print(kilogram," = ",(kilogram * 0.45), " pound eder")

#   SORU 3

sayi = int(input("Lütfen bir sayi giriniz : "))

if sayi < 0:
    print(sayi,"'si negatif bir sayidir")
else:
    print(sayi,"'si pozitif bir sayidir")

#   SORU 4

sayi = int(input("Lütfen bir sayi giriniz : "))

if sayi % 3 == 0:
    print(sayi,"'si 3 un katidir")
else:
    print(sayi, "'si 3 un kati değildir")

#   SORU 5

for i in range(20, 1, -4):
    print(i)

#   SORU 6

for i in range(1, 11):
    print(i)

#   SORU 7

girilen_sayi_adeti = 0
girilen_sayilarin_toplamı = 0

while True:
    girilen_sayi_string = input("Lütfen bir sayi giriniz : ")
    if girilen_sayi_string != '':
        girilen_sayi = int(girilen_sayi_string)
        girilen_sayilarin_toplamı += girilen_sayi
        girilen_sayi_adeti += 1
    else:
        break

print("Girilen sayi adeti = ", girilen_sayi_adeti)
print("Girilen sayilarin toplamı = ", girilen_sayilarin_toplamı)
print("Girilen sayilarin ortalamasi = ", girilen_sayilarin_toplamı / girilen_sayi_adeti)
