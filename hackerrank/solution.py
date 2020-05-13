
import pandas as pd
from statsmodels.tsa.statespace.sarimax import SARIMAX
from sklearn.linear_model import LinearRegression

test = []
for i in range(int(input())):
    inp = input().split()
    test.append(int(inp[1]))

test = pd.DataFrame(test, columns = ['A'])
#model = SARIMAX(test, order = (1,1,2), seasonal_order = (0,0,0,12), trend = 'ct')
#model_fit = model.fit(disp=0)

def ones(pos):
    res = [0 for x in range(0,11)]
    if pos != 12:
        res[pos%12-1] = 1
    return res

t = []
for i in range(len(test['A'])):
    a = ones(i)
    # print(i, '  ', a)
    t.append(a)
# print(t)
t = pd.DataFrame(t, columns=['Month1', 'Month2', 'Month3', 'Month4', 'Month5', 'Month6', 'Month7', 'Month8', 'Month9', 'Month10', 'Month11'])

# print(test.head())

test = test.join(t)

# print(test.iloc[:,:3].head())

model = LinearRegression()

# print(test.iloc[:, 1:12],'break', test.iloc[:, 1])
model.fit(test.iloc[:, 1:12], test.iloc[:, 1])
output = model.predict(test.iloc[:12, 1:12])
# #print(prediction)
# print(output)

# #output = model_fit.forecast(12)

for i in output:
    print(i)