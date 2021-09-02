import numpy as np
import subprocess
import tempfile
import sys, os
from ParamFunhouse import ParamFunhouse
import GA_Tuner
import SolverProblem

filename = sys.argv[1]  #e.g. test1.wcard
timeout = sys.argv[2]   #e.g. 2 (seconds)

pf = ParamFunhouse()

def main():

    #pool = ThreadPool(64)
    #problem = SolverProblem(parallelization = ('starmap', pool.starmap))

    #tuner = GA_Tuner(ownProblem = problem,)
    tuner = GA_Tuner.GA_Tuner()
    result = tuner.geneticAlgorithm()

    tuner.report(result)

    # solver = ()
    # result = GA_Tuner.geneticAlgorithm()
    # solver.report(result)

def mainTest():
    if testCall == 'carlSAT' or testCall == 'obj' or testCall == 'cost':
        print("entered testing")
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

    tempf = tempfile.NamedTemporaryFile(delete=False)
    with open(tempf.name, 'w') as tf:

        proc = subprocess.Popen(list(sLine.split(" ")), stdout=tf)
        proc.wait()
        tf.seek(0)
        #_ potentially write to database
    #testing seek
    #tempf.seek(-27,2)
    return tempf


def extractObjectives(tempf):
    #print(tempf.name)
    with open(tempf.name, 'rb') as tf:
        tf.seek(-27,2) #get last 27 characters

        cost = eval(str(tf.readline(), 'utf-8').split()[1])
        time = eval(str(tf.readline(), 'utf-8').split()[3])
    tempf.close()
    os.unlink(tempf.name)

    timeTakenMs = time * 1000
    maxTimeMs = eval(timeout) * 1000

    return [cost, timeTakenMs, maxTimeMs]


# this function can be expanded to P2 and P3 where what/how we calculate cost(s) will change
def calculateCosts(objectives):
    #print("inside costs function, objectives are" + str(objectives))
    finalCost = objectives[0] + objectives[1]/objectives[2]
    #print(finalCost)
    return finalCost #return an array once we have more than one objective to optimise

# def write():
#     pass

if len(sys.argv) > 3:
    #print(sys.argv[0])
    testCall = sys.argv[3] #e.g.
    mainTest()

else:
    if __name__ == "__main__":
        
        main()
