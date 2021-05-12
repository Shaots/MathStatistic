import numpy as np
from tabulate import tabulate
import scipy.stats as stats
import math

file = open("../result/result.txt", "w")
alpha = 0.05
p = 1 - alpha


def find_k(size):
    return math.ceil(1.72 * size ** (1 / 3))


def MLE(arr, k):
    mu = np.mean(arr)
    sigma = np.std(arr)
    chi_2 = stats.chi2.ppf(p, k - 1)
    file.write('mu = ' + str(np.around(mu, decimals=4)) + "\n")
    file.write('sigma = ' + str(np.around(sigma, decimals=4)) + "\n")
    file.write('chi_2 = ' + str(chi_2) + "\n")


def find_n_and_p(arr, limits):
    p_list = np.array([])
    n_list = np.array([])

    for i in range(-1, len(limits)):
        if i == -1:
            previous_cdf = 0
        else:
            previous_cdf = stats.norm.cdf(limits[i])
        if i == len(limits) - 1:
            current_cdf = 1
        else:
            current_cdf = stats.norm.cdf(limits[i + 1])
        p_list = np.append(p_list, current_cdf - previous_cdf)

        if i == -1:
            n_list = np.append(n_list, len(arr[arr <= limits[0]]))
        elif i == len(limits) - 1:
            n_list = np.append(n_list, len(arr[arr >= limits[-1]]))
        else:
            n_list = np.append(n_list, len(arr[(arr <= limits[i + 1]) & (arr >= limits[i])]))

    return n_list, p_list


def build_table(n_list, p_list, size, limits):
    result = np.divide(np.multiply((n_list - size * p_list), (n_list - size * p_list)), p_list * size)
    rows = []
    headers = ["$i$", "$\\Delta_i = [a_{i-1}, a_i)$", "$n_i$", "$p_i$",
               "$np_i$", "$n_i - np_i$", "$(n_i - np_i)^2/np_i$"]

    for i in range(0, len(n_list)):
        if i == 0:
            boarders = ["-inf", np.around(limits[0], decimals=4)]
        elif i == len(n_list) - 1:
            boarders = [np.around(limits[-1], decimals=4), "inf"]
        else:
            boarders = [np.around(limits[i - 1], decimals=4), np.around(limits[i], decimals=4)]

        rows.append([i + 1, boarders, n_list[i], np.around(p_list[i], decimals=4),
                     np.around(p_list[i] * size, decimals=4), np.around(n_list[i] - size * p_list[i], decimals=4),
                     np.around(result[i], decimals=4)])

    rows.append(["\\sum", "--", np.sum(n_list), np.around(np.sum(p_list), decimals=4),
                 np.around(np.sum(p_list * size), decimals=4), np.around(np.sum(n_list - size * p_list), decimals=4),
                 np.around(np.sum(result), decimals=4)])

    file.write(tabulate(rows, headers))


def run(arr, size):
    k = find_k(size)
    MLE(arr, k)
    limits = np.linspace(-1.1, 1.1, num=k - 1)
    n_list, p_list = find_n_and_p(arr, limits)
    build_table(n_list, p_list, size, limits)
