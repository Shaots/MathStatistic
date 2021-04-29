import scipy.stats as scs
import numpy as np
import math
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.distributions.empirical_distribution import ECDF


class distribution:
    def __init__(self, strDistribution: str) -> None:
        self.title = strDistribution
        self.size = [20, 60, 100]
        self.scale = [0.5, 1, 2]
        self.arr = []
        self.x = []
        self.mycdf = []
        self.mypdf = []

    def build_arr(self, size_) -> None:
        if self.title == "Normal":
            self.arr = scs.norm.rvs(size=size_)
            self.arr.sort()
            self.x = np.linspace(-4, 4, 1000)
            self.mycdf = scs.norm.cdf(self.x)
            self.mypdf = scs.norm.pdf(self.x)
        if self.title == "Cauchy":
            self.arr = scs.cauchy.rvs(size=size_)
            self.arr.sort()
            self.x = np.linspace(-4, 4, 1000)
            self.mycdf = scs.cauchy.cdf(self.x)
            self.mypdf = scs.cauchy.pdf(self.x)
        if self.title == "Laplace":
            self.arr = scs.laplace.rvs(size=size_, scale=1 / math.sqrt(2), loc=0)
            self.arr.sort()
            self.x = np.linspace(-4, 4, 1000)
            self.mycdf = scs.laplace.cdf(self.x, loc=0, scale=1 / math.sqrt(2))
            self.mypdf = scs.laplace.pdf(self.x, loc=0, scale=1 / math.sqrt(2))
        if self.title == "Poisson":
            self.arr = scs.poisson.rvs(size=size_, mu=10)
            self.arr.sort()
            self.x = np.linspace(6, 14, 1000)
            self.mycdf = scs.poisson(10).cdf(self.x)
            self.mypdf = scs.poisson(10).pmf(self.x),
        if self.title == "Uniform":
            self.arr = scs.uniform.rvs(size=size_, loc=-math.sqrt(3), scale=2 * math.sqrt(3))
            self.arr.sort()
            self.x = np.linspace(-4, 4, 1000)
            self.mycdf = scs.uniform.cdf(self.x, loc=-math.sqrt(3), scale=2 * math.sqrt(3))
            self.mypdf = scs.uniform.pdf(self.x, loc=-math.sqrt(3), scale=2 * math.sqrt(3))

    def draw_empirical(self):
        figure, axs = plt.subplots(nrows=1, ncols=3)

        for i in range(len(self.size)):
            self.build_arr(size_=self.size[i])
            ecdf = ECDF(self.arr)
            axs[i].plot(self.x, self.mycdf, color="red", label="cdf", linewidth=1)
            axs[i].plot(self.x, ecdf(self.x), color="blue", label='ecdf', linewidth=1)
            axs[i].legend(loc='lower right')
            axs[i].set_title("n = " + str(self.size[i]))
        figure.suptitle(self.title + " distribution")
        plt.show()

    def draw_kernel(self):
        for i in range(len(self.size)):
            figures, axs = plt.subplots(ncols=3)
            self.build_arr(size_=self.size[i])
            if self.title == "Poisson":
                self.x = np.linspace(6, 14, 9)
                self.mypdf = scs.poisson(10).pmf(self.x)
            for j in range(len(self.scale)):
                axs[j].plot(self.x, self.mypdf, color="red", label="pdf")
                sns.kdeplot(data=self.arr, bw_method="silverman", bw_adjust=self.scale[j], ax=axs[j],
                            fill=True, linewidth=0, label="kde")
                axs[j].legend(loc="upper right")
                axs[j].set(xlabel="x", ylabel="f(x)")
                axs[j].set_xlim([self.x[0], self.x[len(self.x) - 1]])
                axs[j].set_title("h = " + str(self.scale[j]))
            figures.suptitle(self.title + " KDE n = " + str(self.size[i]))
            plt.show()
