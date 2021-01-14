# -*- coding: utf-8 -*-

"""
for_loop
"""

# spyonde:ignore-cell

# pylint: disable=C0103
# Constant name doesn't conform to UPPER_CASE naming style (invalid-name)

# pylint: disable=C0301
# Line too long (105/100) (line-too-long)

# pylint: disable=C0413
# Import should be placed at the top of the module (wrong-import-position)

# pylint: disable=C0412
# Imports from package are not grouped (ungrouped-imports)

# pylint: disable=W0404
# Reimport (imported line 44) (reimported)



#%% `for` döngüsü

# - `list`, `tuple`, `str`, `dict` gibi veri yapılarının elemanları üzerinde döner.
# - bir listeyi tarayarak, her bir eleman üzerinde işlem yapabiliriz.



#%% `for` döngüsü

sehirler = ["istanbul", "izmir", "ankara"]
for sehir in sehirler:
    print(sehir)



#%% for ile iterasyon

# list, tuple, string, dictionary

list1 = [1, 2, 3]

for item in list1:
    print(item)

tuple1 = (1, 2, 3)

for item in tuple1:
    print(item)

string1 = "abcdef"

for item in string1:
    print(item)

dict1 = {}
dict1["one"] = 1
dict1["two"] = 2
dict1["three"] = 3
dict1["dort"] = 4
dict1["bes"] = 5

for key in dict1:
    value = dict1[key]
    print(key, " : ", value)



#%% for, dictionary üzerinde dönebilir.

ti_sozluk = {}
ti_sozluk["bir"] = "one"
ti_sozluk["iki"] = "two"
ti_sozluk["yedi"] = "seven"

for turkce_kelime in ti_sozluk:
    print(turkce_kelime)

for item in ti_sozluk.items():
    print(item)
    print(type(item))  # <class 'tuple'>



#%% uygulama: for döngüsü ile film listesinde arama yapmak

# - bir film listesi olsun.
# - birkaç alanı varsa, nasıl bir veri tipinde tutmalıyız?
# - kullanıcıdan aranan film bilgisini alalım.
# - filmerde arama yapabilsin.
# - küçük-büyük harf farkı olmasın, hepsini bulsun.



#%% çözüm: for döngüsü ile film listesinde arama yapmak

tum_filmler = ["game of thrones", "godzilla", "matrix", "batman", "lucy", "hababam sinifi", "amerikan pastasi"]

aranan = "ma"  # kullanici girsin.

bulundu = False

for bizdeki_film in tum_filmler:
    if bizdeki_film.find(aranan) > -1:
        print(bizdeki_film)
        bulundu = True

if not bulundu:
    print("oyle bir film yok")



#%% range

# belli bir sayı aralığında döndürmek için, `range()` kullanılır.

for i in range(4):
    print(i)



#%% range(stop)

r1 = range(4)
print(r1)
print(r1[0])
print(r1[3])
print(r1[4])  # hata?



#%% range(start, stop)

r1 = range(2, 4)
print(r1)
print(r1[0])
print(r1[1])



#%% range(start, stop[, step])

r1 = range(2, 9, 3)
print(r1)
print(r1[0])
print(r1[1])
print(r1[2])



#%% uygulama: for ile seri hesaplama

# - x = 1/2 + 2/3 + .... 10/11
# - x'in değeri nedir?



#%% uygulama: list içinde list toplamı
# - bu değişkenin içindeki sayıların toplamını hesaplayınız.
# - `data = [[3, 9, 4], [5, 2, 9], [8, 2, 5]]`



#%% Python 2.x ve 3.x için range() farkı

# Python2: list döndürür
# Python3: range object döndürür

print(range(5))

r1 = range(5)
print(type(r1))
print(r1)



#%% help(range)

help(range)



#%% range nesnesini, listeye çevirmek

# öncelikle, bir range() fonksiyonu ne döndürüyor, onu görelim:
print(type(range(7)))  # <class 'range'>

# tüm elemanları hazır etmek istersek:
li1 = list(range(7))
print(type(li1))  # <class 'list'>



#%% uygulama: list içinde list toplamı

