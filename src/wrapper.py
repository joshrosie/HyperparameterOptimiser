
import subprocess
import tempfile
import sys

filename = sys.argv[1]  #e.g. test1.wcard
timeout = sys.argv[2]   #e.g. 2 (seconds)
testArg = sys.argv[3]   #test


def Convert(string):
    new_list = list(string.split(" "))
    return new_list


def main():
    solver = Solver()
    result = solver.geneticAlgorithm()
    solver.report(result)
    

def mainTest():
    print("running test...")
    print(runCarlSAT(2,4,200,1000,5,30,4))
    print("finished!")

def getCost(x):
    #convert pymoo parameters into carlsat parameters
    results = runCarlSAT(#parameter stuff)
    objectives = extractObjectives(results)
    return calculateCosts(objectives)


def runCarlSAT(a,b,c,e,f,r,x):
    
    sLine = './CarlSAT -a {} -b {} -c {} -e {} -f {} -r {} -x {} -t {} -v 2 -z {}'.format(a, b, c, e, f, r, x, timeout, filename)

    with tempfile.TemporaryFile() as tempf:

        proc = subprocess.Popen(list(sline.split(" ")), stdout=tempf)
        proc.wait()
        #_ potentially write to database

    #return extractObjectives(tempf)
    return tempf


def extractObjectives(tempf):

        tempf.seek(-27,2) #get last 27 characters

        cost = eval(str(tempf.readline(), 'utf-8').split()[1])
        time = eval(str(tempf.readline(), 'utf-8').split()[3])

        timeTakenMs = time * 1000
        maxTimeMs = eval(timeout) * 1000

    return [cost,timeTakenMs,maxTimeMs]

    # this function can be expanded to P2 and P3 where what/how we calculate cost(s) will change

def calculateCosts(objectives):
    cost = objectives[0] + objectives[1]/objectives[2]
    return Finalcost #return an array once we have more than one objective to optimise

# def write():
#     pass

if sys.argv[3] == 'true':
    mainTest()
else:
    if __name__ == "__main__":
    main()
