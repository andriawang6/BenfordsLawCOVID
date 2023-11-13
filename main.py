import pandas as pd

us_data = pd.read_csv("USDeaths.csv", header=0)
us_deaths = []
for i in range(len(us_data)):
    us_deaths.append(us_data["New_deaths"][i])

china_data = pd.read_csv("ChinaDeaths.csv", header=0)
china_deaths = []
for i in range(len(china_data)):
    china_deaths.append(china_data["New_deaths"][i])


def count_digits(dataset):
    digits = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(len(dataset)):
        leading_digit = int(str(dataset[i])[0])
        digits[leading_digit] += 1
    return digits


def probability(dataset):
    digits = count_digits(dataset)
    digits.pop(0)
    data_sum = 0
    for i in range(len(digits)):
        data_sum += digits[i]
    for i in range(len(digits)):
        digits[i] /= data_sum
    return digits


import math


def regression_line(x):
    return math.log((x + 1) / x, 10)


def reg_data():
    reg = []
    for i in range(1, 10):
        reg.append(regression_line(i))
    return reg


def r_squared(dataset):
    digits = probability(dataset)
    reg = reg_data()
    ssr = 0
    for i in range(len(digits)):
        ssr += (digits[i] - reg[i]) ** 2
    sst = 0
    avg = sum(digits) / len(digits)
    for i in range(len(digits)):
        sst += (digits[i] - avg) ** 2

    return 1 - (ssr / sst)


print(count_digits(us_deaths))
print(probability(us_deaths))
print(r_squared(us_deaths))

print(count_digits(china_deaths))
print(probability(china_deaths))
print(r_squared(china_deaths))
