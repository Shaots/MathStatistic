import _io
import csv
from Lab2.Code.distribution2 import distribution


def myPrintTable2D(file: _io.TextIOWrapper, table: list):
    for i in range(len(table)):
        if i % 4 == 2:
            for j in range(len(table[i])):
                file.write("[%.3f,%.3f]     " % (table[i][j], table[i + 1][j]))
        else:
            if i % 4 != 3:
                for j in range(len(table[i])):
                    file.write("%f    " % table[i][j])
        file.write("\n")


def main():
    distr = ["Normal", "Cauchy", "Laplace", "Poisson", "Uniform"]
    nameFile = ["Normal.txt", "Cauchy.txt", "Laplace.txt", "Poisson.txt", "Uniform.txt"]
    for i in range(len(distr)):
        obj = distribution(distr[i])
        table = obj.build_table()
        file = open("../result" + nameFile[i], "w")
        myPrintTable2D(file, table)
        file.close()
