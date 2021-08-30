
import subprocess
import tempfile
import sys
#from GenAlgFrameWork import geneticAlgorithm;

#Once we have a better understanding of how we should allow the user to
# interact with the system (like specifying incremental, accessing ancestry, starting from scratch etc.)
# then this gathering of arguments from the command line will be more robust and less hard-coded.

filename = sys.argv[1]  #e.g. test1.wcard
timeout = sys.argv[2]   #e.g. 2 (seconds)
testArg = sys.argv[3] #test

def Convert(string):
    new_list = list(string.split(" "))
    return new_list


#def main():
  #  geneticAlgorithm()

def mainTest():
    print("running test...")
    print(runCarlSAT(2,4,200,1000,5,30,4))
    print("finished!")


def runCarlSAT(a,b,c,e,f,r,x):
    
    sLine = './CarlSAT -a {} -b {} -c {} -e {} -f {} -r {} -x {} -t {} -v 2 -z {}'.format(a, b, c, e, f, r, x, timeout, filename)

    with tempfile.TemporaryFile() as tempf:

        proc = subprocess.Popen(list(sline.split(" ")), stdout=tempf)
        proc.wait()
        #_ potentially write to database

    return extractObjectives(tempf)


def extractObjectives(tempf):

        tempf.seek(-27,2) #get last 27 characters

        cost = eval(str(tempf.readline(), 'utf-8').split()[1])
        time = eval(str(tempf.readline(), 'utf-8').split()[3])
            
        #may have to get out improvement objective from CarlSAT or otherwise we may need to calculate that and return back to GA
        
        timeTakenMs = time * 1000
        maxTimeMs = eval(timeout) * 1000

        #maybe return the objective here:
             ######### finalCost = bestCost + timeStamp_of_bestCost/ max_Time. Where max_Time is the timeout specified by the user
        #obj_val = cost + (timeTakenMs / maxTimeMs)

        return [cost,timeTakenMs,maxTimeMs]

# def write():
#     pass

if sys.argv[3] == 'true':
    mainTest()
else:
    if __name__ == "__main__":
    main()
