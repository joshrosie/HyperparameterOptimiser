
import subprocess
import tempfile
import sys
from pymooProblem import geneticAlgorithm;

#Once we have a better understanding of how we should allow the user to
# interact with the system (like specifying incremental, accessing ancestry, starting from scratch etc.)
# then this gathering of arguments from the command line will be more robust and less hard-coded.

filename = sys.argv[1]  #e.g. test1.wcard
timeout = sys.argv[2]   #e.g. 2 (seconds)

def Convert(string):
    new_list = list(string.split(" "))
    return new_list


def main():
    geneticAlgorithm()

    
def runCarlSAT_extract(a,b,c,e,f,r,x):


    sLine = './CarlSAT -a {} -b {} -c {} -e {} -f {} -r {} -x {} -t {} -v 2 -z {}'.format(a,b,c,e,f,r,x,timeout,filename)
    # The following execution of CarlSat and extraction of console output will most likely be moved to a solver object.
    #Inevitably the cost and timestamp will also be passed into a pymoo problem object/ function as its objectives

    with tempfile.TemporaryFile() as tempf:

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


        # Extract the best cost (in this run of CarlSat)
        cost = 0
        cost = eval(stringLine[(posChar + 2):(len(stringLine) - 1)])
       # print(cost)

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



if __name__ == "__main__":
    main()
