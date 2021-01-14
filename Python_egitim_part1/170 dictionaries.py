# -*- coding: utf-8 -*-

"""
dictionaries
"""

# spyonde:ignore-cell
# the line above means that, this cell will not be in the .ipynb file.

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



#%% Dictionary

#- key-value (anahtar-değer) şeklinde çalışan bir veri yapısıdır.
#- her anahtar tekildir, tekrar etmez.
#- sequence tip değildir.
#- sequence: ranged by numbers
#- dictionaries: ranged by keys



#%% nasıl tanımlanır?

dict1 = {}
dict1["bir"] = "one"
dict1["iki"] = "two"
print(type(dict1))

dict1 = {"bir":"one", "iki":"two"}
print(dict1)
print(type(dict1))

dict1 = {"bir":"one", "iki":"two", "bir":"uno"}
# print(dict1)  # ne yazar?
print(type(dict1))



#%% dir() uygularsak:

dict1 = {"bir":"one", "iki":"two"}
print(dir(dict1))



#%% tekil elemanlarına erişim:

dict1 = {"bir":"one", "iki":"two"}
print(dict1["bir"])
print(dict1["iki"])



#%% tekil elemanlarına erişim (2)

dict1 = {"bir":"one", "iki":"two"}
print(dict1["uc"])



#%% in (membership) operatörü

# önceden kontrol etme imkanımız olsaydı ?

dict1 = {"bir":"one", "iki":"two"}

print(len(dict1))

if "bir" in dict1:
    print(dict1["bir"])

if "iki" in dict1:
    print(dict1["iki"])

if "uc" in dict1:
    print(dict1["uc"])
else:
    print("no such key")



#%% uygulama: şifre kontrolu

#- kullanıcının sifrelerinin olduğu bir `dict` olsun.
#- kullanıcıdan, kullanıcı adı ve şifre alalım.
#- login olabiliyorsa, login oldun diyelim.
#- degilse, olmadığını belirtelim.



#%% bir elemanı silmek

# iki method: `del()` ya da `pop()`

dict1 = {"bir":"one", "iki":"two", "dort":"four"}

del dict1["dort"]
value = dict1.pop("iki")

print(value)
print(dict1)

print(dir(dict1))



#%% bir anahtarın değerini değiştirmek

dict1 = {"bir":"one", "iki":"two", "dort":"four"}

dict1["bir"] = "un"
dict1["bir"] = "1"

print(dict1)



#%% anahtar, tekil (unique) olmalıdır.

#```python
#dict_name[key] = value
#```

# key olarak ne kullanılabilir?



#%% anahtar olarak string

dict1 = {}
dict1["one"] = 1

print(dict1)




#%% anahtar olarak sayılar, örneğin integer ya da float

dict1 = {}
dict1[1] = "one"

print(dict1)



#%% Uygulama: ingilizce-türkce sözlük örneği

#- aşağıdaki kelimeleri ekleyelim:
#- one, two
#- kullanıcıya, hangi kelimeyi aradığını soralım.
#- eğer sözlükte yoksa, sözlüğe ekleyelim.



#%% il dictionary örneği

iller = {}
iller["adana"] = ("01", "akdeniz")
iller["ordu"] = ("52", "karadeniz")
iller["samsun"] = ("55", "karadeniz")
iller["izmir"] = ("35", "ege")
iller["erzurum"] = ("25", "doğu anadolu")
iller["istanbul"] = ("34", "marmara")



#%% Uygulama: il dictionary örneği (2)

#- kullanıcıdan bir il bilgisi alalım.
#- değeri ekrana yazalım.
#- bilmediğimiz bir il ise, plaka kodu ve bölgesini soralım.
#- `iller` içine ekleyelim.



#%% ingilizce-türkce sözlük örneği

#- ingilizce `free` kelimesinin, Türkçe'de 2 anlamı var.
#- ikisini de tutmak istiyoruz.
#- nasıl bir çözüm getirebiliriz?



#%% anahtar olarak tuple

tuple1 = ("fransizca", 1)

dict1 = {}
dict1[tuple1] = "one"

print(dict1)



#%% değeri geri almaya çalışalım.

tuple1 = ("fransizca", 1)

dict1 = {}
dict1[tuple1] = "one"

tuple2 = ("fransizca", 1)

print(dict1[tuple2])



#%% list kullanırsak

list1 = ("fransizca", 1)

dict1 = {}
dict1[list1] = "one"

list2 = ["fransizca", 1]

print(dict1[list2])


#Traceback (most recent call last):
#  File "C:\projects\file1.py", line 8, in <module>
#    print(dict1[list2])
#TypeError: unhashable type: 'list'



#%% dictionary ile yemek listesi

yemek_listesi = {}
yemek_listesi["pazartesi"] = ("pide", "ayran", "cacik")
yemek_listesi["sali"] = ("lahmacun", "cola", None)
yemek_listesi["carsamba"] = ("t-bone", "srp", None)
yemek_listesi["persembe"] = ("midye", "br", None)
yemek_listesi["cuma"] = ("hamburger", "soda", "ayran")
# print(yemek_listesi)
for gun in yemek_listesi:  # sadece key
    print(gun)
    print(yemek_listesi[gun])

for x in yemek_listesi.items():
    # ('cuma', ('hamburger', 'soda'))
    pass

for gun, menu in yemek_listesi.items():
    print(gun)
    # print("\t", menu)
    yiyecek, icecek, yan_yemek = menu
    print("\t\t", icecek)



#%% son
