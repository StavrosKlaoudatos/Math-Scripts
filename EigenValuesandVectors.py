def FindEigenValuesandVectorsofMatrixorOperator(matrix):
    import math
    import numpy as np
    import scipy.linalg as la

    eigvals, eigvecs = la.eig(matrix)
    print("EigenValues: ",eigvals)
    print("EigenVectors: \n",eigvecs)




