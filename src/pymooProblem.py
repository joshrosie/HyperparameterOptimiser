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


    #The number of threads to be used. Not sure what is optimal, but currently 64 works best. Anything higher didn't improve the speed, just used more memory.
    #Lower number of threads were slightly slower. Multithreading is better than multiprocessing in this case because of the CarlSAT problem being mainly I/O bound.
    #Furthermore, advanced frameworks like DASK introduce too much overhead and will actually lead to a performance decrease because the runs of CarlSAT
    # are limited to the timeout setting (i.e. they are I/O bound, we cannot make it run faster than the timeout).
    # see shorturl.at/otMO2 and shorturl.at/gtyJ1 for more information.
    n_threads = 64
   

    # initialize the thread pool
    pool = ThreadPool(n_threads)
   
    #DE algorithm currently with default, best practice values for parameters. We may find through experimention that some
    # parameters could be tweaked, but there is no "golden" rule - we have to discover it empirically.
    # However, our project is not focused on tuning these parameters. We are tuning what goes into CarlSAT.

    algorithm = DE(
    pop_size = 36, sampling=get_sampling("int_random"),    #Need to decide upon best pop_size. Apparently it should be 36 - according to Johan, but 128 seems to be faster; 
                                                           #however, larger values don't always find a better solution than 36
    variant="DE/rand/1/bin",
    CR=0.9,
    F=0.8,
    dither="vector",
    jitter=False)

    #initialize the solver problem with parallelization. Pymoo uses the starmap implementation for parallelization.
    #See https://pymoo.org/problems/parallelization.html

    problem = solverProblem(parallelization = ('starmap', pool.starmap))
    

    #Start the genetic algorithm
    res = minimize(problem,
               algorithm,
                termination=('n_eval', 1024), # inspect termination criteria for future prototypes
               seed=1,
               verbose=True)

    #How long it took until the termination criteria was met.
    print('Time taken:', res.exec_time)

    #note: The best solution values here will be the integers that correspond to indexes in the parameter arrays.
    #i.e. they are not the actual parameters that were found to be optimal for CarlSAT.
    #Eventually we will change this to be more appropriate once we have the parameter factory class.
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

