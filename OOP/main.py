from functools import reduce

class User():
    def __init__(self,email):
        self.email = email

    def sign_in(self):
        print('logged in')
    
class Wizard(User):
    def __init__(self,name,power,email):
        User.__init__(self,email)
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power of {self.power}')

class Archer(User):
    def __init__(self,name,num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'attacking with num_arrows of {self.num_arrows}')

class HybridBorg(Wizard, Archer):
    pass

wizard1 = Wizard('merlin',50,'merlin@gmail')
archer1 = Archer('Robin',100)
wizard1.attack()
archer1.attack()

print(list(filter(lambda item: item % 2 != 0, [1,2,3])))
print(reduce(lambda acc,item: acc+item,[1,2,3]))

my_list = [5,4,3]

print(list(map(lambda item: item*item,my_list)))

a = [(0,2),(4,3),(9,9),(10,-1)]
a.sort(key=lambda x: x[1])
print(a)

my_char = [char for char in 'hello']
my_list2 = [num for num in range(0,100)]
my_list3 = [num*2 for num in range(0,100)]
my_list4 = [num**2 for num in range(0,100) if num % 2 == 0]

print(my_list4)

my_set = {char for char in 'hello'}

simple_dict = {
    'a':1,
    'b':2
}
my_dict = {key:value**2 for key,value in simple_dict.items() if value % 2 == 0}
my_dict2 = {num:num*2 for num in [1,2,3]}

some_list = ['a','b','c','d','c','a']
duplicates = {num for num in some_list if some_list.count(num) > 1}
print(list(duplicates))

#Decorator
from time import time

def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'took {t2-t1} ms')
        return result
    return wrapper

@performance
def long_time():
    for i in range(10000):
        i*5


long_time()