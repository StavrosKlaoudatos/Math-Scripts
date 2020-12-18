import sympy as sm
y = sm.Symbol("y")
x = sm.Symbol("x")
z = sm.Symbol("z")
def Derivativeofx(respectto,function):
    import sympy as sm
    y = sm.Symbol("y")
    x = sm.Symbol("x")
    z = sm.Symbol("z")
    if respectto == x:
        differentiaytion = sm.diff(function,x)
    if respectto == y:
        differentiaytion = sm.diff(function, y)
    if respectto == z:
        differentiaytion = sm.diff(function, z)



    print(differentiaytion)



