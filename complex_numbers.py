import cmath, math, sympy
from sympy import symbols


x, a, b, c, d = symbols('x a b c d')

expr1 = (-1*b**3)/(27*a**3) + b*c/(6*a**2) - d/(2*a)
expr2 = expr1**2 + (c/(3*a) - b**2/(9*a**2))**3

solution1 = (expr1 + expr2**(1/2))**(1/3) + (expr1 - expr2**(1/2))**(1/3) - b/(3*a)
solution2 = (expr1 + expr2**(1/2))**(1/3) + (expr1 + expr2**(1/2))**(1/3) - b/(3*a)
solution3 = (expr1 - expr2**(1/2))**(1/3) + (expr1 - expr2**(1/2))**(1/3) - b/(3*a)

x**3 - 1

print(solution1.subs({a: 1, b: 0, c: 0, d: -1}))
print(solution2.subs({a: 1, b: 0, c: 0, d: -1}))
print(solution3.subs({a: 1, b: 0, c: 0, d: -1}))


