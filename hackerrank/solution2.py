import numpy as np

N = int(input())
data = []
temp = []
for i in range(N):
    data.append(input().split())
    temp.append(float(data[i][1]))


print(data)

print(temp)

from scipy import interpolate

leng = list(range(len((temp))))
interpolation = interpolate.interp1d(leng, temp, fill_value="extrapolate")

y = interpolation(range(len(temp), len(temp) + 12))

for x in y:
    print(x)
