#tester

from ParamFunhouse import ParamFunhouse
from GA_Tuner import GA_Tuner

tuner = GA_Tuner()
result = tuner.geneticAlgorithm()
solver.report(result)

pf = ParamFunhouse(style="hardcoded")
x = [0,2,9,15,2,1,19]
y = [0,0,0,0,0,0,0]

testParameters = pf.getParameters(x)
print(testParameters)

testParameters = pf.getParameters(y)
print(testParameters)

print(pf.plot(0))
