from pymoo.core.problem import ElementwiseProblem
import numpy as np
import wrapper

class SolverProblem(ElementwiseProblem):

    def __init__(self, **kwargs):

        super().__init__(n_var=7,
                         n_obj=1,
                         n_constr=0,
                         xl=[0,0,0,0,0,0,0], # make space here for these P1 P2 P3 lower
                         xu=[19,19,19,19,19,19,19], # make space here for these P1 P2 P3 upper
                         
                         **kwargs)


    def _evaluate(self, x, out, *args, **kwargs):     

        
        cost = wrapper.getCost(x)
        out["F"] = np.column_stack([cost])



