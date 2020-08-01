# import numpy as np
import numpy as np

r1 = 4 / 2
r = 4
l = 5
length = 1000
R = 200
K = 0.0339 / 1000
h_air = 4.5 / 1000000
h_water = 890 / 1000000
T_air = 30
T_water = 20
w = 200 / 1000


# r function from x y z
def r_Up_get(z):
    if z == 50:
        return 200
    return r1 + z * r


def A_side_get(z):
    if z == 0:
        return np.pi * (r_Up_get(z) ** 2)
    return np.pi * (r_Up_get(z) ** 2 - r_Up_get(z - 1) ** 2) / 2


def A_Up(z):
    return np.pi * r_Up_get(z) * l


def A_Down(z):
    if z == 0:
        return 2 * r1 * l
    return np.pi * r_Up_get(z - 1) * l


def index2z(j):
    if j == 50:
        return 0
    elif j > 50:
        return j - 50
    else:
        return 50 - j


a = np.zeros((201, 101))
for i in range(201):
    for j in range(101):
        a[i, j] = 30
n = int(input())
for k in range(n):
    for i in range(1, 200):
        for j in range(101):
            if j == 0:
                a[i][j] = ((2 * K * A_side_get(index2z(j)) / l) * (a[i + 1][j] + a[i - 1][j]) + h_water * A_Up(
                    index2z(j)) * T_water + A_Down(index2z(j)) * K * a[i][j + 1]) / (
                                  2 * K * A_side_get(index2z(j)) / l + K * A_Down(index2z(j)) / l + A_Up(
                              index2z(j)) * h_water)
            elif j == 100:
                a[i][j] = ((2 * K * A_side_get(index2z(j)) / l) * (a[i + 1][j] + a[i - 1][j]) + h_air * A_Up(
                    index2z(j)) * T_air + A_Down(index2z(j)) * K * a[i][j - 1]) / (
                                  2 * K * A_side_get(index2z(j)) / l + K * A_Down(index2z(j)) / l + A_Up(
                              index2z(j)) * h_air)
            elif 0 < j < 51:
                (K / l * (2 * A_side_get(index2z(j)) * (a[i - 1][j] + a[i + 1][j]) + A_Down(index2z(j)) * a[i][
                    j + 1] + A_Up(
                    index2z(j) * a[i][j - 1]))) / (K / l * (2 * A_side_get(index2z(j))) + A_Down(index2z(j)) + A_Up(
                    index2z(j)))
            else:
                K / l * (2 * A_side_get(index2z(j)) * (a[i - 1][j] + a[i + 1][j]) + A_Down(index2z(j)) * a[i][
                    j - 1] + A_Up(
                    index2z(j) * a[i][j + 1])) / (K / l * (2 * A_side_get(index2z(j))) + A_Down(index2z(j)) + A_Up(
                    index2z(j)))
    i = 200
    for j in range(101):
        if j == 0:
            a[i][j] = ((K * A_side_get(index2z(j)) / l) * (a[i - 1][j]) + h_water * A_Up(
                index2z(j)) * T_water + A_Down(index2z(j)) * K * a[i][j + 1] + A_side_get(index2z(j)) * w) / (
                              K * A_side_get(index2z(j)) / l + K * A_Down(index2z(j)) / l + A_Up(
                          index2z(j)) * h_water)
        elif j == 100:
            a[i][j] = ((K * A_side_get(index2z(j)) / l) * (a[i - 1][j]) + h_air * A_Up(
                index2z(j)) * T_air + A_Down(index2z(j)) * K * a[i][j - 1] + A_side_get(index2z(j)) * w) / (
                              K * A_side_get(index2z(j)) / l + K * A_Down(index2z(j)) / l + A_Up(
                          index2z(j)) * h_air)
        elif 0 < j < 51:
            (K / l * (A_side_get(index2z(j)) * (a[i - 1][j]) + A_Down(index2z(j)) * a[i][j + 1] + A_Up(
                index2z(j) * a[i][j - 1])) + A_side_get(index2z(j)) * w) / (
                    K / l * (A_side_get(index2z(j))) + k*A_Down(index2z(j))/r + A_Up(
                index2z(j))*K/r)
        else:
            (K / l * (A_side_get(index2z(j)) * (a[i - 1][j]) + A_Down(index2z(j)) * a[i][j - 1] + A_Up(
                index2z(j) * a[i][j + 1])) + A_side_get(index2z(j)) * w) / (
                    K / l * (2 * A_side_get(index2z(j))) + A_Down(index2z(j)) + A_Up(
                index2z(j)))
f = open("final senter.txt", "w")
for i in range(201):
    print(i,(a[i][50]))
