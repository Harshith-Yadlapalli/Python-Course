""" Math Module"""
# import math
# print(math.sqrt(25))
# print(math.factorial(5))
# print(math.pi)
# print(math.floor(4.8))
# print(math.ceil(3.4))
# print(math.sin(90))

""" Random module"""
# import random
# print(random.random())

# print(random.randrange(1,10))

# rakhis = ["designed rakhi","gold_rakhi","diamond_rakhi","homemade_rakhi"]
# print(random.choice(rakhis))

# numbers = [10,20,30,40,50]
# print(random.sample(numbers,3))

# random.shuffle(numbers)
# print(numbers)

# n=[10,32,14,54,10,42]
# m=["der", "fes", "br","ted"]
# print(random.random()) # 0.76843
# print(random.randint(2,9)) # 2
# print(random.choice(n)) # 10
# print(random.choices(n,k=3)) # [10,10,14]
# print(random.sample(n,k=4)) # [10,54,42,14]
# print(random.shuffle(m)) # None
# print(m) # ['ted','der', 'br','fes']

""" Sys Module"""

# import sys
# print(sys.version)
# print(sys.platform)
#print(sys.orgv)

""" Platform Module"""
# print(platform.system()) # Windows
# print(platform.release()) # 11
# print(platform.machine()) # AMD64
# print(platform.processor()) # AMD64 Family 25 Model 80 Stepping 0, AuthenticAMD
# print(platform.python_version()) # 3.13.15

""" Collection Module"""
# from collections import Counter
# n="nayan sharma"
# h=Counter(n)
# print(h) # Counter({'e':2, 's':1, 'r': 1, 'y':1,'a':1, 'h':1})
# nums=[1,3,2,4,5,2,5,2]
# m=Counter(nums)
# print(m) #Counter({2: 3, 5: 2, 1: 1, 3: 1, 4: 1})

# from collections import counter
# n="nayan"
# h = Counter(n)
# print(h)

# from collections import defaultdict
# d = defaultdict(int)
# d["apple"]=1
# print("name")
# dic={'a':2,'b':3,'c':7}
# print(dic['a'])

# from collections import deque
# d = deque([1,2,3])
# d.append(4)
# d.appendleft(10)
# d.pop()
# d.popleft()
# print(d)

""" Intertools"""
# #Itertools
# from itertools import combinations
# numbers1 = [1,2,3,4]
# print(list(combinations(numbers1,3)))

# from itertools import product
# a = [1,2,4]
# b=['A','B','C']
# print(list(product(numbers,3)))

""" Datetime"""
from datetime import datetime
now = datetime.now()
print(now)
print()
print(now.year)
print(now.month)
print(now.day)
print()
print(now.hour)
print(now.minute)
print(now.second)

from datetime import datetime
today = date.today()
print(today)
now = datetime.now()
print(now.strftime("%H:%M:%S"))
print(now.strftime("%:%:%"))
print(now.strftime("%H:%M:%S"))

from datetime import date, timedelta
t =date.today()
f= t+timedelta(days=45)
print(f)