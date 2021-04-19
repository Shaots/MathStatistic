import _io
from Lab2.Code.distribution import distribution


def myPrintTable2D(file: _io.TextIOWrapper, tableE: list, tableD: list, name: str):
    file.write(name + "\n")
    file.write("                   Mean    Median    Zr    Zq    Ztr\n")
    for i in range(len(tableE)):
        file.write("E(z): n = 10^%d    " % (i + 1))
        for j in range(len(tableE[i])):
            file.write("%.2f    " % tableE[i][j])
        file.write("\n")
        file.write("D(z): n = 10^%d    " % (i + 1))
        for j in range(len(tableD[i])):
            file.write("%.2f    " % tableD[i][j])
        file.write("\n")


def main():
    distr = ["Normal", "Cauchy", "Laplace", "Poisson", "Uniform"]
    nameFileE = ["NormalE.txt", "CauchyE.txt", "LaplaceE.txt", "PoissonE.txt", "UniformE.txt"]
    nameFileD = ["NormalD.txt", "CauchyD.txt", "LaplaceD.txt", "PoissonD.txt", "UniformD.txt"]
    for i in range(len(distr)):
        obj = distribution(distr[i])
        tableE, tableD = obj.build_table()
        file = open("../result" + nameFileE[i], "w")
        myPrintTable2D(file, tableE, tableD, distr[i])
        file.close()
