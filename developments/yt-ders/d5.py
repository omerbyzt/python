is_palindrom = True
str = "omer"
str_reverse = str[::-1]
print(str_reverse)



"""
İki yönden de aynı şekilde okunan sayılara palindromik sayılar denir. 2 haneli 2 sayıdan oluşturulabilecek en büyük palindrom değeri 9009’dur. (91 x 99)

3 haneli iki sayıdan oluşturulabilecek en büyük palindromik sayıyı bulunuz.
#906609
"""

num1 = 0
num2 = 0

big_palindrom = 0
for i in range(100, 1000):
    for j in range(100, 1000):
        num = str(i * j)
        num_reverse = num[::-1]
        if(num == num_reverse and i*j > big_palindrom):
            num1 = i
            num2 = j
            big_palindrom = i*j

print(num1)
print(num2)
print(big_palindrom)