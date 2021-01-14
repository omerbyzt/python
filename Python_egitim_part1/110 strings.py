# -*- coding: utf-8 -*-

"""
strings
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



#%% String Tipi
#- sequence tip olarak geçer.
#- https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str



#%% String Tipi

# Metin (alfanumerik) bilgilerini tutmak için kullanılır.
# tek tırnak ' veya çift tırnak " kullanılabilir.

sehir = "Ankara"
dosya_adi = "veriler.xlsx"
isim = "Sebastian Vettel"

# type inference:
tcno1 = "1501111"
tcno2 = 1501112
print(type(tcno1))
print(type(tcno2))



#%% String tanımlarken, tırnak kullanımı

takim1 = "Scuderia Ferrari"
takim2 = 'Mercedes AMG F1'
print(type(takim1))
print(type(takim2))



#%% String tanımlarken, tırnak kullanımı

#- Tırnak işaretleri, duruma göre diğeri kullanılarak, faydalanılabilir.
#- Örneğin, bu metini yazmak istersek:

#```
#Scuderia Ferrari'nin pilotu Sebastian Vettel
#```



#%% Sorunlu bir string tanımlama

#```python
#pilot = 'Scuderia Ferrari'nin pilotu Sebastian Vettel'
#print(type(pilot))
#print(pilot)
#```



#%% Sorunlu bir string tanımlama (doğrusu)

pilot = "Scuderia Ferrari'nin pilotu Sebastian Vettel"
print(type(pilot))
print(pilot)



#%% Escape karakteri kullanımı

pilot = 'Scuderia Ferrari\'nin pilotu Sebastian Vettel'
print(pilot)



#%% Bazı Escape karakterleri

#```
#\\	Backslash (\)
#\'	Single quote (')
#\"	Double quote (")
#\n	ASCII Linefeed (LF)
#\r	ASCII Carriage Return (CR)
#\t	ASCII Horizontal Tab (TAB)
#```



#%% Dosya isimi tanımlarken

#```python
#dosya1 = "C:\path\to\my\file.txt"
#print(dosya1)
#
#dosya2 = "C:\\path\\to\\my\\file.txt"
#print(dosya2)
#```



#%% raw (ham) string

#```python
#dosya3 = r"C:\path\to\my\file.txt"
#print(dosya3)
#```



#%% Dosya isimi tanımlarken
dosya4 = "C:/path/to/my/file.txt"



#%% Multiline Strings

#- Kullanım alanları:
#- Yardım metinleri
#- Yorumlar
#- Yazılımın kullanacağı varsayılan dosyaların orjinal halleri
#- Ekranda kullanıcıya gösterilecek uzun metinler



#%% Multiline Strings
some_peps = r"""
PEP "257" -- Docstring Conventions https://www.python.org/dev/peps/pep-0257/
PEP "3105" -- Make print a function https://www.python.org/dev/peps/pep-3105/
PEP "3333" -- Python Web Server Gateway Interface v1.0.1 https://www.python.org/dev/peps/pep-3333/
"""
print(some_peps)



#%% multiline string, nasıl görünür?

# ekranda gercekten asagidaki sekilde gorunsun istiyoruz diyelim?

members = r"""
\\	Backslash (\)
\'	Single quote (')
\"	Double quote (")
\n	ASCII Linefeed (LF)
\r	ASCII Carriage Return (CR)
\t	ASCII Horizontal Tab (TAB)
"""
print(members)

# çıktıyı yorumlayalım.
# bunu düzeltmenin bir yolu olmalı.



#%% başına r koyarsak?

members = r"""
\\	Backslash (\)
\'	Single quote (')
\"	Double quote (")
\n	ASCII Linefeed (LF)
\r	ASCII Carriage Return (CR)
\t	ASCII Horizontal Tab (TAB)
"""
print(members)



#%% index ile erişim

#- Bir string değişkenin, istenen bir elemanına erişim sağlar.
#- C dilindeki karakter dizileri ile aynı mantıkta çalışır.
#- Python'da string değişkenlerde, index, 0 (sıfır) ile başlar.



#%% index ile erişim

#           1
# 0123456789012345
# Sebastian Vettel


pilot = "Sebastian Vettel"
print(len(pilot))  # 16

print(pilot[0])
print(pilot[1])
print(pilot[14])
print(pilot[15])
# print(pilot[16])  # IndexError: string index out of range



#%% Bir string'in son karakterini nasıl alırız?

#        012345
pilot = "Vettel"
print(pilot[5])



#%% Bir string'in son karakterini almak

pilot = "Vettel"
length = len(pilot)
print(pilot[length-1])

# daha iyi bir yolu olabilir mi?



#%% Reverse Index

#- String'in sonundan, -1 ile başlar.

#           1
# 0123456789012345
# Sebastian Vettel
# 6543210987654321
#       1


pilot = "Sebastian Vettel"
print(pilot[-1])
print(pilot[-2])
print(pilot[-3])
print(pilot[-12])

# neden -1, neden -0 değil ?



#%% neden -1, neden -0 değil ? (ispat)

pilot = "Sebastian Vettel"
print(pilot[-0])
print(pilot[0])



#%% Eğer bir string'in ilk 5 harfini almak istersem?

# hatırlatma: string concentation(arka arkada ekleme) operator : +

pilot = "Sebastian Vettel"
first_five_chars = pilot[0] + pilot[1] + pilot[2] + pilot[3] + pilot[4]
print(first_five_chars)

# daha iyi bir yolu olabilir mi?



#%% Slicing (Dilimleme)

## hatırlatma:

# ```
#           1
# 0123456789012345
# Sebastian Vettel
# 6543210987654321
#       1
# ```




#%% dilimleme için aralık verebiliriz:

pilot = "Sebastian Vettel"
print(pilot[1:6])

# `-1` dahil, `6` dahil değil



#%% dilimleme örnekleri

pilot = "Sebastian Vettel"

print(pilot[0:5])

print(pilot[1:6])

print(pilot[2:7])



#%% string'in başından başlıyorsa, 0 değerini belirtmemize gerek yok.

# okunuşuna dikkat edelim.

pilot = "Sebastian Vettel"
print(pilot[0:5])
print(pilot[:5])



#%% string'in sonuna kadar gidiyorsa, son değerini belirtmemize gerek yok.

# okunuşuna dikkat edelim.
# aşağıdaki iki satır, birbirine denktir.

pilot = "Sebastian Vettel"
print(pilot[5:])
print(pilot[5])



#%% başından, -4'üncü karaktere kadar:

pilot = "Sebastian Vettel"
print(pilot[:-4])



#%% -6 ve -4'üncü karakterler arası:

pilot = "Sebastian Vettel"
print(pilot[-6:-4])



#%% String bir sequence tiptir.
#- Dolayısıyla, "common sequence operations" destekler:
#- https://docs.python.org/3/library/stdtypes.html#typesseq-common



#%% yeni bir string oluşturmak

## hatırlatma:

# ```
#           1
# 0123456789012345
# Sebastian Vettel
# 6543210987654321
#       1
# ```



#%% bir string değişkenin bir parçasını değiştirmeye çalışırsak:

# ```python
# pilot = "Sebastian Vettel"
# pilot[0] = '5'
# ```



#%% strings are immutable

#- string'ler, immutable durumdadır, yani değiştirilemez.
#- yeniden oluşturmak gerekir.
#- Class ve Dictionary bölümünde, sebebini göreceğiz.



#%% bir string değişkenin bir parçasını değiştirmeye çalışırsak:

# değiştirmenin bir yolu:

pilot = "Sebastian Vettel"
pilot = "5" + pilot[1:]
print(pilot)



#%% Gördüğümüz Python built-in fonksiyonları

#```python
#print()
#len()
#type()
#```
#
## yeni:
#
#```python
#dir()
#```



#%% dir() fonksiyonunu string tipine uygulayalım:

pilot = "Sebastian Vettel"
print(dir(pilot))



#%% string methods
#- https://docs.python.org/3/library/stdtypes.html#string-methods
#- döküman nasıl okunur?
#- https://docs.python.org/3/library/stdtypes.html#str.center
#- `str.center(width[, fillchar])`



#%% Bir string değişkeni için, birkaç tanesini kullanalım:

# ```python
# str.capitalize()
# str.center(width[, fillchar])
# str.count(sub[, start[, end]])
# str.endswith(suffix[, start[, end]])
# str.find(sub[, start[, end]])  # -1
# str.index(sub[, start[, end]])  # ValueError
# str.is...
# str.join(iterable)
# str.ljust(width[, fillchar])
# str.lower()
# str.lstrip([chars])
# str.replace(old, new[, count])
# str.rfind(sub[, start[, end]])
# str.rindex(sub[, start[, end]])
# str.rjust(width[, fillchar])
# str.rsplit(sep=None, maxsplit=-1)
# str.rstrip([chars])
# str.split(sep=None, maxsplit=-1)
# str.splitlines([keepends])
# str.startswith(prefix[, start[, end]])
# str.strip([chars])
# str.upper()
# ```



#%% is.. ile başlayan fonksiyonlar/methodlar

# - genellikle True/False döndürürler.
# - https://docs.python.org/3/library/stdtypes.html#str.isalnum



#%% "abc" için:

value1 = "abc"
print(value1.isalnum())  # True
print(value1.isalpha())  # True
print(value1.isdecimal())  # False
print(value1.isdigit())  # False
print(value1.isnumeric())  # False



#%% "123" için:

value1 = "123"
print(value1.isalnum())  # True
print(value1.isalpha())  # False
print(value1.isdecimal())  # True
print(value1.isdigit())  # True
print(value1.isnumeric())  # True



#%% "123.4" için:

value1 = "123.4"
print(value1.isalnum())  # False
print(value1.isalpha())  # False
print(value1.isdecimal())  # False
print(value1.isdigit())  # False
print(value1.isnumeric())  # False



#%% multiline strings, strip() beraber kullanımı

data1 = """
a
b
c
d
"""
lines = data1.strip().splitlines()
print(lines)



#%% `print()` fonksiyonu (1)
#- sadece `print()` yazarsak, `\n` yazar, yani yeni satıra geçer.
#- https://realpython.com/python-print/



#%% `print()` fonksiyonu (2)
answer = 42
print(answer)
# print("herseyin cevabi: " + answer)
# Traceback (most recent call last):
#   File "C:\...........py", line 2, in <module>
#     print("herseyin cevabi: " + answer)
# TypeError: can only concatenate str (not "int") to str
print("herseyin cevabi:", answer)
print("herseyin cevabi:", answer, sep="_")

print("1", end="")
print("2", end="")
print("3", end="")
# 123



#%% `printf`-style String Formatting
#- https://docs.python.org/3/library/stdtypes.html#printf-style-string-formatting

print("bu yıl, yüzde %(buyume)3d büyüme hedefliyoruz." % {"buyume":23})


#%% string.format
#- https://docs.python.org/3/library/stdtypes.html#printf-style-string-formatting

print("bu yıl, yüzde {} büyüme hedefliyoruz.".format(23))
print("Zamorano {0}, Ronaldo {1} numaralı formaları giydiler".format("1+8", 9))
print("Zamorano {1}, Ronaldo {0} numaralı formaları giydiler".format(9, "1+8"))



#%% f-strings (1)

#- Formatted string literals.
#- Python 3.6 ile geldi.
#- https://docs.python.org/3/tutorial/inputoutput.html#formatted-string-literals
#- https://docs.python.org/3/reference/lexical_analysis.html#f-strings
#- https://realpython.com/python-f-strings/



#%% f-strings (2)
number1 = 5
number2 = 6
total = number1 + number2

print(str(number1) + "+" +  str(number2) + "=" + str(total))
# 5+6=11
print(f"{number1}+{number2}={total}")
# 5+6=11



#%% `input()` fonksiyonu ile Kullanıcıdan değer almak

#- Python 3.x için, `input()` isimli function kullanılır.
#- Python 2.x için, `raw_input()` isimli function kullanılır.
#- Bu fonksiyon, kullanıcının girdiği değeri döndürür.



#%% Kullanıcıdan değer almak (2)

deger = input("adinizi giriniz: ")
print(deger)



#%% Uygulama: Kullanıcının adını alıp, "merhaba" şeklinde selamlayan bir program

#- örneğin `Ahmet` girip enter tuşuna bastıysa,
#- programımız, ekranda `merhaba Ahmet` yazısını göstersin.



#%% Uygulama: Kullanıcıdan iki ayrı sayı alıp, toplamlarını yazan bir program




#%% Sıradaki kodu, önce alfanumerik, sonra da sayısal bir değer ile deneyelim:

x1 = input(">>")
print(x1)
print(type(x1))



#%% Gördüğümüz Python built-in fonksiyonları

#```python
#print()
#len()
#type()
#dir()
#```
#
## yeni:
#
#```python
#int()
#float()
#```



#%% int() fonksiyonu

x1 = input("int icin bir sayi giriniz >>")
i1 = int(x1)  # int() kullanimi
print(i1)
print(type(i1))



#%% float() fonksiyonu

x1 = input("float icin bir sayi giriniz >>")
f1 = float(x1)  # float() kullanimi
print(f1)
print(type(f1))



#%% Uygulama: Kullanıcıdan iki ayrı sayı alıp, toplamlarını yazan bir program



#%% Python Tutorial - Strings
#- https://docs.python.org/3/tutorial/introduction.html#strings



#%% son
