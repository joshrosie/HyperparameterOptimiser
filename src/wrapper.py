# from pymoo.algorithms.so_de import DE
# from pymoo.factory import get_problem
# from pymoo.operators.sampling.latin_hypercube_sampling import LatinHypercubeSampling
# from pymoo.optimize import minimize
import subprocess
import tempfile
import os
import sys

def Convert(string):
    new_list = list(string.split(" "))
    return new_list

def main():


    filename = sys.argv[1]
    timeout = sys.argv[2]
    
    sLine = './CarlSAT -a 2 -b 4 -c 200 -e 1000 -f 5 -r 30 -x 4 -t ' + timeout + ' -v 2 -z ' + filename

    with tempfile.TemporaryFile() as tempf:
        proc = subprocess.Popen(Convert(sLine), stdout=tempf)
        proc.wait()
        tempf.seek(tempf.tell() - 105)
        tempf.read
        for line in tempf:
            print(line.strip())
        # for line in tempf:
        #     print(line.strip())
       # print(tempf.read())
        
    # stream = os.popen('echo Returned output')
    # output = stream.read().strip()
    # print(output)

if __name__ == "__main__":
    main()