class number:
    def __init__(self, n):
        self.n = n
    def __add__(self, num):
        return self.n + num.n
#operators in python can be overloaded using the following methods
# __add__(self, other) # +
# __sub__(self, other) # -
# __mul__(self, other) # *
# __truediv__(self, other) # /
# __floordiv__(self, other) # //
# __mod__(self, other) # %
# __pow__(self, other) # **
# __and__(self, other) # &
# __or__(self, other) # |
# __xor__(self, other) # ^
n = number(4)
m = number(5)
print(n + m)

