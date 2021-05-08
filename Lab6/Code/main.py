from Lab6.Code.distribution6 import *

def main():

    x = np.linspace(-1.8, 2, 20)
    y = standard_with_error(x)
    build_graphic(x, y, "Распределение без возмущения")
    y[0] += 10
    y[-1] -= 10
    build_graphic(x, y, "Распределение с возмущением")
