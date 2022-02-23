import sympy as sym

# x = sym.Symbol('x')
# y = sym.Symbol('y')


class math_expression():
    def __init__(self, exp):
        self.exp = exp
        x = sym.Symbol('x')
        y = sym.Symbol('y')

    def __str__(self):
        return f'mathExp({self.exp})'

    def __repr__(self):
        return f"mathExp({self.exp})"

    def simplify(self):
        # Can Work With Python Default Solving Also
        ans = sym.simplify(self.exp)
        return str(ans)

    def expand(self):
        ans = sym.expand(self.exp)
        return str(ans)


obj = math_expression('7 + x - 9')
print(obj)
print(type(obj))

v = math_expression('x + 8 + 9 - 4').simplify()
print(v)
print(type(v))

v2 = math_expression('(x + y) ** 3').expand()
print(v2)
print(type(v2))


# def eval_():
#     eq = str(input('(Linear) Equation You Want To Solve: '))
#     eq = eq.replace(' ', '')
#     eq_ans = eval(eq)
#     print(f'{eq} = {eq_ans}')
