import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.transforms as transforms
from matplotlib.patches import Ellipse


class distribution:
    def __init__(self) -> None:
        self.size = [20, 60, 100]
        self.rho = [0, 0.5, 0.9]
        self.repetitions = 1000
        self.arr = []
        self.mix = []

    def build_arr(self, size, rho) -> None:
        self.arr = stats.multivariate_normal.rvs([0, 0], [[1.0, rho], [rho, 1.0]], size=size)

    def build_mix(self, size, rho) -> None:
        self.mix = 0.9 * stats.multivariate_normal.rvs([0, 0], [[1, 0.9], [0.9, 1]], size) +\
           0.1 * stats.multivariate_normal.rvs([0, 0], [[10, -0.9], [-0.9, 10]], size)

    def quadrant(self, x, y):
        res = [0, 0, 0, 0]
        xmed = np.median(x)
        ymed = np.median(y)
        for i in range(len(x)):
            if x[i] >= xmed and y[i] >= ymed:
                res[0] += 1
            elif x[i] < xmed and y[i] >= ymed:
                res[1] += 1
            elif x[i] < xmed and y[i] < ymed:
                res[2] += 1
            elif x[i] >= xmed and y[i] < ymed:
                res[3] += 1
        return (res[0] + res[2] - res[1] - res[3]) / len(self.arr)

    def coeff(self, fun, size, rho):
        pearson, quadrant, spirman = [], [], []
        for i in range(self.repetitions):
            fun(size, rho)
            if fun == self.build_arr:
                x = [i[0] for i in self.arr]
                y = [i[1] for i in self.arr]
            else:
                x = [i[0] for i in self.mix]
                y = [i[1] for i in self.mix]
            quadrant.append(self.quadrant(x, y))
            pearson.append(stats.pearsonr(x, y)[0])
            spirman.append(stats.spearmanr(x, y)[0])
        return pearson, spirman, quadrant

    def build_table(self, p, s, q):
        e = []
        e_2 = []
        d = []
        e.append(np.around(np.mean(p), decimals=4))
        e.append(np.around(np.mean(s), decimals=4))
        e.append(np.around(np.mean(q), decimals=4))
        d.append(np.around(np.var(p), decimals=4))
        d.append(np.around(np.var(s), decimals=4))
        d.append(np.around(np.var(q), decimals=4))

        for i in range(len(e)):
            e_2.append(np.around(d[i] + e[i] * e[i], decimals=4))
        return e, e_2, d

    def build_ellipse(self, x, y, axs):
        cov = np.cov(x, y)
        pearson = cov[0, 1] / np.sqrt(cov[0, 0] * cov[1, 1])
        rad_x = np.sqrt(1 + pearson)
        rad_y = np.sqrt(1 - pearson)
        ellipse = Ellipse((0, 0), width=rad_x * 2, height=rad_y * 2, facecolor='none', edgecolor='red')

        scale_x = np.sqrt(cov[0, 0]) * 3
        mean_x = np.mean(x)

        scale_y = np.sqrt(cov[1, 1]) * 3
        mean_y = np.mean(y)

        transform = transforms.Affine2D().rotate_deg(45).scale(scale_x, scale_y).translate(mean_x, mean_y)
        ellipse.set_transform(transform + axs.transData)
        return axs.add_patch(ellipse)

    def show_ellipse(self):
        titles = ["rho = 0", "rho = 0.5", "rho = 0.9"]
        for i in range(len(self.size)):
            figure, axs = plt.subplots(nrows=1, ncols=3)
            for j in range(len(self.rho)):
                self.build_arr(self.size[i], self.rho[j])
                x = [k[0] for k in self.arr]
                y = [k[1] for k in self.arr]
                self.build_ellipse(x, y, axs[j])
                axs[j].grid()
                axs[j].scatter(x, y, s=5)
                axs[j].set_title(titles[j])
            plt.suptitle("n = " + str(self.size[i]))
            plt.show()

    def main(self):
        file = open("../result/result.txt", "w")
        for i in range(len(self.size)):
            file.write("size = %d\n" % self.size[i])
            for j in range(len(self.rho)):
                file.write("rho = %.1f\n" % self.rho[j])
                file.write("         r       r_s      r_Q\n")
                p, s, q = self.coeff(self.build_arr, self.size[i], self.rho[j])
                e, e_2, d = self.build_table(p, s, q)
                file.write("E(z) = " + str(e) + "\n")
                file.write("E(z^2) = " + str(e_2) + "\n")
                file.write("D(z) = " + str(d) + "\n")
                file.write("\n")

        file.write("\n\nFor mix\n")
        for i in range(len(self.size)):
            p, s, q = self.coeff(self.build_mix, self.size[i], 0)
            e, e_2, d = self.build_table(p, s, q)
            file.write("n = %d     r       r_s      r_Q\n" % self.size[i])
            file.write("E(z) = " + str(e) + "\n")
            file.write("E(z^2) = " + str(e_2) + "\n")
            file.write("D(z) = " + str(d) + "\n")
            file.write("\n")
        self.show_ellipse()
