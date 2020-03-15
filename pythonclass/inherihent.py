class A:
    def __init__(self):
        pass


class B(A):
    def __init__(self):
        super().__init__()
        pass


class C(B):
    def __init__(self):
        super().__init__()
        pass

"""---------------------------------------------------------------------------------"""

class MyException(Exception):
    pass


# try:
#     b = "bb"
#     a = 1/0
# except Exception:
#     print("Exception has occudr")
# finally:
#     print("finanlly")
#     print(a)

# print(dir())


for x in range(5):
    print(x)
else:
    print("ok")

import math
