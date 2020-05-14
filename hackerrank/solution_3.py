# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
import pandas as pd
from statsmodels.tsa.arima_model import ARIMA


def getTrainData():
    data = []
    N = int(input())
    for i in range(N):
        line = [x for x in input().split("\t")]
        data.append(int(line[1]))

    ts = pd.Series(data)
    ts.reset_index(drop=True, inplace=True)
    return ts, N


def main():
    ts, N = getTrainData()
    model = ARIMA(ts, order=(1, 1, 0))
    model_fit = model.fit(disp=0)
    # print(model_fit.summary())
    # residuals = pd.DataFrame(model_fit.resid)
    # residuals.plot()
    # plt.show()
    # residuals.plot(kind='kde')
    # plt.show()
    # print(residuals.describe())
    preds = model_fit.predict(N, N + 11)
    for val in preds:
        print(val)


if __name__ == "__main__":
    main()
