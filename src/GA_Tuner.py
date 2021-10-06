from pymoo.algorithms.soo.nonconvex.de import DE
from pymoo.core.problem import starmap_parallelized_eval
#test
from pymoo.algorithms.so_de import DE
from pymoo.algorithms.nsga2 import NSGA2
import matplotlib.pyplot as plt
import numpy as np


from pymoo.optimize import minimize
from pymoo.configuration import Configuration
from pymoo.factory import get_termination, get_sampling
from pymoo.core.callback import Callback
from multiprocessing.pool import ThreadPool
from Callback import Callback

Configuration.show_compile_hint = False
import numpy as np
import SolverProblem as SP
import copy

class GA_Tuner:


    def __init__(self, n_threads=8, problem=None, algorithm=None, populationSize=8):
        
        self.pool = ThreadPool(n_threads)
        if problem is None: #DC
            #self.problem = SolverProblem.SolverProblem(parallelization = ('starmap', self.pool.starmap))
            self.problem = SP.SolverProblem(runner=self.pool.starmap, func_eval=starmap_parallelized_eval)
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
        else:
            self.algorithm = GSGA2(
            pop_size = populationSize,
            sampling=get_sampling("int_random"),  #Best pop_size is dependent on host's number of cores
            variant="DE/rand/1/bin",
            CR=0.9,
            F=0.8,
            dither="vector",
            jitter=False)

        
        self.termination = get_termination("n_gen",8)
        self.callback = Callback()
        #termination critera change here



    def geneticAlgorithm(self, term_n_eval=1024, result=None, history=True): #give arg on how want to run.
        #Start the genetic algorithm
        if self.problem is None: #DC
            print("error: solver null")
        result = minimize(self.problem,
                        self.algorithm,
                       # termination=('n_eval', term_n_eval), # inspect termination criteria for future prototypes
                        termination = self.termination,
                        seed=1,
                        save_history=history,
                        callback=self.callback, #results will not be stored in callback object, but rather result.callback
                        verbose=True)  
        self.pool.close() #DC
        return result

    def plot(self,result):
        val = result.algorithm.callback.data["best"]
        plt.plot(np.arange(len(val)), val)
        plt.show()
        

    def report(self,result):
        return [result.exec_time, result.X, result.F]


    #can add method to extract information/ancestory from result object
    def ancetry(result):
        pass #returns a key-word array to be put as an entry into db as well as output

class callback:
    def __init__(self) -> None:
        super().__init__()
        self.data["best"] = []

    def notify(self, algorithm):
        self.data["best"].append(algorithm.pop.get("F").min())