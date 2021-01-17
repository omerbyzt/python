"""
Fibonacci serisinde her sayı, kendisinden önce gelen iki sayının toplamıdır. 1 ve 2 ile başlayan serinin ilk 10 sayısı:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, …

Bu serinin dört milyondan küçük tüm çift sayılarının toplamını bulunuz.
#4613732
"""

num1 = 2
num2 = 1
new_bigger = 0
sum = 2
print(num2, end=" ")
print(num1, end=" ")
while sum < 4000000:
    new_bigger = num1 + num2
    num2 = num1
    num1 = new_bigger
    if (num1 % 2 == 0):
        sum += num1
        print(new_bigger, end=" ")
print()
print(sum, end=" ")
