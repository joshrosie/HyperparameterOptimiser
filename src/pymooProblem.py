from pymoo.algorithms.so_de import DE
from pymoo.factory import get_problem
from pymoo.operators.sampling.latin_hypercube_sampling import LatinHypercubeSampling
from pymoo.optimize import minimize
from pymoo.configuration import Configuration
Configuration.show_compile_hint = False
import numpy as np

def geneticAlgorithm():

    algorithm = DE(pop_size = 36, sampling=LatinHypercubeSampling(iterations=100, criterion="maxmin"),
        variant="DE/rand/1/bin",
        CR=0.5,
        F=0.3,
        dither="vector",
        jitter=False
    )

    problem = get_problem("ackley", n_var=10)

    res = minimize(problem,
               algorithm,
               seed=1,
               verbose=False)

    print("Best solution found: \nX = %s\nF = %s" % (res.X, res.F))

