from Lab3.Code.distribution3 import distribution

def main():
    distr = ["Normal", "Cauchy", "Laplace", "Poisson", "Uniform"]
    size = [20, 100]
    share = []
    for i in range(len(distr)):
        obj = distribution(distr[i])
        obj.draw_boxplot()
        share.append(obj.emission_share())
    with open("../result/Emission_share.txt", "w") as f:
        for i in range(len(distr)):
            for j in range(len(size)):
                f.write(distr[i] + "    size = " + str(size[j]) + "    emission_share = " + str(share[i][j]) + "\n")
        f.close()
