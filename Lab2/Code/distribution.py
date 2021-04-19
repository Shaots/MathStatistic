import numpy as np
import scipy.stats as scs
import math


class distribution:
    def __init__(self, strDistribution: str) -> None:
        self.title = strDistribution
        self.size = [10, 100, 1000]
        self.arr = []
        self.repetitions = 1000

    def build_arr(self, size_) -> None:
        if self.title == "Normal":
            self.arr = scs.norm.rvs(size=size_)
            self.arr.sort()
        if self.title == "Cauchy":
            self.arr = scs.cauchy.rvs(size=size_)
            self.arr.sort()
        if self.title == "Laplace":
            self.arr = scs.laplace.rvs(size=size_, scale=1 / math.sqrt(2), loc=0)
            self.arr.sort()
        if self.title == "Poisson":
            self.arr = scs.poisson.rvs(size=size_, mu=10)
            self.arr.sort()
        if self.title == "Uniform":
            self.arr = scs.uniform.rvs(size=size_, loc=-math.sqrt(3), scale=2 * math.sqrt(3))
            self.arr.sort()

    def z_r(self, size):
        return (self.arr[0] + self.arr[size - 1]) / 2

    def z_p(self, size: int, p: float):
        if (size * p).is_integer():
            return self.arr[int(size * p)]
        else:
            return self.arr[int(size * p) + 1]

    def z_q(self, size: int):
        return (self.z_p(size, 1 / 4) + self.z_p(size, 3 / 4)) / 2

    def z_tr(self, size: int):
        r = int(size / 4)
        sum_: float = 0.0
        for i in range(r + 1, size - r + 1):
            sum_ += self.arr[i]
        return sum_ / (size - 2 * r)

    def build_table(self):
        arrMean = []
        arrMedian = []
        arrZr = []
        arrZq = []
        arrZtr = []
        tableE = [[0 for i in range(5)] for j in range(len(self.size))]
        tableD = [[0 for i in range(5)] for j in range(len(self.size))]
        for i in range(len(self.size)):
            for j in range(self.repetitions):
                self.build_arr(self.size[i])
                arrMean.append(np.mean(self.arr))
                arrMedian.append(np.median(self.arr))
                arrZr.append(self.z_r(self.size[i]))
                arrZq.append(self.z_q(self.size[i]))
                arrZtr.append(self.z_tr(self.size[i]))
            tableE[i][0] = np.mean(arrMean)
            tableE[i][1] = np.mean(arrMedian)
            tableE[i][2] = np.mean(arrZr)
            tableE[i][3] = np.mean(arrZq)
            tableE[i][4] = np.mean(arrZtr)
            tableD[i][0] = np.var(arrMean)
            tableD[i][1] = np.var(arrMedian)
            tableD[i][2] = np.var(arrZr)
            tableD[i][3] = np.var(arrZq)
            tableD[i][4] = np.var(arrZtr)
        return tableE, tableD
