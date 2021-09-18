import matplotlib.pyplot as plt
import numpy as np

from pymoo.algorithms.moo.NSGA2 import NSGA2
from pymoo.factory import get_problem
from pymoo.core.callback.Callback import Callback
from pymoo.optimize import minimize


class MyCallback(Callback):

    def __init__(self) -> None:
        super().__init__()
        self.data["best"] = []

    def notify(self, algorithm):
        self.data["best"].append(algorithm.pop.get("F").min())
