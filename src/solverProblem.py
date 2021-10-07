from pymoo.core.problem import ElementwiseProblem
import numpy as np
<<<<<<< HEAD
import wrapper
=======
import Wrapper
>>>>>>> ede8e940e6986b73052a31415164aaa3ea68833e

class SolverProblem(ElementwiseProblem):

    def __init__(self, **kwargs):
        super().__init__(n_var=7,
                         n_obj=1,
                         n_constr=0,
                         xl=[0,0,0, 0,0,0,0], 
                         xu=[19,19,19,19,19,19,19], 
                         **kwargs)


    def _evaluate(self, x, out, *args, **kwargs):     

<<<<<<< HEAD

        objectives = wrapper.runCarlSAT_extract(
        aParams[x[0]], bParams[x[1]], cParams[x[2]],
        eParams[x[3]],fParams[x[4]],rParams[x[5]],xParams[x[6]])

        # print(aParams[x[0]],  bParams[x[1]] , cParams[x[2]] ,
        # eParams[x[3]] , fParams[x[4]] , rParams[x[5]] , xParams[x[6]], sep = ':')
        
        #Condense the 3 objectives into one cost. This cost is what we are trying to minimize:
        # From Johan's email, the formula is understood to be:
        # finalCost = bestCost + timeStamp_of_bestCost/ max_Time. Where max_Time is the timeout specified by the user
        
        cost = objectives[0] + objectives[1]/objectives[2]
       # print(cost)
        
        #Add the cost to the dictionary (this is how the GA keeps track of the previous scores)
=======
        cost = Wrapper.getCost(x)
>>>>>>> ede8e940e6986b73052a31415164aaa3ea68833e
        out["F"] = np.column_stack([cost])



