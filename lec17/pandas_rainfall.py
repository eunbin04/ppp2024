import pandas as pd

def main():
    df = pd.read_csv("./lec17/weather_146_2020-2020.csv")
    print(df[df[' month'] == 8][" tavg"].mean())
    ax=df[df[" rainfall"]>10][" rainfall"].plot.bar()
    ax.figure.savefig("./lec17/pandas_rainfall.png")

if __name__=="__main__":
    main()