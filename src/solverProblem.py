from pymoo.core.problem import ElementwiseProblem
#test
import numpy as np
import Wrapper

class SolverProblem(ElementwiseProblem):

    def __init__(self, **kwargs):
        super().__init__(n_var=7,
                         n_obj=1,
                         n_constr=0,
                         xl=[0,0,0, 0,0,0,0], 
                         xu=[19,19,19,19,19,19,19], 
                         **kwargs)


    def _evaluate(self, x, out, *args, **kwargs):     

        cost = Wrapper.getCost(x)
        out["F"] = np.column_stack([cost])



