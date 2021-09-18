import numpy as np
import subprocess
import tempfile
<<<<<<< HEAD
import sys, os
from ParamFunhouse import ParamFunhouse
import GA_Tuner
import SolverProblem
=======
import sys
import pymooProblem

#Once we have a better understanding of how we should allow the user to
# interact with the system (like specifying incremental, accessing ancestry, starting from scratch etc.)
# then this gathering of arguments from the command line will be more robust and less hard-coded.
>>>>>>> 0c3eed5d92a3c126ccb8af5acaca3680e5066fb9

filename = sys.argv[1]  #e.g. test1.wcard
timeout = sys.argv[2]   #e.g. 2 (seconds)

pf = ParamFunhouse()

def main():

<<<<<<< HEAD
    tuner = GA_Tuner.GA_Tuner()
    result = tuner.geneticAlgorithm()
    output(tuner.report(result))




def mainTest():
    print("entered testing")
    if testCall == 'carlSAT' or testCall == 'obj' or testCall == 'cost':
        pf = ParamFunhouse()
        x=[1,2,1,4,6,10,14]
        print("running test...")
        saveFile = runCarlSAT(x)
        print("finished!!!")

        if testCall == 'obj' or testCall == 'cost':
            print(saveFile.name)
            objectives = extractObjectives(saveFile)
            print(str(objectives) + " are the objectives")

            if testCall == 'cost':
                cost = calculateCosts(objectives)
                print(str(cost) + " is the associated cost")
                

#this takes in pymoo parameters, runs the solver with those parameters
#extracts the objectives and returns the calculated cost(s) associated with that run
def getCost(pymooParams):
    #convert pymoo parameters into carlsat parameters
    carlSATparams = pf.getParameters(pymooParams)
    resultFile = runCarlSAT(carlSATparams)
    objectives = extractObjectives(resultFile)

    return calculateCosts(objectives)


def runCarlSAT(p):
    
    sLine = './CarlSAT -a {} -b {} -c {} -e {} -f {} -r {} -x {} -t {} -v 2 -z {}'.format( p[0], p[1], p[2], p[3], p[4], p[5], p[6], timeout, filename)
=======
def main():
    pymooProblem.geneticAlgorithm()

    
def runCarlSAT_extract(a,b,c,e,f,r,x):


    sLine = './CarlSAT -a {} -b {} -c {} -e {} -f {} -r {} -x {} -t {} -v 2 -z {}'.format(a,b,c,e,f,r,x,timeout,filename)
    # The following execution of CarlSat and extraction of console output will most likely be moved to a solver object.
    #Inevitably the cost and timestamp will also be passed into a pymoo problem object/ function as its objectives
>>>>>>> 0c3eed5d92a3c126ccb8af5acaca3680e5066fb9

    tempf = tempfile.NamedTemporaryFile(delete=False)
    with open(tempf.name, 'w') as tf:

<<<<<<< HEAD
        proc = subprocess.Popen(list(sLine.split(" ")), stdout=tf)
        proc.wait()
        tf.seek(0)

    return tempf
=======
        # This runs whatever shell command you put into it and the console output is stored in the temporary file
        proc = subprocess.Popen(Convert(sLine), stdout=tempf) #?
  
        proc.wait()  # Waiting on child process to finish i.e. waiting until CarlSat is finished and displayed its output

        # Go to the end of the file and then back a bit to just have the last two lines of output left.
        tempf.seek(tempf.tell() - 27)
        # From current understanding - it is only the last two lines of the output that is relevant.

        # Convert bytes into string
        stringLine = str(tempf.readline(), 'utf-8')


        # Find the 'o' character that always comes before the cost value
        posChar = stringLine.find('o')
>>>>>>> 0c3eed5d92a3c126ccb8af5acaca3680e5066fb9


        # Extract the best cost (in this run of CarlSat)
        cost = 0
        cost = eval(stringLine[(posChar + 2):(len(stringLine) - 1)])
       # print(cost)

<<<<<<< HEAD
    with open(tempf.name, 'rb') as tf:
        tf.seek(-27,2)
        cost = eval(str(tf.readline(), 'utf-8').split()[1])
        time = eval(str(tf.readline(), 'utf-8').split()[3])
    tempf.close()
    os.unlink(tempf.name)

    timeTakenMs = time * 1000
    maxTimeMs = eval(timeout) * 1000

    return [cost, timeTakenMs, maxTimeMs]


# this function can be expanded to P2 and P3 where what/how we calculate cost(s) will change
def calculateCosts(objectives):
    finalCost = objectives[0] + objectives[1]/objectives[2]
    return finalCost #return an array once we have more than one objective to optimise
=======
        stringLine = str(tempf.readline(), 'utf-8')

        # Find the ':' character that always comes before the time stamp value
        posChar = stringLine.find(':')


        # Extract the time stamp of when the best cost was found (in this run of CarlSat)
        timeTaken = stringLine[(posChar + 2):(len(stringLine) - 3)]
        

        # Convert the timeTaken into its millisecond representation
        timeTakenMs = eval(timeTaken) * 1000
        maxTimeMs = eval(timeout) * 1000 

        #print(timeTakenMs)

        return [cost,timeTakenMs,maxTimeMs]    

>>>>>>> 0c3eed5d92a3c126ccb8af5acaca3680e5066fb9


<<<<<<< HEAD
def output(results):
        print('Time taken:', results[0])
        #these are just the indices, not param vals #update
        print("Best solution found with: \nParameters = %s,\nGiving Cost = %s" % (pf.getParameters(results[1]), results[2]))

if len(sys.argv) > 3:

    testCall = sys.argv[3] #e.g. 'carlSAT'
    mainTest()

else:
    if __name__ == "__main__":
        
        main()
=======
if __name__ == "__main__":
    main()
>>>>>>> 0c3eed5d92a3c126ccb8af5acaca3680e5066fb9
