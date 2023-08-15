import os

class Limit(object):
    def __init__(self, value):
        self.limit = value

    def get_limit(self):
        # print(f"The limitation is now set as {self.limit}")
        return self.limit
    
    def change_limit(self, value):
        print(f"Limit is updated from {self.limit} to {value}")
        self.limit = value

class ExceedLimitException(Exception):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Product {self.name} not created successfully. Exceed maximum: max {LIMIT.get_limit()} product"


class Product(object):
    __count = 0
    def __new__(cls, name):
        if cls.__count>=LIMIT.get_limit():
            raise ExceedLimitException(name)
        cls.__count+=1
        return super(Product,cls).__new__(cls)

    def __init__(self, name):
        self.name = name
        print(f"product {name} created")
        pass

    def __del__(self):
        print(f"product {self.name} deleted")
        # return f"product {self.name} deleted"




if __name__ == '__main__':
    LIMIT = Limit(2)
    LIMIT.get_limit()
    LIMIT.change_limit(3)
    LIMIT.get_limit()

    # p1 = Product("car")
    # p2 = Product("Table")
    # p3 = Product("Apple")
    # # p4 = Product("Appleaa")
    # print(p1.name)
    # print(p2.name)
    # del p1
    # p4 = Product("Bag")


    try:
        p1 = Product("car")
        p2 = Product("Table")
        p3 = Product("Apple")
        # p4 = Product("Appleaa")
        # print(p1.name)
        # print(p2.name)
        del p1
        p4 = Product("Bag")
    except Exception as e:
        print(e)

    os._exit(0)