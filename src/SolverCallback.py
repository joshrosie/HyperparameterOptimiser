class SolverCallback:

    def __init__(self) -> None:
        super().__init__()
        self.data = {}

    def notify(self, algorithm, **kwargs):
        #update the new parameter set
        #potentially use stochastic selection to update parameter space
        #update xl and xu #repo #p1 P2 P3
        #increase generation counter/ cumulative timeout.
        #20ms * gen0
        

        print("callback for generation: " + algorithm.problem)
        
        
