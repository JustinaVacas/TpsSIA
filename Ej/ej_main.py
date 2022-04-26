import time
from scipy.optimize import minimize
import numpy as np
from Ej.function import error
from numpy import inf
from qiskit.algorithms.optimizers import ADAM


def main():

    # gradiente descendiente
    x1 = np.zeros(11)
    start_time = time.time()
    opt1 = minimize(error, x1, args=(), method='L-BFGS-B',
                    options={'disp': None, 'maxcor': 10, 'ftol': 2.220446049250313e-09, 'gtol': 1e-05, 'eps': 1e-08,
                             'maxfun': 15000, 'maxiter': 15000, 'iprint': - 1, 'maxls': 20,
                             'finite_diff_rel_step': None})
    print("Gradiente descendiente")
    print("W = ", opt1.x[0:3])
    print("w = " + str(opt1.x[3:6]) + "\n\t" + str(opt1.x[6:9]))
    print("w0 = ", opt1.x[9:11])
    print("Error = ", opt1.fun)
    print("Time = ", time.time() - start_time)

    # gradiente conjugado
    x2 = np.zeros(11)
    start_time2 = time.time()
    opt2 = minimize(error, x2, args=(), method='CG', options={'gtol': 1e-05, 'norm': inf, 'eps': 1.4901161193847656e-08, 'maxiter': None,
                           'disp': False, 'return_all': False, 'finite_diff_rel_step': None} )
    print("Gradiente conjugado")
    print("W = ", opt2.x[0:3])
    print("w = " + str(opt2.x[3:6]) + "\n\t" + str(opt2.x[6:9]))
    print("w0 = ", opt2.x[9:11])
    print("Error = ", opt2.fun)
    print("Time = ", time.time() - start_time2)

    # metodo adam
    x3 = np.zeros(11)
    start_time3 = time.time()
    opt3 = ADAM().optimize(11, error, initial_point=x3)
    print("Metodo Adam")
    print("W = ", [opt3[0][i] for i in range(0, 3)])
    print("w = " + str([opt3[0][i] for i in range(3, 6)]) + "\n\t" + str([opt3[0][i] for i in range(6, 9)]))
    print("w0 = ", [opt3[0][i] for i in range(9, 11)])
    print("Error = ", error(opt3[0]))
    print("Time = ", time.time() - start_time3)


print("Starting...")
main()
print("- END -")
