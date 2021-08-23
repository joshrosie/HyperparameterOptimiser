from pymoo.algorithms.so_de import DE

from pymoo.operators.sampling.latin_hypercube_sampling import LatinHypercubeSampling
from pymoo.optimize import minimize
from pymoo.configuration import Configuration
from pymoo.factory import get_termination

Configuration.show_compile_hint = False
import numpy as np
from solverProblem import solverProblem 
import copy

def geneticAlgorithm():

    cParams = [10,20,40,80,150, 200, 300,400, 500, 800, 1000, 2000, 5000, 8000, 10000, 50000, 100000, 500000, 1000000]
    aParams = [1,2,3,4, 5, 6 , 7 ,8, 9 , 10, 15, 20, 30, 50, 100, 200, 300,500,800, 1000]
    
    
    
    algorithm = DE(
    pop_size = 36, sampling=LatinHypercubeSampling(iterations=100, criterion="maxmin"),     #This sampling thing here needs to be changed to a predefined variable space instead of random
    variant="DE/rand/1/bin",
    CR=0.9,
    F=0.8,
    dither="vector",
    jitter=False, eliminate_duplicates=True)

    problem = solverProblem()

    # res = minimize(problem,
    #            algorithm,
    #             termination=('n_gen', 10),
    #            seed=1,
    #            verbose=True)

    # print("Best solution found: \nX = %s\nF = %s" % (res.X, res.F))

  
    termination = get_termination("n_gen", 5)
    # perform a copy of the algorithm to ensure reproducibility
    obj = copy.deepcopy(algorithm)

    # let the algorithm know what problem we are intending to solve and provide other attributes
    obj.setup(problem, termination=termination, seed=1)

    # until the termination criterion has not been met
    while obj.has_next():

    # perform an iteration of the algorithm
        obj.next()

    # access the algorithm to print some intermediate outputs
        print(f"gen: {obj.n_gen} n_nds: {len(obj.opt)} constr: {obj.opt.get('CV').min()} ideal: {obj.opt.get('F').min(axis=0)}")

    # finally obtain the result object
    result = obj.result()
    

