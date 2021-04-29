import scipy.stats as scs
import numpy as np
import math
import matplotlib.pyplot as plt

sizes = [20, 100]
names = ["Normal", "Cauchy", "Laplace", "Poisson", "Uniform"]


class distribution:
    def __init__(self, strDistribution: str) -> None:
        self.title = strDistribution
        self.size = [20, 100]
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

    def mustache(self):
        q1, q3 = np.quantile(self.arr, [0.25, 0.75])
        return q1 - 3 / 2 * (q3 - q1), q3 + + 3 / 2 * (q3 - q1)

    def emissions(self):
        x1, x3 = self.mustache()
        filter = [x for x in self.arr if x > x3 or x < x1]
        return len(filter)

    def draw_boxplot(self) -> None:
        arr = []
        self.build_arr(self.size[0])
        arr.append(self.arr)
        self.build_arr(self.size[1])
        arr.append(self.arr)
        labels = ["size = 20", "size = 100"]
        bplot = plt.boxplot(arr, patch_artist=True, labels=labels)
        plt.title(self.title)
        colors = ["pink", "red"]
        for patch, color in zip(bplot['boxes'], colors):
            patch.set_facecolor(color)
        plt.xlabel('2 size')
        plt.ylabel('Box plot')
        plt.show()

    def emission_share(self):
        arr_emis_share = []
        for i in range(len(self.size)):
            count = 0
            for j in range(self.repetitions):
                self.build_arr(self.size[i])
                count += self.emissions()
            count /= (self.size[i] * self.repetitions)
            arr_emis_share.append(count)
        return arr_emis_share