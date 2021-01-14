# -*- coding: utf-8 -*-

"""
data_types_and_variables
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



#%% Veri Tipleri ve Değişkenler

#- numerics
#  - int
#    - boolean
#  - float
#  - complex
#- sequences
#  - list, tuple, range
#- mappings
#- classes, instances
#- exceptions
#- https://docs.python.org/3/library/stdtypes.html#built-in-types



#%% Numeric Types

#- int
#  - booleans (sub type of integers)
#- float
#- complex
#- https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex



#%% Değişken tanımı ve tipi

# Bir değişken, `=` operatörü ile tanımlanır.
# değer, sağdan sola geçer.

pi = 3.14
cevap = 42

x, y = 4, 5



#%% Type inference

#- Değişkenin, daha önceden bir yerde tanımlanması gerekmez.



#%% type() fonksiyonu

# built-in `type()` fonksiyonu, verilen bir değerin tipini döndürür.

n1 = "deneme"
print(type(n1))
print(type(9))
print(type(9.2))



#%% Sıradaki kod parçasını çalıştırırsak, ne görürüz?

n1 = 6
print(temp)



#%% Sayısal değişkenlerin boyutu

# - bunun çalıştığını biliyoruz:

n2 = 3.2
print(n2)
print(type(n2))

# bir de bunu deneyelim:

n1 = 309487593480750934876590348759847593845687934598345
print(n1)
print(type(n1))

n2 = 34 ** 74
print(n2)



#%% Sayısal değişkenlerin boyutu

# - "Integers have unlimited precision."
# - https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex



#%% float

n3 = 309487593480750934876590348759847593845687934598345.309487593480750934876590348759847593845687934598345
print(n3)
print(type(n3))



#%% float
#- Floating point numbers are usually implemented using double in C



#%% Complex Sayı Tipi

n4 = 3+5j
print(n4)
print(type(n4))



#%% Numeric Operations
#- All numeric types (except complex) support the following operations (for priorities of the operations
#- https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex



#%% Operator Precedence
#- https://docs.python.org/3/reference/expressions.html#operator-summary



#%% Bitwise Operations on Integer Types
#- https://docs.python.org/3/library/stdtypes.html#bitwise-operations-on-integer-types



#%% Sayısal Değişken Tipleri - özet

#- int
#  - bool
#- float
#- complex
#- https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex



#%% Operatörler

#- Arithmetic Operators (`+ - * / ** % //`)
#- Comparison (Relational) Operators (`==, !=, <, >, <=, >=`)
#- Assignment Operators (`= += -= *= /= %= **= //=`)
#- Logical Operators (`and or nor`)
#- Bitwise Operators (`& || ..`)
#- Membership Operators (`in , not in`)
#- Identity Operators (`is , is not`)



#%% Operator Precedence:
#- https://docs.python.org/3/reference/expressions.html#operator-precedence



#%% Aritmetik Operatörler

#- `+`  addition
#- `-`  subtraction
#- `*`  multiplication
#- `/`  division (true division)
#- `//` division (floor division)
#- `%`  modulus
#- `**` exponentiation



#%% addition, subtraction

print(2+3)
print(2+3.1)

print(4-2)
print(4-2.0)
print(2-3.1)



#%% hitpoint
hitpoint = 100
hitpoint = hitpoint - 20  # yüksekten düştük
hitpoint = hitpoint - 10  # yerdeki dikene bastık
hitpoint = hitpoint - 20  # yüksekten düştük



#%% Multiplication

print(2*3)
print(2*3.1)



#%% Division

print(4/2)  # true division
print(4/2.0)
print(4//2)  # floor division



#%% Division (2)

print(5/2)
print(5/2.0)
print(5//2)

print(7/2)
print(7//2)



#%% Division, negatif sayılar ile

print(5/2)
print(-5/2)
print(-5//2)

# -3 değerinden gördüğümüz üzere, "floor" işlemi uygulanıyor.
# bu işlem, floor division olarak da bilinir.



#%% round() fonksiyonu (1)

# - https://docs.python.org/3/library/functions.html#round
# - `round(number[, ndigits])`
# - Return number rounded to ndigits precision after the decimal point.
# - If ndigits is omitted or is None, it returns the nearest integer to its input.



#%% round() fonksiyonu (2)

print(int(2.1))
print(round(2.1))
print(int(2.5))
print(round(2.5))
print(int(2.8))
print(round(2.8))  # 3

pi_num = 3.14159265359
print(round(pi_num, 2))



#%% Modulus operator

# bölümünden kalanı verir.

print(5%2)
print(4%2)
print(2%2)
print(1%2)
print(0%2)
print(-1%2)
print(-2%2)



#%% + ve * operatörleri üzerine...

# operatörler, operandlarına göre farklı davranmaktadırlar.

print(4 + 5)
print("4" + "5")
print(4 * 5)
print("4" * "5")
print("mine " * 20)
print(20 * "mine ")



#%% boolean tip, True ve False
film_izlendi = True
veri_bulundu = False

kayit_edilecek = True
sorun_bulundu = False

maskesi_var_mi = True
otobuse_binebilir_mi = False



#%% boolean tip, True ve False
#- https://docs.python.org/3/library/stdtypes.html#boolean-values



#%% Truth table
#- and
#- or
#- not



#%% Truth table - and
print(False and False)
print(False and True)
print(True and False)
print(True and True)



#%% Truth table - or
print(False or False)
print(False or True)
print(True or False)
print(True or True)



#%% Truth table - not
print(not False)
print(not True)



#%% None değeri

secilmis_kisi = None
son_kayit = None
en_sevdigim_sayı = None

# `type()` ile deneyelim.



#%% None değeri
#- Python data, in Built-in Constants
#- represent the absence of a value
#- "adınızı giriniz" örneğini düşünelim.
#- "bir sayı giriniz" örneğini düşünelim.
#- https://docs.python.org/3/library/constants.html?highlight=none#None



#%% Referanslar, Detaylar

#- https://docs.python.org/3/library/stdtypes.html
#- https://docs.python.org/3/reference/datamodel.html#types
#- https://docs.python.org/3/library/constants.html
#- https://docs.python.org/3/library/datatypes.html



#%% Python Tutorial - Numbers
#- https://docs.python.org/3/tutorial/introduction.html#numbers



#%% Değişken isimleri
# - herhangi bir uzunlukta olabilir.
# - küçük harfler, büyük harfler, rakamlar ve underscore(_) içerebilir.
# - rakam ile başlayamaz.



#%% Naming Conventions (1)

# ```
# sn
# studentNumber (Camel case, camelCase, CamelCase)
# StudentNumber (Upper Camel Case, PascalCase)
# student_number (snake_case, Python'un tercihi)
# ```



#%% Naming Conventions (2)
#- https://www.python.org/dev/peps/pep-0008/#id34
#- https://en.wikipedia.org/wiki/Camel_case
#- https://en.wikipedia.org/wiki/Naming_convention_(programming)



#%% son
