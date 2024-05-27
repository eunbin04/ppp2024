import matplotlib.pyplot as plt
import numpy as np

def main():
    np.random.seed(0)

    n = 50
    x = np.random.rand(n)
    y = np.random.rand(n)

    plt.scatter(x, y)
    plt.savefig("./lec15/scatter.png")

if __name__ == "__main__":
    main()
