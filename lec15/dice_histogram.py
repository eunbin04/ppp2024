import matplotlib.pyplot as plt
import numpy as np

def main():
    dices = np.random.randint(1, 7, size=500) #size는 몇 번 던지나

    print(dices)

    plt.hist(dices, bins=6, color="lightgreen")
    plt.show()

    plt.savefig("./lec15/histogram.png")

if __name__ == "__main__":
    main()
