import random

def Randomizer(list1):
    for i in range(10):
        list1.append(random.randint(0,10))
    return list1

x = []

print(Randomizer(x))