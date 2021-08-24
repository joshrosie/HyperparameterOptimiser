from pymoo.model.problem import Problem
import numpy as np
import wrapper

aParams = [1,2,3,4, 5, 6 , 7 ,8, 9 , 10, 15, 20, 30, 50, 100, 200, 300,500,800, 1000]
bParams = [1,2,3,4, 5, 6 , 7 ,8, 9 , 10, 15, 20, 30, 50, 100, 200, 300,500,800, 1000]
cParams = [10,20,40,80,100,150, 200, 300,400, 500, 800, 1000, 2000, 5000, 8000, 10000, 50000, 100000, 500000, 1000000]
eParams = [0.1,0.5,1,4,8,10, 16, 20,40, 80, 120, 300, 400, 500, 600, 700, 800, 900, 950, 1000] 
fParams = [0.1,0.2,0.5, 0.8, 1, 2, 3, 4,8,10, 16, 20,40, 80, 120, 300, 500, 700, 900, 1000]   
rParams = [0,2,4,6,8,10, 12, 15,20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90, 100]
xParams = [1,2,3,4, 5, 6 , 7 ,8, 9 , 10, 20, 50, 100, 250, 500, 1000, 2000,5000,8000, 10000]

class solverProblem(Problem):

    def __init__(self, **kwargs):
     
         super().__init__(n_var=7, n_obj=1, n_constr=0, xl=[0,0,0, 0,0,0,0], 
        xu=[19,19,19,19,19,19,19], 
        elementwise_evaluation=True, **kwargs)

    def _evaluate(self, x, out, *args, **kwargs):
        
        
        objectives = wrapper.runCarlSAT_extract(
        aParams[x[0]], bParams[x[1]], cParams[x[2]],
        eParams[x[3]],fParams[x[4]],rParams[x[5]],xParams[x[6]])

        # print(aParams[x[0]],  bParams[x[1]] , cParams[x[2]] ,
        # eParams[x[3]] , fParams[x[4]] , rParams[x[5]] , xParams[x[6]], sep = ':')
        

        cost = objectives[0] + objectives[1]/objectives[2]
        #print(cost)
        
        out["F"] = np.column_stack([cost])




