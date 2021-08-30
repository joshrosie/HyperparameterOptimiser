import numpy as np
import matplotlib.pyplot as plt

parameterSet
lowerBounds, upperBounds




def generateSets(lowers,uppers,style):
    lowerBounds = lowers
    upperBounds = uppers

    if style == 'default':
        defaultGen()
    if style == 'hard-coded':
        hardCodeGen()

def getParameters(array):
    result = []

    for i in range(7):
        result[i] = [ parameterset[i][array[i]] ]


    # return [paramterset[0][array[0]],
    #         paramterset[1][array[1]],
    #         paramterset[2][array[2]],
    #         paramterset[3][array[3]],
    #         paramterset[4][array[4]],
    #         paramterset[5][array[5]]]


def defaultGen():
    for i in range(7):
        parameterSet[i] = geomspace(lowerBounds[i],upperBounds[i],num=20,dtype=int)
        plot(i)

def hardCodeGen():
    parameterSet[1] = [1,2,3,4, 5, 6 , 7 ,8, 9 , 10, 15, 20, 30, 50, 100, 200, 300,500,800, 1000]
    parameterSet[0] = [1,2,3,4, 5, 6 , 7 ,8, 9 , 10, 15, 20, 30, 50, 100, 200, 300,500,800, 1000]
    parameterSet[2] = [10,20,40,80,100,150, 200, 300,400, 500, 800, 1000, 2000, 5000, 8000, 10000, 50000, 100000, 500000, 1000000]
    parameterSet[3] = [0.1,0.5,1,4,8,10, 16, 20,40, 80, 120, 300, 400, 500, 600, 700, 800, 900, 950, 1000] 
    parameterSet[4] = [0.1,0.2,0.5, 0.8, 1, 2, 3, 4,8,10, 16, 20,40, 80, 120, 300, 500, 700, 900, 1000]   
    parameterSet[5] = [0,2,4,6,8,10, 12, 15,20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90, 100]
    parameterSet[6] = [1,2,3,4, 5, 6 , 7 ,8, 9 , 10, 20, 50, 100, 250, 500, 1000, 2000,5000,8000, 10000]

def fibonacciGen():
    pass


def plot(i):
    x = np.arange(0,20)
    y = paramterSet[i]
    plt.plot(x,y)
    plt.show()

parameterSet = [7]
hardCodeGen()
plot(0)
