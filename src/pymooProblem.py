from pymoo.algorithms.so_de import DE

from pymoo.optimize import minimize
from pymoo.configuration import Configuration
from pymoo.factory import get_termination, get_sampling
from multiprocessing.pool import ThreadPool


Configuration.show_compile_hint = False
import numpy as np
from solverProblem import solverProblem 
import copy

def geneticAlgorithm():


    # the number of threads to be used. Not sure what is optimal, but currently 64 works best
    n_threads = 64
   

    # initialize the thread pool
    pool = ThreadPool(n_threads)
   
    #DE algorithm currently with default, best practice values for parameters.
    algorithm = DE(
    pop_size = 36, sampling=get_sampling("int_random"),    #Need to decide upon best pop_size. Apparently it should be 36, but 128 seems to be faster; 
                                                           #however it doesn't always find a better solution than 36
    variant="DE/rand/1/bin",
    CR=0.9,
    F=0.8,
    dither="vector",
    jitter=False)

    #initialize the solver problem with parallelization
    problem = solverProblem(parallelization = ('starmap', pool.starmap))

    #Start the genetic algorithm
    res = minimize(problem,
               algorithm,
                termination=('n_eval', 1024),
               seed=1,
               verbose=True)

    #How long it took until the termination criteria was met.
    print('Time taken:', res.exec_time)

    print("Best solution found: \nX = %s\nF = %s" % (res.X, res.F))

  
    # termination = get_termination("n_gen", 5)
    # # perform a copy of the algorithm to ensure reproducibility
    # obj = copy.deepcopy(algorithm)

    # # let the algorithm know what problem we are intending to solve and provide other attributes
    # obj.setup(problem, termination=termination, seed=1)

    # # until the termination criterion has not been met
    # while obj.has_next():

    # # perform an iteration of the algorithm
    #     obj.next()

    # # access the algorithm to print some intermediate outputs
    #     print(f"gen: {obj.n_gen} n_nds: {len(obj.opt)} constr: {obj.opt.get('CV').min()} ideal: {obj.opt.get('F').min(axis=0)}")

    # # finally obtain the result object
    # result = obj.result()
    
    pool.close()

