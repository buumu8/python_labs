import random
import sys
from utility import multiply, divide
from shopping.more_shopping import shopping_cart

if __name__ == "__main__":
    print(shopping_cart.buy("apple"))
    print(divide(4, 2))
    print(multiply(4, 3))
    print("Hello")
    print(random.random())
    print(random.choice([1, 2, 3, 4, 5]))
    print(random.randint(1, 100))
    my_list = [1, 2, 3]
    random.shuffle(my_list)
    print(my_list)
    print(sys.argv)
