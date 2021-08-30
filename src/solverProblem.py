from pymoo.model.problem import Problem
import numpy as np
from wrapper import runCarlSAT_extract


#These arrays make up the 20 options available for the genetic algorithm to use.
# An idea suggested by Kiera is to make a parameterFactory class that can build arrays
# of this nature on the fly (i.e. specify different intervals, upper and lower bounds, scalars, custom functions etc.)
# and return the arrays to be used. This allows for more experimentation and versatility going forwards.
# It's also a nice thing to show the client/ tutor that we have tried something outside the box, instead of just hardcoding
# the options like how it is currently.

aParams = [1,2,3,4, 5, 6 , 7 ,8, 9 , 10, 15, 20, 30, 50, 100, 200, 300,500,800, 1000]
bParams = [1,2,3,4, 5, 6 , 7 ,8, 9 , 10, 15, 20, 30, 50, 100, 200, 300,500,800, 1000]
cParams = [10,20,40,80,100,150, 200, 300,400, 500, 800, 1000, 2000, 5000, 8000, 10000, 50000, 100000, 500000, 1000000]
eParams = [0.1,0.5,1,4,8,10, 16, 20,40, 80, 120, 300, 400, 500, 600, 700, 800, 900, 950, 1000] 
fParams = [0.1,0.2,0.5, 0.8, 1, 2, 3, 4,8,10, 16, 20,40, 80, 120, 300, 500, 700, 900, 1000]   
rParams = [0,2,4,6,8,10, 12, 15,20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90, 100]
xParams = [1,2,3,4, 5, 6 , 7 ,8, 9 , 10, 20, 50, 100, 250, 500, 1000, 2000,5000,8000, 10000]

  
        

class solverProblem(Problem):

    def __init__(self, **kwargs):
     
        #Initialize the problem. We have 7 design variables which can change how CarlSAT performs.
        #There is only one objective function which we are trying to minimize.
        #We have no constraints because this is a black box problem instead of a mathematical one
        # EXCEPT for lower and upper limits on the variables (they are between 0 and 19).
        # The variables are also constrained to being only integers, but that is controlled by the GA,
        # not in the problem definition.

       #  0 <= x1,x2,x3 .. X7 <= 19
        # X1,X2,X3 .. X7 ARE ALL INTEGERS (managed by GA)
        
         super().__init__(n_var=7, n_obj=1, n_constr=0, xl=[0,0,0, 0,0,0,0], 
        xu=[19,19,19,19,19,19,19], 
        elementwise_evaluation=True, **kwargs)

    def _evaluate(self, x, out, *args, **kwargs):   #The "x" param are the actual values chosen by the GA. 
                                                    #It is a one-dimensional array in this case, because we have set elementwise evaluation to true.
        
   
        
        #Run carlSAT with the parameters chosen by the genetic algorithm. The GA spits out integers
        # between 0 and 19, which correspond to indexes in the parameter arrays.
        # An example would be the GA spits out 2 for the first param (i.e. the "a" param). So x[0] = 2
        # This corresponds to the value 3 in the aParam array.
        # The flow looks like this: aParams[x[0]] -> aParams[2] -> 3. This is then passed to CarlSAT through
        # the call to runCarlSAT_extract()
        #CarlSAT_extract() returns the objectives (i.e. the best cost with its corresponding timestamp and the timeout)


        objectives = runCarlSAT_extract(
        aParams[x[0]], bParams[x[1]], cParams[x[2]],
        eParams[x[3]],fParams[x[4]],rParams[x[5]],xParams[x[6]])

        # print(aParams[x[0]],  bParams[x[1]] , cParams[x[2]] ,
        # eParams[x[3]] , fParams[x[4]] , rParams[x[5]] , xParams[x[6]], sep = ':')
        
        #Condense the 3 objectives into one cost. This cost is what we are trying to minimize:
        # From Johan's email, the formula is understood to be:
        # finalCost = bestCost + timeStamp_of_bestCost/ max_Time. Where max_Time is the timeout specified by the user
        
        finalCost = objectives[0] + objectives[1]/objectives[2] #Maybe we change the weight of best_cost vs time_stamp/ max_time
        
       # print(cost)
        
        #Add the cost to the dictionary (this is how the GA keeps track of the previous scores)
        out["F"] = np.column_stack([finalCost])
       


     




