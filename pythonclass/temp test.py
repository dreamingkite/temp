
#实现property装饰器

class Property:
    def __init__(self, get_fn=None,set_fn=None):
        print("property init")
        self.get_fn = get_fn
        self.set_fn = set_fn

    def __get__(self, instance, owner):
        # print("Property,get method")
        return self.get_fn(instance)

    def __set__(self, instance, value):
        print("property.set")
        self.set_fn(instance,value)

    def setter(self,fn):
        self.set_fn = fn
        return self


class MyClass:
    def __init__(self,x,y):
        self.__x = x
        self.__y = y

    @Property
    def x(self):    # x = Property(x)
        return self.__x
#现在已经名为x的Property类对象了，就需要在类对象中添加setter方法
    @x.setter
    def x(self,value):  #x = x.setter(x) return self
        self.__x = value


a = MyClass(1,2)
print(a.x)
a.x = 5
print(a.__dict__)
print(a.x)


class TestClass:
    def __init__(self,x):
        self.__x = x

    def get_x(self):
        return self.__x

    def set_x(self,value):
        self.__x = value

    def show_x(self):
        return self.__x

    def wrapper_show_x(self):
        return self.show_x()

    x = Property(get_fn=get_x, set_fn=set_x)

b = TestClass(10)
print(b.x)
b.x = "abcd"
print(b.x)
print(b.__dict__)
print(b.wrapper_show_x())