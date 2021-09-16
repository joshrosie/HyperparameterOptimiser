from pymoo.model.problem import Problem
import numpy as np
import Wrapper

class SolverProblem(Problem):

    def __init__(self, **kwargs):
        super().__init__(n_var=7,
                         n_obj=1,
                         n_constr=0,
                         xl=[0,0,0, 0,0,0,0], 
                         xu=[19,19,19,19,19,19,19], 
                         elementwise_evaluation=True,
                         **kwargs)


    def _evaluate(self, x, out, *args, **kwargs):     

        cost = Wrapper.getCost(x)
        out["F"] = np.column_stack([cost])



