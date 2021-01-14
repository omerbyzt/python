# -*- coding: utf-8 -*-

"""
if-elif-else
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



#%% Akış Denetimi if-elif-else

# - operatörler
# - bloklar
# - if



#%% boolean değişkenler

a = True
b = False
print(a)
print(b)
print(a == b)
esit_mi = a == b
dogru = True
izlendi = False
bulundu = True


#%% mantıksal (logical) operatörler

# - `and`
# - `or`
# - `not`



#%% `and` operatörü

a = True
b = True
c = False
d = False

print(a and b)
print(a and c)
print(c and d)



#%% `or` operatorü

a = True
b = True
c = False
d = False

print(a or b)
print(a or c)
print(c or d)



#%% `not` operatorü

a = True
b = True
c = False
d = False

print(a)
print(not a)
print(c)
print(not c)



#%% Karşılaştırma operatörleri

# ```
# ==
# != ( Python 2 : <> )
# >
# <
# >=
# <=
# ```



#%% Atama (assignment) operatörleri

# ```
# =
#
# +=
# -=
#
# *=
# /=
# %=
# **=
# //=
# ```



#%% if deyimi

# ```python
# if ifade:
#     blok
#     blok
# ```
#
# - indentation (girintileme)
# - PEP8'e göre 4 space kullanılır, tab tuşuna basılır ama tab karakteri  kullanılmaz.
# - ifade parantez içinde olmak zorunda değildir.



#%% if ile şifre kontrol

gizli_sifre = "12345"
girilen_sifre = input("sifreyi giriniz:")
esit_mi = gizli_sifre == girilen_sifre
print(esit_mi)
print(type(esit_mi))  # <class 'bool'>
if esit_mi:
    print("login olabilirsiniz.")

# ya da:
if gizli_sifre == girilen_sifre:
    print("login olabilirsiniz.")



#%% if deyimi

if 5 > 4:
    print("5 buyuk")

if 1:
    print("hep 1")

if True:
    print("hep True")



#%% if - else deyimi

# ```python
# if ifade:
#     blok
#     blok
# else:
#     blok
#     blok
# ```



#%% Uygulama : 2 sayı eşitliği

# - Kullanıcıdan 2 sayı al, eğer eşitlerse eşit yazsın.
# - Eşit değillerse, eşit değil yazsın.
# - Buna ek olarak, eğer alınan değer 6 ise, ek olarak, "en sevdiğim sayı" desin.



#%% Uygulama : Bankamızdan SMS almak ister misiniz?

# - kullanıcıya soru sorup, cevabını yazan bir uygulama yazalım.



#%% Çözüm : Bankamızdan SMS almak ister misiniz?

# kullanıcıya soru sorup, cevabını yazan bir uygulama yazalım.

cevap = input("SMS almak ister misiniz? e/h")
sms_gonderilsin = False
if cevap == "e":
    sms_gonderilsin = True

if sms_gonderilsin:
    print("reklam gonderilecek")



#%% if - elif - else deyimi

# ```python
# if ifade1:
#     blok
# elif ifade2:
#     blok
# elif ifade3:
#     blok
# elif ifade4:
#     blok
# else:
#     blok
# ```



#%% Uygulama: Yol ücretleri hesaplama

# - Verilen tablolara göre, yolcunun nereye gideceğini, ve business-class mı uçacağını sorup,
# - buna göre toplam ücreti hesaplayan bir uygulama yazınız.
# - Eğer gitmek istediği yer, tabloda yoksa, yolcuya bunu da belirtiniz.
#
#
# ```
# Barcelona | 200
# Paris     | 200
# Milano    | 150
# Atina     | 100
# Ankara    | 50
# ```
#
# ```
# Business | +100
# ```



#%% Uygulama : puan-not çevirisi

# - Kullanıcıdan bir puan alalım.
# - Aşağıdaki aralıklara göre, notunu harf olarak belirleyelim.
#
# ```
# D: 0 .. 50
# C: 51 .. 65
# B: 66 .. 85
# A: 86 .. 100
# ```



#%% Uygulama : operator ve 2 sayı almak

# - Kullanıcıdan 1 operatör ve iki de sayı alıp, sonucunu yazan bir uygulama yazınız.
#
# ```
# operand1 >>> 3
# operator >>> +
# operand2 >>> 2
# 3.0 + 2.0 = 5.0
# ```



#%% Çözüm : operator ve 2 sayı almak

# - Kullanıcıdan 1 operatör ve iki de sayı alıp, sonucunu yazan bir uygulama yazınız.
#
# ```python
# operand1 = float(input("operand1 >>> "))
# operator = input("operator >>> ")
# operand2 = float(input("operand2 >>> "))
#
# if operator == "+":
#     result = operand1 + operand2
# elif operator == "-":
#     result = operand1 - operand2
# elif operator == "*":
#     result = operand1 * operand2
# elif operator == "/":
#     result = operand1 / operand2
# elif operator == "//":
#     result = operand1 // operand2
#
# print("{} {} {} = {}".format(operand1, operator, operand2, result))
# ```



#%% Uygulama : 3 sayı içinde min ve max

# - Kullanıcıdan 3 sayı alarak, en büyük ve en küçük olanını ekrana yazan uygulama
#
# ```
# >>>1
# >>>2
# >>>3
# max :  3.0
# min :  1.0
# ```



#%% Çözüm : 3 sayı içinde min ve max

# Kullanıcıdan 3 sayı alarak, en büyük ve en küçük olanını ekrana yazan uygulama

n1 = float(input(">>>"))
n2 = float(input(">>>"))
n3 = float(input(">>>"))

if (n1 >= n2) and (n1 >= n3):
    print("max : ", n1)
elif (n2 >= n1) and (n2 >= n3):
    print("max : ", n2)
elif (n3 >= n1) and (n3 >= n2):
    print("max : ", n3)

if (n1 <= n2) and (n1 <= n3):
    print("min : ", n1)
elif (n2 <= n1) and (n2 <= n3):
    print("min : ", n2)
elif (n3 <= n1) and (n3 <= n2):
    print("min : ", n3)



#%% son
