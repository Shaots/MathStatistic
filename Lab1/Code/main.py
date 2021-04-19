from pathlib import Path
from Lab1.Code.distribution import distribution


def main():
    Directoy = Path("../result")
    size = [10, 50, 1000]
    distr = ["Normal", "Cauchy", "Laplace", "Poisson", "Uniform"]
    for i in distr:
        for j in size:
            obj = distribution(i, j)
            Path(Directoy / i).mkdir(parents=True, exist_ok=True)
            obj.build(Directoy / i / f"size_{j}.png")