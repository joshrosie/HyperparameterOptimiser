import numpy as np
import subprocess
import tempfile
import sys, os
from ParamFunhouse import ParamFunhouse
import GA_Tuner as GT
import Repository as REPO


problemCard = sys.argv[1]  #e.g. test1.wcard
timeout = sys.argv[2]   #e.g. 2 (seconds)
timeoutIt = eval(timeout)/20

pf = ParamFunhouse()

def main():
    repo = REPO.Repository()
    repo.initConnection()
    repo.insert([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,1,2,3])
    repo.insert([4,5,6,7,8,9,17,18,19,110,111,112,113,114,115,116,117,118,119,120,4,5,6])
    tables = repo.showTables()
    thing = repo.getStatesRanked([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,7,8,9])
    # for x in thing:
    #     print(x)
   # tuner = GT.GA_Tuner()
    #result = tuner.geneticAlgorithm()
    
    # tuner.report(result)

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
def getCost(pymooParams): #repo writes
    #convert pymoo parameters into carlsat parameters
    carlSATparams = pf.getParameters(pymooParams)
    resultFile = runCarlSAT(carlSATparams)
    objectives = extractObjectives(resultFile)

    return calculateCosts(objectives)


def runCarlSAT(p, entry):
    
  # inc(outputNum, entry) #repo's autonumber or something
    
    sParamString = '-a {} -b {} -c {} -e {} -f {} -r {} -x {}'.format( p[0], p[1], p[2], p[3], p[4], p[5], p[6]) #TV
    sArguments = '-m {} -v 2 -z {} -i {} -w {}'.format(timeoutIt, problemCard, p[7])
    sRunLine = './CarlSAT ' + sParamString + ' ' + sArguments
    
    tempf = tempfile.NamedTemporaryFile(delete=False)
    with open(tempf.name, 'w') as tf:

        proc = subprocess.Popen(list(sRunLine.split(" ")), stdout=tf)
        proc.wait()
        tf.seek(0)
    
    return [tempf,OutputfileName]

def extractObjectives(tempf):

    #extract A = end score of previous run (intermediate score, no longer final score)
    #starting score B (what run started with)
    # time needed to achieve starting score (cumulative) (dependent on A)
    # timeout given.

    with open(tempf.name, 'rb') as tf:
        tf.seek(-27,2)
        cost = eval(str(tf.readline(), 'utf-8').split()[1])
        time = eval(str(tf.readline(), 'utf-8').split()[3])
    tempf.close()
    os.unlink(tempf.name)

    timeTakenMs = time * 1000
    maxTimeMs = eval(timeout) * 1000

    return [A, B, C, D] #potentially be used by callback as printing.


# this function can be expanded to P2 and P3 where what/how we calculate cost(s) will change
def calculateCosts(objectives): 
    
    #An - Bn + Cn - Dn
    
    finalCost = (objectives[0] - objectives[1]) + (objectives[2] - objectives[3])
    return finalCost


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
