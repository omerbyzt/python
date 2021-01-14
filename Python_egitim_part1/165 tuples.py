# -*- coding: utf-8 -*-

"""
tuples.py
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



#%% Tuple veri tipi

#- telaffuz
#- https://english.stackexchange.com/questions/12980/how-to-pronounce-tuple
#- listeden farklı olarak, `[` ve `)` yerine `(` ve `)` ile tanımlanırlar.
#- listeden farklı olarak, immutable
#- bir index'deki değerini değiştirmeyi deneyelim
#- `dir()` ile methodlarına bakalım.


#%% örnek bir tuple

players = ("marco van basten", "roberto baggio", "ruud gullit", "ivan zamorano")
print(type(players))
print(len(players))



#%% kişisel bilgiler için bir tuple

kisisel_bilgiler = ("marco", "van basten", 12349, "Netherlands")



#%% birkaç futbolcuyu tanımlayan bir tuple

players = ("marco van basten", "roberto baggio", "ruud gullit", "ivan zamorano")
print(players)
print(len)
print(players[0])
print(players[2])




#%% aşağıdaki kodun çıktısı ne olur?


players = ("marco van basten", "roberto baggio", "ruud gullit", "ivan zamorano")
print(players[0])
print(players[2])
players[2] = "eric cantona"
print(players)




#%% "slicing" kullanılabilir

players = ("marco van basten", "roberto baggio", "ruud gullit", "ivan zamorano")
print(players[0:2])




#%% çıktısı ne olur?

players = ("marco van basten", "roberto baggio", "ruud gullit", "ivan zamorano")
players.append("Ryan Giggs")

# içine dir() ile bakalım.



#%% dir() ile üyelerine bakalım.

players = ("marco van basten", "roberto baggio", "ruud gullit", "ivan zamorano")
print(dir(players))
print()
print(dir([]))



#%% dir() ile üyelerine bakalım. (2)

#- bir list tipine göre daha en az eleman görüyor olmalıyız.
#- immutable ne demek?
#- `append()` yok.
#- `remove()` yok.
#- `insert()` yok.



#%% Uygulama : ruud gullit'i nasıl silebilirim?

players = ("marco van basten", "roberto baggio", "ruud gullit", "ivan zamorano")

# istenen çıktı:
# ('marco van basten', 'roberto baggio', 'ivan zamorano')



#%% tek elemanlı tuple yaratmak

# a değişkeninin tipi ne olur?

a = (4)
print(type(a))




#%% tek elemanlı tuple yaratmak, çözüm

b = (4,)
print(type(b))



#%% list ve tuple

#- `list` mutable, `tuple` immutable
#- `list` boyutu dinamik, `tuple` boyutu sabit
#- `tuple` icinde, `append()`, `remove()`, `pop()` gibi methodlar yok.
#- Kültürel : `list` içindeki elemanların, aynı tipten olması tercih edilir.
#- Kültürel : `tuple` içindeki elemanlar, farklı tipten olabilir (C'deki struct gibi)
#- `list()` fonksiyonu ile, tuple tipinden bir nesne, bir listeye döndürülebilir.
#- `tuple()` fonksiyonu da tersini yapar.



#%% son
