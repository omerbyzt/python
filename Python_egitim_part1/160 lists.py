# -*- coding: utf-8 -*-

"""
lists.py
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



#%% List

#- Virgül ile ayrılmış değerleri tutar.
#- bir sequence tiptir.
#- https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range



#%% List vs Array
#- list != array
#- array != NumPy np.array
#- https://docs.python.org/3/library/array.html
#- Arrays are sequence types and behave very much like lists
#- the type of objects stored in them is constrained.



#%% Liste tanımı

some_numbers = [1, 3, 7]
print(some_numbers)



#%% listelerde, her bir değer farklı tipte olabilir:

some_numbers_and_names = [1, 3, "spam", "eggs"]
print(some_numbers_and_names)



#%% dilimleme (slicing)

some_numbers_and_names = [1, 3, "spam", "eggs"]
only_numbers = some_numbers_and_names[:2]
print(only_numbers)



#%% Uygulama : Sadece alfabe içerenleri almak istersek, nasıl dilimleriz?

some_numbers_and_names = [1, 3, "spam", "eggs"]
only_numbers = some_numbers_and_names[:2]
print(only_numbers)



#%% Listeler değiştirilebilir özelliğe sahiptir (mutable)

# aşağıdaki kodun sonucu ne olur?

some_numbers_and_names = [1, 3, "spam", "eggs"]
some_numbers_and_names[1] = 5
print(some_numbers_and_names)

# string tiplerde nasıldı?



#%% aşağıdaki kodun sonucu ne olur?

some_numbers_and_names = [1, 3, "spam", "eggs"]

some_numbers_and_names[1] = [4, 5]
print(some_numbers_and_names)
print(len(some_numbers_and_names))



#%% Liste elemanlarını değiştirmek

#- nested (yuvalanmış) olmasını istemezsek...
#- istenmeyen : `[1, [4, 5], 'spam', 'eggs']`
#- istenilen : `[1, 4, 5, 'spam', 'eggs']`

some_numbers_and_names = [1, 3, "spam", "eggs"]

some_numbers_and_names[1:2] = [4, 5]
print(some_numbers_and_names)
print(len(some_numbers_and_names))



#%% Liste elemanlarını nasıl silebiliriz?

# aşağıdaki örnekte,`spam` ve `eggs` değerlerini silmek istersek, nasıl bir yol izleyebiliriz?

some_numbers_and_names = [1, 3, "spam", "eggs", 4, 5]

print(some_numbers_and_names)
print(len(some_numbers_and_names))



#%% çözüm : spam ve eggs elemanlarını silmek için

some_numbers_and_names = [1, 3, "spam", "eggs", 4, 5]
print(some_numbers_and_names)
print(len(some_numbers_and_names))

some_numbers_and_names[2:4] = []  # bos liste tanimi

print(some_numbers_and_names)
print(len(some_numbers_and_names))



#%% bir Listeye, `dir()` methodunu uygularsak?

some_numbers_and_names = [1, 3, "spam", "eggs", 4, 5]
print(dir(some_numbers_and_names))



#%% + kullanarak eklemek

# aşağıdaki şekilde ekleyebilir miyiz?

some_numbers_and_names = [1, 3, "spam", "eggs", 4, 5]
print(some_numbers_and_names)
some_numbers_and_names = some_numbers_and_names + 6



#%% + ile ekleyecegimiz eleman, yine bir liste olmalı.

some_numbers_and_names = [1, 3, "spam", "eggs", 4, 5]
print(some_numbers_and_names)

some_numbers_and_names = some_numbers_and_names + [6]

print(some_numbers_and_names)



#%% Sequence Operations
#- Common:
#- https://docs.python.org/3/library/stdtypes.html#common-sequence-operations
#- Mutable:
#- https://docs.python.org/3/library/stdtypes.html#mutable-sequence-types



#%% append() kullanımı

# listenin sonuna eklemek icin.

some_numbers_and_names = [1, 3, "spam", "eggs", 4, 5]
print(some_numbers_and_names)

some_numbers_and_names.append(6)
print(some_numbers_and_names)



#%% List için bazı diğer methodlar.

#- `insert()`
#- `clear()`
#- `count()`
#- `remove()`
#- `pop()`



#%% insert()

list1 = ["a", "b", "d", "e"]
list1.insert(2, "c")

print(list1)



#%% clear()

list1 = ["a", "b", "d", "e"]
list1.clear()

print(list1)




#%% count()

list1 = ["a", "b", "c", "c", "d", "e"]

print(list1.count("a"))
print(list1.count("c"))
print(list1.count("invalid"))




#%% remove()

list1 = ["a", "b", "c", "c", "d", "e"]

list1.remove("a")
print(list1)

list1.remove("c")
print(list1)



#%% pop()

list1 = ["a", "b", "c", "c", "d", "e"]

item = list1.pop(1)
print(item)
print(list1)



#%% index()
list1 = ["a", "b", "c", "c", "d", "e"]

found_at = list1.index("c")
print(found_at)

# ValueError:
# found_at = list1.index("x")
# print(found_at)



#%% `list` içinde `list`
# - bir kişiyi simgeleyecek bir `list` yapalım.
# - ilk elemanı: adı
# - sonraki elemanı: soyadı
# - sonraki elemanı: mesleği (meslekleri?)
# - birden fazla kişiyi tutmak için de ayrı bir `list` yapalım.



#%% bir listeyi sıralamak
#- "sorted" vs "ordered"
#- "ordered", "koydugumuz sırada" anlamına gelir.



#%% sorted() fonksiyonu

some_numbers = [2, 4, 5, 3]
some_numbers2 = sorted(some_numbers)
print(some_numbers)
print(some_numbers2)



#%% sorted() fonksiyonu, ters sıralamak
some_numbers = [2, 4, 5, 3]
some_numbers2 = sorted(some_numbers, reverse=True)
print(some_numbers)
print(some_numbers2)



#%% aşağıdaki kod çalışınca ne olur?

some_numbers_and_names = [1, 3, "spam", "eggs", 4, 5]
print(sorted(some_numbers_and_names))

#```
#Traceback (most recent call last):
#  File "C:\projects\file1.py, line 2, in <module>
#    print(sorted(some_numbers_and_names))
#TypeError: '<' not supported between instances of
#    'str' and 'int'
#```


#%% dir() bize bir list döndürür.

result = dir(4)
print(type(result))
print(result)



#%% list yardım dokumanını okumak

print(help(list))



#%% Using Lists as Stacks

# The list methods make it very easy to use a list as a stack, where the last element added is the first element retrieved (“last-in, first-out”).
# To add an item to the top of the stack, use append().
# To retrieve an item from the top of the stack, use pop() without an explicit index.

stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print(stack)
stack.pop()
print(stack)
stack.pop()
print(stack)
stack.pop()
print(stack)



#%% Uygulama: Futbol ligi örneği

#- ispanya ligi yaratalım.
#- birkaç takım ekleyelim.
#- kaç takım ekledik?
#- belli bir takımı küme düşürelim.
#- son takımı küme düşürelim.
#- düşürme işlerini yaparken, takım listede mi, kontrol edelim.
#- italya ligi yaratalım.
#- iki ligin en üst iki takımından yeni bir lig yaratalım.



#%% list eşitliği

list1 = ["a", "b", "c"]
list2 = list1
list1.append("d")
print(list1)
print(list2)



#%% builtin id() fonksiyonu

# bir nesnenin, hafızadaki adresini verir.

x = 5
adres = id(x)



#%% is operator

# iki değişkenin hafıza adreslerini karşılaştırarak, aynı değişken olup olmadığını tespit eder.



#%% liste eşitliği - çıktısı ne olur?

list1 = [1, 2, 3]
print(id(list1))

list2 = list1
print(id(list2))

list2.append(4)

print(list1)
print(list2)

list3 = [1, 2, 3, 4]
print(list1 is list2)

if list1 == list2:
    print("list1 == list2")
else:
    print("list1 != list2")

if list1 == list3:
    print("list1 == list3")
else:
    print("list1 != list3")



#%% Python Tutorial - Lists
#- https://docs.python.org/3/tutorial/introduction.html#lists