# aşağıdaki veride, tüm hücrelerdeki verinin toplamı nedir?

data = [[3, 9, 4], [5, 2, 9], [8, 2, 5]]



#%% rastgele bir liste oluşturmak için

# daha büyük veri oluşturmak için:
# bir döngü ile beraber, random kullanılabilir:

import random
x = random.randint(0, 9)
print(x)



#%% for ile Uygulama : not ortalaması

# - Kullanıcıdan, sınıftaki öğrenci sayısını alıp, o kadar notu `input()` olarak alan ve ortalamasını yazan program.



#%% for ile Uygulama : break ve continue kullanımı

# - istediğimiz çıktı:

# ```
# 1
# 2
# 3
# 5
# ```



#%% for ile Uygulama : break ve continue kullanımı

for i in range(1, 9):
    if i == 4:
        continue
    elif i == 6:
        break
    print(i)



#%% Uygulama

# şu uygulama ne kadar mantıklı?

# - Kullanıcı, negatif bir sayı girene kadar kullanıcıdan değer alıp, bittiğinde ortalamasını hesaplayan bir program.
# - break ile tekrar yazalım.
#
# ```
# >>> 100
# >>> 80
# >>> 90
# >>> -1
# 270.0
# 90.0
# ```




#%% for-else

# 4 ve 2 degerleri icin deneyelim.

raw_value = input(">>>")
unwanted = int(raw_value)
for item in range(4):
    if item == unwanted:
        break
    else:
        print(item)
else:
    print("all clear")

# else, döngü, break olmadan bitmiş ise çalışır.



#%% Uygulama : histogram

# - Kullanıcıdan, boş giriş yapılana kadar harf alan,
# - sonra da bunların histogramını gösteren bir uygulama
# - bunun, bir `str` üzerinde aynı işlemi yapan versiyonu nasıl yapılırdı?



#%% Uygulama : Tam Sayının Tam Bölenleri

# - Verilen bir tam sayının, tam sayı bölenlerini bulan uygulama
#
# ```
# >>>2
# [1, 2]
#
# >>>3
# [1, 3]
#
# >>>8
# [1, 2, 4, 8]
#
# >>>9
# [1, 3, 9]
# ```


#%% Çözüm : Tam Sayının Tam Bölenleri

bolenler = [1]

number = int(input("enter a number : "))
for bolen in range(2, number+1):
    kalan = number % bolen
    if kalan == 0:
        bolenler.append(bolen)

print(bolenler)

# test:
# 0, 1, n



#%% Uygulama : palindrome testi

# - Kullanıcıdan bir `str` alıp, palindrome mu değil mi tespit eden bir uygulama.
#
# ```
# >>>1
# palindrome
#
# >>>121
# palindrome
#
# >>>1234
# not palindrome
#
# >>>
# palindrome
# ```


#%% Çözüm : palindrome testi

data = input(">>>")
data2 = ""
for ch in data:
    data2 = ch + data2
if data == data2:
    print("palindrome")
else:
    print("not palindrome")

list1 = []
data = input(">>>") # abcdef
for ch in data:
    list1.insert(0, ch)

print(list1)

reversed_data = "".join(list1)
print(reversed_data)

if data == reversed_data:
    print("palindrome")
else:
    print("not palindrome")



#%% Uygulama : factorial

# - Kullanıcıdan bir sayı alarak, factorial hesabı yapan program
# - n! = n * (n-1) * (n-2) .. 1
# - 5! = 5 * 4 * 3 * 2 * 1 = 120
#
# ```
# >>> 0
# 1
# >>> 1
# 1
# >>> 2
# 2
# >>> 3
# 6
# >>> 7
# 5040
# >>> 300
# ???
# ```



#%% Çözüm : factorial

total = 1
num = int(input(">>> "))
if num == 0 or num == 1:
    pass
else:
    for i in range(2, num+1):
        total = total * i

print(total)



#%% Uygulama : çarpım tablosu



#%% Uygulama : pascal üçgeni

# ```
#        1
#     1     1
#    1   2   1
#   1  3   3  1
#  1  4  6  4  1
# 1  5 10 10  5 1
# ```


#%% son
