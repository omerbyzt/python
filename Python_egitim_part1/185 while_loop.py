# -*- coding: utf-8 -*-

"""
while_loop
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



#%% while döngüsü

# - `for` ile beraber, Python'daki iki döngü tipinden biri.
# - bir şart sağlandığı sürece, belli işlemleri tekrar eder.



#%% while döngüsü

counter = 1
while counter < 9:
    print(counter)
    counter = counter + 1



#%% uygulama: while ile seri hesaplama

# - x = 1/2 + 2/3 + .... 10/11
# - x'in değeri nedir?



#%% Uygulama : while ile kısıtlı input

# İstenilen değerlerden biri girilene kadar devam ettirebiliriz.

cevap = " "
while cevap not in "/*-+":
    cevap = input("bir operator giriniz: /*-+ >>")
print(cevap, "girdiniz")



#%% Uygulama : negatif sayı girilene kadar ortalama

# - Kullanıcı, negatif bir sayı girene kadar kullanıcıdan değer alıp,
# - bittiğinde ortalamasını hesaplayan bir program.
#
# ```
# >>> 100
# >>> 80
# >>> 90
# >>> -1
# 270.0
# 90.0
# ```



#%% Çözüm 1 : negatif sayı girilene kadar ortalama

# - Kullanıcı, negatif bir sayı girene kadar kullanıcıdan değer alıp,
# - bittiğinde ortalamasını hesaplayan bir program.

done = False
count = 0
total = 0.0
while not done:
    current = int(input(">>>"))
    if current < 0:
        done = True
    else:
        count = count + 1
        total = total + current

print(total)
print(count)
print(total / count)



#%% break ve continue deyimleri

# - `break` : tüm iterasyonları sonlandırır.
# - `continue` : bir sonraki iterasyona geçer.



#%% Çözüm 2 : negatif sayı girilene kadar ortalama

# - Kullanıcı, negatif bir sayı girene kadar kullanıcıdan değer alıp,
# - bittiğinde ortalamasını hesaplayan bir program.

total = 0.0
count = 0

while True:
    number = float(input("sayi giriniz >>>"))
    if number < 0:
        break

    total = total + number
    count = count + 1

result = total / count
print("{} tane ortalama {}".format(count, result))



#%% Sonsuz döngüye dikkat

# ```python
# counter = 1
# while counter < 9:
#     print(counter)
# ```



#%% Uygulama: en fazla n şifre denemesi
# - kullanıcımız, doğru sifreyi girerse, program sifreyi kabul etsin.
# - şifreyi yanlış girerse, şifreyi en fazla 3 kere deneyebilsin.
# - 3 kere yanlış girerse, tekrar deneyemesin.



#%% Uygulama: sayı tahmin
# - bilgisayar, bir sayı tutsun.
# - kullanıcı, bu sayiyi tahmin etmeye çalışsın.
# - bilgisayar, kullanıcımıza, her tahminde, "çık" ya da "in" desin.
# - gizli sayı için, `random` kullanılabilir.
# ```
# import random
# gizli_sayi = random.randint(1, 20)
# ```



#%% son
