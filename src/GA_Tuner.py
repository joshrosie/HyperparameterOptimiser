from pymoo.algorithms.so_de import DE

from pymoo.optimize import minimize
from pymoo.configuration import Configuration
from pymoo.factory import get_termination, get_sampling
from multiprocessing.pool import ThreadPool

Configuration.show_compile_hint = False
import numpy as np
import SolverProblem 
import copy

class GA_Tuner:


    #solver will always have the same algorithm (DE) and problem number
    #what changes is just the way we run the GA (from state or scratch)
    def __init__(self, n_threads=64, problem=None, algorithm=None, populationSize=36):
        self.pool = ThreadPool(n_threads)
        if problem is None: #DC
            self.problem = SolverProblem.SolverProblem(parallelization = ('starmap', self.pool.starmap))
        else:
            self.problem = problem

        if algorithm is None:
            self.algorithm = DE(
            pop_size = populationSize,
            sampling=get_sampling("int_random"),  #Best pop_size is dependent on host's number of cores
            variant="DE/rand/1/bin",
            CR=0.9,
            F=0.8,
            dither="vector",
            jitter=False)



    def geneticAlgorithm(self, term_n_eval=1024, result=None, history=True): #give arg on how want to run.
        #Start the genetic algorithm
        if self.problem is None: #DC
            print("error: solver null")
        result = minimize(self.problem,
                        self.algorithm,
                        termination=('n_eval', term_n_eval), # inspect termination criteria for future prototypes
                        seed=1,
                        save_history=history,
                        verbose=True)  
        self.pool.close() #DC
        return result


    def report(self,result):
        print('Time taken:', result.exec_time)
        #these are just the indices, not param vals #update
        print("Best solution found: \nX = %s\nF = %s" % (result.X, result.F))


    #can add method to extract information/ancestory from result object
    def ancetry(result):
        pass #returns a key-word array to be put as an entry into db as well as output
