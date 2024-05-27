import matplotlib.pyplot as plt
import numpy as np

def main():
    tmax = np.random.rand(30) * 15 + 15
    tmin = tmax - (np.random.rand(30) * 5 + 5)

    plt.rcParams['font.family'] = ['NanumGothic', 'sans-serif']
    plt.rcParams['axes.unicode_minus'] = False

    plt.plot(tmax, color="r", label="최고기온")
    plt.plot(tmin, color="b", label="최저기온")

    plt.ylabel("Temperature(℃)")
    
    plt.legend()
    plt.savefig("./lec15/linegraph_korean.png")

if __name__ == "__main__":
    main()
