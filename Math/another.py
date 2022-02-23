import math

a = int(input("Enter the coefficient of x. "))
b = int(input("Enter the constant in the equation. "))
if int(b) < 0:
    b = b * -1
    c = b / a
    d = str(a) + "x"
    print(d, "-", b, "= 0")
    print("Root: ", c)
else:
    e = b / a
    f = str(a) + "x"
    print(f, "+", b, "= 0")
    print("Root: ", (e * -1))
input("")
