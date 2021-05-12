from Lab7.Code.distribution7 import *
from scipy.stats import laplace, uniform


def main():
    file.write("Normal distribution\n")
    run(np.random.normal(0, 1, size=100), 100)
    file.write("\n\nLaplace distribution\n")
    run(laplace.rvs(size=20, scale=1 / math.sqrt(2), loc=0), 20)
    file.write("\n\nUniform distribution\n")
    run(uniform.rvs(size=20, loc=-math.sqrt(3), scale=2 * math.sqrt(3)), 20)
