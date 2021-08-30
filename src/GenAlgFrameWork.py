from pymoo.algorithms.so_de import DE

from pymoo.optimize import minimize
from pymoo.configuration import Configuration
from pymoo.factory import get_termination, get_sampling
from multiprocessing.pool import ThreadPool


Configuration.show_compile_hint = False
import numpy as np
from solverProblem import solverProblem 
import copy

 def initialize(n_threads,population,CrossOverRate,F,term_n_eval): #global instance variables? #like setting the settings. 
    
    algorithm = DE(
        pop_size = 36, sampling=get_sampling("int_random"),    #Best pop_size is dependent on host's number of cores
        variant="DE/rand/1/bin",
        CR=0.9,
        F=0.8,
        dither="vector",
        jitter=False)

    problem = solverProblem(parallelization = ('starmap', pool.starmap))
    


def geneticAlgorithm(n_threads,problem,algorithm,term_n_eval): #give arg on how want to run. should have global vars

    #genetic algorithm set-up factory

    #Start the genetic algorithm
    pool = ThreadPool(n_threads)

    res = minimize(problem,
               algorithm,
                termination=('n_eval', term_n_eval), # inspect termination criteria for future prototypes
               seed=1,
               save_history=True,
               verbose=True)

    print('Time taken:', res.exec_time)

    #these are just the indices, not param vals
    print("Best solution found: \nX = %s\nF = %s" % (res.X, res.F))     
    pool.close()

