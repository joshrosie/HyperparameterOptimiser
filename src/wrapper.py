
import subprocess
import tempfile
import os
import sys
import pymooProblem


def Convert(string):
    new_list = list(string.split(" "))
    return new_list


def main():

    filename = sys.argv[1]
    timeout = sys.argv[2]

    sLine = './CarlSAT -a 2 -b 4 -c 200 -e 1000 -f 5 -r 30 -x 4 -t ' + timeout + ' -v 2 -z ' + filename

    # The following execution of CarlSat and extraction of console output will most likely be moved to a solver object.
    #Inevitably the cost and timestamp will also be passed into a pymoo problem object/ function as its objectives

    with tempfile.TemporaryFile() as tempf:

        # This runs whatever shell command you put into it and the console output is stored in the temporary file
        proc = subprocess.Popen(Convert(sLine), stdout=tempf)

        proc.wait()  # Waiting on child process to finish i.e. waiting until CarlSat is finished and displayed its output

        # Go to the end of the file and then back a bit to just have the last two lines of output left.
        tempf.seek(tempf.tell() - 27)
        # From current understanding - it is only the last two lines of the output that is relevant, however maybe for prototype 2 onwards
        # We want the cost and time stamps for every flip - not just the final best cost and time stamp?



        # Convert bytes into string
        stringLine = str(tempf.readline(), 'utf-8')


        # Find the 'o' character that always comes before the cost value
        posChar = stringLine.find('o')


        # Extract the best cost (in this run of CarlSat)
        cost = stringLine[(posChar + 2):(len(stringLine) - 1)]
        print(cost)

        stringLine = str(tempf.readline(), 'utf-8')

        # Find the ':' character that always comes before the time stamp value
        posChar = stringLine.find(':')


        # Extract the time stamp of when the best cost was found (in this run of CarlSat)
        timeTaken = stringLine[(posChar + 2):(len(stringLine) - 3)]


        # Convert the timeTaken into its millisecond representation
        timeTakenMs = eval(timeTaken) * 1000
        print(timeTakenMs)

        pymooProblem.geneticAlgorithm()



if __name__ == "__main__":
    main()
