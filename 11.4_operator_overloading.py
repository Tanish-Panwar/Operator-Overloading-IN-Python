# Double Underscore method is also called dunder methods
# Operator Overloading Methods

# class Number:
#     def __init__(self, num):
#         self.num = num

#     def __add__(self, num2):
#         print("let's Add")
#         return self.num + num2.num

#     def __mul__(self, num2):
#         print("let's Multiply")
#         return self.num * num2.num

# Operators in python can be overloaded using dunder methods
# These methods are called when a given operator is used on the objects

# n1 = Number(6)
# n2 = Number(4)
# sum = n1 + n2
# mul = n1 * n2
# print(sum)
# print(mul)


# Operator's can be overloaded using the following methods
# n1 + n2 --> __add__()
# n1 * n2 --> __mul__()
# n1 / n2 --> __truediv__()
# n1 - n2 --> __sub__()
# n1 // n2 --> __floordiv__()


# other dunder magic methods in python


# __str__()--> used to set what gets displayed upon calling str(obj)
# __len__()--> used to set what gets displayed upon calling __len__() or len(obj)


class Number:
    def __init__(self, num):
        self.num = num

    def __add__(self, num2):
        print("let's Add")
        return self.num + num2.num

    def __mul__(self, num2):
        print("let's Multiply")
        return self.num * num2.num

    def __str__(self):
        return f"Decimal Number: {self.num}"

    def __len__(self):
        return 1

n = Number(9)    
print(n)    
print(len(n))