from Lab4.Code.distribution4 import distribution

def main():
    distr = ["Normal", "Cauchy", "Laplace", "Poisson", "Uniform"]
    for i in range(len(distr)):
        obj = distribution(distr[i])
        obj.draw_empirical()
        obj.draw_kernel()
