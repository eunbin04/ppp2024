import pandas as pd

def main():
    df = pd.read_csv("./lec17/weather_146_2020-2020.csv")
    print(df.columns)
    print(df[df[' month'] == 8][" tavg"].mean())
    ax=df[" tavg"].plot()
    ax.figure.savefig("./lec17/pandas_tavg.png")
    print(df)

if __name__=="__main__":
    main()