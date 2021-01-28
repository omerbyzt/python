"""
#   https://www.youtube.com/watch?v=G9RLqNfXstA&list=PLK6Whnd55IH5i1klkNSBDasIaO77l-Bm9&index=9&ab_channel=MertMekatronik

Video sonunda console ekranından çalışacak bir todolist uygulaması yazpılıyor
Girilen komutlara göre bir dosya oluşuturup bu dosyaya eleman ekleme ve çıkarma işlemi yapılıyor

# cikar düzgün calismiyor
"""
import sys

gelenArg = sys.argv[-1]

komutlar = gelenArg.split("_")

if gelenArg == "komutlar":
    print("-yeni_<isim>\n- ekle_<dosya>_<kitapAdi>\n- cikar_<dosya>_<kitapAdi>")

if komutlar[0] == "yeni":
    dosya = open("{}.txt".format(komutlar[1]), "a")
    dosya.close()

if komutlar[0] == "ekle":
    dosya = open("{}.txt".format(komutlar[1]), "a")
    dosya.write("{}\n".format(komutlar[2]))
    dosya.close()

if komutlar[0] == "cikar":
    with open("{}.txt".format(komutlar[1]), "a") as f:
        lines = f.readlines()
    with open("{}.txt".format(komutlar[1]), "a") as f:
        for line in lines:
            if line.strip("\n") != komutlar[2]:
                f.write(line)
