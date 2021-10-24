import random


#random int
print(random.randint(1, 10))

#random range
print(random.randrange(10, 50))

#random float
print(random.uniform(1, 10))

#random float 0~1
print(random.random())

#random string
print(random.choice('asd4354.wq!#$#$&^$%'))

#random from list
listA = [1, 7, 9, 16]
print(random.sample(listA, 1))