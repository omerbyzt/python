#   SARI KAGIT

#   SORU 1

alisveris_tutari = 60

if alisveris_tutari > 50:
    print("Alisveris tutari = ",alisveris_tutari)
    print("Kargo ucreti = 0 TL")
    print("Toplam tutar = ", alisveris_tutari)
else:
    print("Alisveris tutari = ", alisveris_tutari)
    print("Kargo ucreti =  7 TL")
    print("Toplam tutar = ", alisveris_tutari + 7)

#   SORU 2

sicaklik_degeri = int(input("Lütfen bir sicaklik degeri giriniz : "))
if sicaklik_degeri <= 0:
    print("0 derecenin altında su kati haldedir")
elif sicaklik_degeri > 0 and sicaklik_degeri < 100:
    print("0-100 derece arasında su sivi haldedir")
else:
    print("100 derenin üstünde su gaz halindedir")

#   SORU 3

harcanan_tutar = int(input("Harcama mikrarini giriniz : "))

if harcanan_tutar <= 1000:
    print("10 tl hediye puan kazandiniz")
elif harcanan_tutar > 1000 and harcanan_tutar <2000:
    print("50 tl hediye puan kazandiniz")
else:
    print("100 tl hediye paun kazandiniz")

#   SORU 4

boy = int(input("Boyunuzu giriniz : "))

if boy <= 170:
    print("boyunuz kisa")
elif boy > 170 and boy < 180:
    print("boyunuz normal")
else:
    print("boyunuz uzun")

#   SORU 5

ortalama = int(input("Lütfen ortalamanızı giriniz : "))

if ortalama < 45:
    print("KALDI")
elif ortalama >= 45 and ortalama < 55:
    print("2")
elif ortalama >= 55 and ortalama < 70:
    print("3")
elif ortalama >= 70 and ortalama <85:
    print("4")
else:
    print("5")

#   SORU 6

yas = int(input("Yasinizi giriniz : "))

if yas < 18:
    print("Bilet fiyatı = 15 TL")
elif yas >= 18 and yas <65:
    print("Bilet fiyati = 20 TL")
else:
    print("Bilet fiyatı = 10")

#   SORU 7

agirlik = float(input("Lütfen agirlik giriniz : "))

if agirlik < 2:
    print("1 kilogram kargo fiyatı = 6 TL")
    print(agirlik, " kg kargo fiyati = ", agirlik * 6)
elif agirlik >= 2 and agirlik < 6:
    print("1 kilogram kargo fiyatı = 5 TL")
    print(agirlik, " kg kargo fiyati = ", agirlik * 5)
elif agirlik >= 6 and agirlik < 10:
    print("1 kilogram kargo fiyatı = 4 TL")
    print(agirlik, " kg kargo fiyati = ", agirlik * 4)
else:
    print("1 kilogram kargo fiyatı = 3 TL")
    print(agirlik, " kg kargo fiyati = ", agirlik * 3)

#   SORU 8

cinsiyet = input("Lütfen cinsiyetinizi giriniz (K/E): ")
boy = int(input("Lütfen boyunuzu giriniz : "))
kilo = int(input("Lütfen kilonuzu giriniz : "))

if cinsiyet.lower() == "k":
    ideal_boy_kilo_orani = boy - 110
    print("Ideal kilonuz = ",ideal_boy_kilo_orani)
    if kilo > ideal_boy_kilo_orani:
        print("Ideal kilonuza erismek icin lütfen ", kilo - ideal_boy_kilo_orani, " kg veriniz")
    elif kilo < ideal_boy_kilo_orani:
        print("Ideal kilonuza erismek icin lütfen ", ideal_boy_kilo_orani - kilo, " kg aliniz")
    else:
        print("Ideal kilonuzdasiniz")
else:
    ideal_boy_kilo_orani = boy - 108
    print("Ideal kilonuz = ", ideal_boy_kilo_orani)
    if kilo > ideal_boy_kilo_orani:
        print("Ideal kilonuza erismek icin lütfen ", kilo - ideal_boy_kilo_orani, " kg veriniz")
    elif kilo < ideal_boy_kilo_orani:
        print("Ideal kilonuza erismek icin lütfen ", ideal_boy_kilo_orani - kilo, " kg aliniz")
    else:
        print("Ideal kilonuzdasiniz")