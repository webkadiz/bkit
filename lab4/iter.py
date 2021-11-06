from inspect import signature

# @classmethod
class property():
    def __get__(self, obj, cls):
        print("getter used", self, obj)
        return self.gfunc(obj)

    def __set__(self, obj, val):
        print("setter used")
        self.sfunc(obj, val)

    def __delete__(self, obj):
        print("deleter used")

    def __init__(self, func):
        print(func)
        self.gfunc = func
    
    def setter(self, func):
        print(func)
        self.sfunc = func
        return self
    

def print_dec(func):
    print(func)
    def wrapper(obj):
        print(obj)
        print("before")
        res = func(obj)
        print("after")
        return res

    return wrapper


class A():
    def __init__(self, a, b):
        self._a = a
        self._b = b

    @property
    @print_dec
    def a(self):
        return self._a

    @a.setter
    def a(self, value):
        self._a = value
    

obj = A(1,2)
print(obj.a)
obj.a = 2
print(obj.a)