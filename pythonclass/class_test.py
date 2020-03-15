
class Typed:
    def __init__(self,cls):
        self.cls = cls

    def __call__(self, *args, **kwargs):
        self.mark = "mark"
        return self.cls

@Typed
class MyClass:
    x = Typed(str)
    y = Typed(int)

    def __init__(self,x:str,y:int):
        self.x = x
        self.y = y

a = MyClass("abc",2)
print(a.__dict__)
print(MyClass.__dict__)


