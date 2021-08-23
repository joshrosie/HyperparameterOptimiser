from pymoo.model.problem import Problem
import numpy as np
import wrapper



class solverProblem(Problem):

    def __init__(self):
        super().__init__(n_var=7, n_obj=1, n_constr=0, xl=[1,1,10, 0.1,0.1,0,1], 
        xu=[1000,1000,1000000,1000.0,1000.0,100,10000], 
        elementwise_evaluation=True)

    def _evaluate(self, x, out, *args, **kwargs):
        
        cost = wrapper.runCarlSAT_extract(x[0], x[1], x[2],x[3],x[4],x[5],x[6])
        combinedCost = cost[0] + cost[1]/cost[2]
        
        out["F"] = np.column_stack([combinedCost])




