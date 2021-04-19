import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as scs
import math
from pathlib import Path


class distribution:
    def __init__(self, strDistribution: str, size: int) -> None:
        self.title = strDistribution

        if strDistribution == "Normal":
            self.fun = scs.norm()
            self.Hist = scs.norm.rvs(size=size)
        if strDistribution == "Cauchy":
            self.fun = scs.cauchy()
            self.Hist = scs.cauchy.rvs(size=size)
        if strDistribution == "Laplace":
            self.fun = scs.laplace(scale=1 / math.sqrt(2), loc=0)
            self.Hist = scs.laplace.rvs(size=size, scale=1 / math.sqrt(2), loc=0)
        if strDistribution == "Poisson":
            self.fun = scs.poisson(mu=10)
            self.Hist = scs.poisson.rvs(size=size, mu=10)
        if strDistribution == "Uniform":
            self.fun = scs.uniform(loc=-math.sqrt(3), scale=2 * math.sqrt(3))
            self.Hist = scs.uniform.rvs(size=size, loc=-math.sqrt(3), scale=2 * math.sqrt(3))

    def build(self, imgpath: Path) -> None:
        fig, ax = plt.subplots(1, 1)
        ax.hist(self.Hist, density=True, histtype="stepfilled")

        if self.title == "Poisson":
            x = np.arange(self.fun.ppf(0.01), self.fun.ppf(0.99))
        else:
            x = np.linspace(self.fun.ppf(0.01), self.fun.ppf(0.99), 100)

        if self.title == "Poisson":
            ax.plot(x, self.fun.pmf(x), "r")
        else:
            ax.plot(x, self.fun.pdf(x), "r")

        ax.set_xlabel(f"{len(self.Hist)}")
        ax.set_ylabel("density")
        ax.set_title(self.title)
        plt.grid()
        plt.savefig(imgpath)
