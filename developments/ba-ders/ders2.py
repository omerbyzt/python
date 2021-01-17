# stack, LIFO
# queue, FIFo

# rabbitmq

harfler = ["a", "b", "c"]
# list

harfler.append("d")
last = harfler.pop()

print(harfler)

harfler2 = [] # boş liste
harfler2.append("d")
harfler2.append("e")
harfler2.append("f")

last = harfler2.pop()
print(last)
last = harfler2.pop()
print(last)
last = harfler2.pop()
print(last)

harfler.insert(1, "x")
print(harfler)

import collections
collections.deque