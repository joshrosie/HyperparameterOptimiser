from pymoo.algorithms.so_de import DE

from pymoo.optimize import minimize
from pymoo.configuration import Configuration
from pymoo.factory import get_termination, get_sampling
from multiprocessing.pool import ThreadPool

Configuration.show_compile_hint = False
import numpy as np
from solverProblem import solverProblem 
import copy

class Solver:

    #our tester class could try with different algorithms
    def __init__(self, problem=None, algorithm=None, populationSize=36):

        if problem is None: #DC
            self.problem = solverProblem(parallelization = ('starmap', pool.starmap))

        if algorithm is None:
            self.algorithm = DE(
            pop_size = populationSize,
            sampling=get_sampling("int_random"),  #Best pop_size is dependent on host's number of cores
            variant="DE/rand/1/bin",
            CR=0.9,
            F=0.8,
            dither="vector",
            jitter=False)



def geneticAlgorithm(n_threads=64, term_n_eval=1024, result=None, history=True): #give arg on how want to run.
    #Start the genetic algorithm
    pool = ThreadPool(n_threads)

    result = minimize(problem,
                    algorithm,
                    termination=('n_eval', term_n_eval), # inspect termination criteria for future prototypes
                    seed=1,
                    save_history=history,
                    verbose=True)  
    pool.close()
    return result


def report(result):
    print('Time taken:', result.exec_time)
    #these are just the indices, not param vals #update
    print("Best solution found: \nX = %s\nF = %s" % (result.X, result.F))


#can add method to extract information/ancestory from result object
def ancetry(result):
    pass #returns a key-word array to be put as an entry into db as well as output
