import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import scipy.optimize as opt


file = open("../result/result.txt", "w")


def standard(x):
    return 2 + 2 * x


def standard_with_error(x):
    return [stats.norm.rvs(0, 1) + i for i in standard(x)]


def mnk_parameter(x, y):
    beta_1 = (np.mean(x * y) - np.mean(x) * np.mean(y)) / (np.mean(x * x) - np.mean(x) ** 2)
    beta_0 = np.mean(y) - beta_1 * np.mean(x)
    return beta_0, beta_1


def mnk(x, y):
    beta_0, beta_1 = mnk_parameter(x, y)
    file.write("MNK: beta_0 = " + str(beta_0) + ", beta_1 = " + str(beta_1) + "\n")
    return [beta_0 + beta_1 * i for i in x]


def mnm_min(beta, x, y):
    beta_0, beta_1 = beta
    Sum = 0
    for i in range(len(x)):
        Sum += abs(y[i] - beta_0 - beta_1 * x[i])
    return Sum


def mnm_parameter(x, y):
    beta_0, beta_1 = mnk_parameter(x, y)
    result = opt.minimize(mnm_min, [beta_0, beta_1], args=(x, y), method='SLSQP')
    coefs = result.x
    alpha_0, alpha_1 = coefs[0], coefs[1]
    return alpha_0, alpha_1


def mnm(x, y):
    beta_0, beta_1 = mnm_parameter(x, y)
    file.write("MNM: beta_0 = " + str(beta_0) + ", beta_1 = " + str(beta_1) + "\n")
    return [beta_0 + beta_1 * element for element in x]


def build_graphic(x, y, name):
    y_mnk = mnk(x, y)
    y_mnm = mnm(x, y)
    dist_mnk = sum([(standard(x)[i] - y_mnk[i])**2 for i in range(len(y))])
    dist_mnm = sum([abs(standard(x)[i] - y_mnm[i]) for i in range(len(y))])
    file.write("mnk distance = " + str(dist_mnk) + ", mnm distance = " + str(dist_mnm) + "\n")

    plt.plot(x, standard(x), color="red", label="Эталон")
    plt.plot(x, y_mnk, color="green", label="МНК")
    plt.plot(x, y_mnm, color="orange", label="МНМ")
    plt.scatter(x, y, c="blue", label="Выборка")
    plt.xlim([-2, 2.2])
    plt.grid()
    plt.legend()
    plt.title(name)
    plt.show()


