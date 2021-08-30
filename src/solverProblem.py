from pymoo.model.problem import Problem
import numpy as np
from wrapper import runCarlSAT_extract


#These arrays make up the 20 options available for the genetic algorithm to use.
# An idea suggested by Kiera is to make a parameterFactory class that can build arrays
# of this nature on the fly (i.e. specify different intervals, upper and lower bounds, scalars, custom functions etc.)
# and return the arrays to be used. This allows for more experimentation and versatility going forwards.
# It's also a nice thing to show the client/ tutor that we have tried something outside the box, instead of just hardcoding
# the options like how it is currently.        

class solverProblem(Problem):

    def __init__(self, **kwargs):
     
        #Initialize the problem. We have 7 design variables which can change how CarlSAT performs.
        #There is only one objective function which we are trying to minimize.
        #We have no constraints because this is a black box problem instead of a mathematical one
        # EXCEPT for lower and upper limits on the variables (they are between 0 and 19).
        # The variables are also constrained to being only integers, but that is controlled by the GA,
        # not in the problem definition.

         super().__init__(n_var=7, n_obj=1, n_constr=0, xl=[0,0,0, 0,0,0,0], 
        xu=[19,19,19,19,19,19,19], 
        elementwise_evaluation=True, **kwargs)

    def _evaluate(self, x, out, *args, **kwargs):        
        objectives = runCarlSAT_extract(
        aParams[x[0]], bParams[x[1]], cParams[x[2]],
        eParams[x[3]],fParams[x[4]],rParams[x[5]],xParams[x[6]])

        # print(aParams[x[0]],  bParams[x[1]] , cParams[x[2]] ,
        # eParams[x[3]] , fParams[x[4]] , rParams[x[5]] , xParams[x[6]], sep = ':')
        
        #Condense the 3 objectives into one cost. This cost is what we are trying to minimize:
        # From Johan's email, the formula is understood to be:
        # finalCost = bestCost + timeStamp_of_bestCost/ max_Time. Where max_Time is the timeout specified by the user
        
        cost = objectives[0] + objectives[1]/objectives[2] #_eventually, in (P_II) will pass improvement as objective to GA
       # print(cost)
        
        #Add the cost to the dictionary (this is how the GA keeps track of the previous scores)
        out["F"] = np.column_stack([cost])

        #_?? column stack if single value?


