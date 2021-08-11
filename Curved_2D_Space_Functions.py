'''
Geodesic Calculator by Stavros Klaoudatos
Made on 10/8/2021- took 2:30 hours

=== THE FILE CURRENTLY IS SETUP TO CALCULATE THE GEODESIC EQUATION FOR A SPHERE WHERE u = t and v = k*l ===

Hello and thanks for downloading/ viewing my code. I have made a simple script to help calculate
the Notorious Christoffel Symbols and Geodesic Equations.

At the time I was 16 years old. I liked Tensor Calculus and science in General.

Note that this script is not for solving all geodesic problems. It is for solving
the equations, and calculating the Christoffel Symbols, for curved 2D space.

You need to setup all the parameters in order for this script to help you.

I Suggest you use this for verification. So far, it has calculated corectly many examples, but obviously there limitations.

For example, sympy can raise a NotImplementedError whenever it cannot solve something.

Thanks a lot.

For any inquires or assistance contact me @ stavrosklaoudatos@gmail.com

'''





import sympy as sp
from sympy.interactive import printing

printing.init_printing(use_latex=True)

# Placegolder Values for the Metric Tensor (Will become Inverse Metric Tensor Later)
g = [[[11], [12]], [[21], [22]]]

# Setting Up Parameters
l = sp.symbols("l")
k = sp.symbols('k')
t = sp.symbols('t')

# Setting Up the Initial Flat 2D space as a position based function of u and v parametrised by l
# Will enable me to differentiate with respect to u and v
u = sp.Function('u')(l)
v = sp.Function('v')(l)

# Values of u and v for solving the Geodesic Equations

u_func = l
v_func = l

# Lists to make loops easier and generalize
basis = [u, v]
funcs = [u_func, v_func]

# 2D Curved Space projected on a Cartesian 3D Space

X, Y, Z = sp.cos(v) * sp.sin(u), sp.sin(v) * sp.sin(u), sp.cos(u)

#Basically useless but here if you need it
R = sp.Function('R')(X, Y, Z)
eu = sp.diff(R, u)
ev = sp.diff(R, v)

#Computing the Contravariant Metric Tensor

def compute_inverse_metric_tensor(g=g):
    for i in range(len(basis)):
        for j in range(len(basis)):
            g[i][j] = sp.simplify(
                sp.diff(X, basis[i]) * sp.diff(X, basis[j]) + sp.diff(Y, basis[i]) * sp.diff(Y, basis[j]) + sp.diff(Z,
                                                                                                                    basis[
                                                                                                                        i]) * sp.diff(
                    Z, basis[j]))

            if i == j:
                g[i][j] = 1 / g[i][j]
            else:
                g[i][j] = -g[i][j]

    return g

#Computing Arclength
#Using Numerical Integration because sympy is not strong enough
def calculate_arc_length(g=compute_inverse_metric_tensor(), u=u, v=v, X=X, Y=Y, Z=Z, l=l, a=0, b=sp.pi/2,n=10):
    magRsqrt = 0
    for i in range(len(basis)):
        for j in range(len(basis)):
            if i == j:
                g[i][j] = 1 / g[i][j]
            else:
                g[i][j] = -g[i][j]

    print(g)

    for i in range(len(basis)):
        for j in range(len(basis)):
            term = sp.diff(funcs[i], l) * sp.diff(funcs[j], l) * g[i][j]
            term = term.subs(u, u_func)
            term = term.subs(v, v_func)
            term = term.subs(sp.cos(l), sp.cos(l))

            magRsqrt += term



    magR = sp.simplify(sp.sqrt(magRsqrt))
    print(magR)

    arclen = sp.simplify(((b - a) / n) * (magR.subs(l, a) / 2 + sum([magR.subs(l, a + k * (b - a) / n) for k in range(n)]) + magR.subs(l,b) / 2))

    print("Arclength from l = {} to  l = {}: ".format(a, b), arclen.evalf())
#Calculating the Christoffel Symbols

def calculate_Christoffel_Symbols(R=R, u=u, v=v, g=compute_inverse_metric_tensor()):
    G = [[[[0], [0]], [[0], [0]]], [[[0], [0]], [[0], [0]]]]

    for i in range(len(basis)):
        for j in range(len(basis)):
            for k in range(len(basis)):
                for m in range(len(basis)):
                    G[i][j][k][0] += sp.diff(X, basis[i], basis[j]) * sp.diff(X, basis[m]) * g[m][k] + sp.diff(Y,
                                                                                                               basis[i],
                                                                                                               basis[
                                                                                                                   j]) * sp.diff(
                        Y, basis[m]) * g[m][k] + sp.diff(Z, basis[i], basis[j]) * sp.diff(Z, basis[m]) * g[m][k]

                G[i][j][k][0] = sp.simplify(G[i][j][k][0])
               # print(G[i][j][k])

    return G

# Solving the Geodesic Equations

def Solve_Geodesic_Equation(u=u, v=v, G=calculate_Christoffel_Symbols()):
    solutionsl = []
    solutionsk = []
    solutionst = []
    solutions  = []
    for i in range(len(basis)):
        for j in range(len(basis)):
            for k in range(len(basis)):

                term = sp.diff(funcs[k], l, l) + G[i][j][k][0] * sp.diff(funcs[i], l) * sp.diff(funcs[j], l)
                term = term.subs(u, u_func)
                term = term.subs(v, v_func)

                try:
                    solution = sp.solve(term, l)
                    solutionsl.append([solution])

                    solution = sp.solve(term, k)
                    solutionsk.append([solution])

                    solution = sp.solve(term, t)
                    solutionst.append(solution)

                except(NotImplementedError):
                    pass

    for n in range(len(solutionsk)):
        if solutionsk[n] != [[]] and solutionsk[n] != []:
            solutions.append("k ={}".format(solutionsk[n]))

        if solutionsl[n] != [[]] and solutionsl[n] != []:
            solutions.append("l ={}".format(solutionsl[n]))

        if solutionst[n] != [[]] and solutionst[n] != []:
            solutions.append("t ={}".format(solutionst[n]))
    solutions = list(dict.fromkeys(solutions))
    print("Solutions : ", solutions)


