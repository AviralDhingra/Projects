# import string

# alphabet_list = list(string.ascii_lowercase)
# print(alphabet_list + '   ' + type(alphabet_list))


"""
string = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'
print(string)
print(type(string))
string = string.split(' ')
print(string)
print(type(string))

for i in range(len(string)):
    string[i] = str(string[i])
    print(string[i])
# print(a)
"""

"""
import numpy as np

a = np.array([[3, -9], [2, 4]])  # [  [3, -9], [2, 4]  ]
print(a)
b = np.array([-42, 2])
print(b)

z = np.linalg.solve(a, b)
print(z)
"""


import sympy as sym
x = sym.Symbol('x')
y = sym.Symbol('y')

v = sym.solveset(x - 7, 7 + 2)
print(v)
print(type(v))
