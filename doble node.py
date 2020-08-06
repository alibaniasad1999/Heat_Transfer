
# all are the same exept we dive r r1 and l to 2 and use in loop twice number
import numpy as np

r1 = 4 / 2 / 2
r = 4 / 2
l = 5 / 2
length = 1000
R = 200
K = 0.055 / 1000
h_air = 4.5 / 1000000
h_water = 890 / 1000000
T_air = 30
T_water = 20
w = 1 / 1000


# r function from x y z
def r_up_get(z):
    if z == 100:
        return 200
    return r1 + z * r


def area_side_get(z):
    if z == 0:
        return np.pi * (r_up_get(z) ** 2)
    return np.pi * (r_up_get(z) ** 2 - r_up_get(z - 1) ** 2) / 2


def area_up(z):
    return np.pi * r_up_get(z) * l


def area_down(z):
    if z == 0:
        return area_up(0)
    return np.pi * r_up_get(z - 1) * l


def index2z(j):
    if j == 100:
        return 0
    elif j > 100:
        return j - 100
    else:
        return 100 - j


a = np.zeros((401, 201))
for i in range(401):
    for j in range(201):
        if i == 0:
            a[i, j] = 40
        else:
            a[i, j] = 40
n = int(input())
f = open("final center for 100 wat node 40 double.txt", "w")
for k in range(n):
    print(k)
    for i in range(1, 400):
        for j in range(201):
            if j == 0:
                a[i][j] = (area_up(index2z(j)) * h_water * T_water + K * (a[i][j + 1] * (
                    area_down(index2z(j))) / r + area_side_get(index2z(j)) / l * (a[i - 1][j] + a[i + 1][j]))) / (
                                  area_up(index2z(j)) * h_water + K * (
                                   area_down(index2z(j)) / r + 2 * area_side_get(index2z(j)) / l))
            elif j == 200:
                a[i][j] = (area_up(index2z(j)) * h_air * T_air + K * (a[i][j - 1] * (
                    area_down(index2z(j))) / r + area_side_get(index2z(j)) / l * (a[i - 1][j] + a[i + 1][j]))) / (
                                  area_up(index2z(j)) * h_air + K * (
                                   area_down(index2z(j)) / r + 2 * area_side_get(index2z(j)) / l))
            elif 0 < j < 101:
                a[i][j] = (K / r * (area_down(index2z(j)) * a[i][j + 1] + area_up(index2z(j)) * a[i][j - 1]) + K / l * (
                        area_side_get(index2z(j))) * (a[i - 1][j] + a[i + 1][j])) / (
                                  K / r * (area_down(index2z(j)) + area_up(index2z(j))) + K / l * 2 * area_side_get(
                                 index2z(j)))
            else:
                a[i][j] = (K / r * (area_down(index2z(j)) * a[i][j - 1] + area_up(index2z(j)) * a[i][j + 1]) + K / l * (
                        area_side_get(index2z(j))) * (a[i - 1][j] + a[i + 1][j])) / (
                                  K / r * (area_down(index2z(j)) + area_up(index2z(j))) + K / l * 2 * area_side_get(
                               index2z(j)))
            # f.write(str(int((1000*a[i][j]))/1000))
            # f.write(' ')
        # f.write('///////////////')

    i = 400
    for j in range(201):
        if j == 0:
            a[i][j] = (area_up(index2z(j)) * h_water * T_water + K * (a[i][j+1] * (
                    area_down(index2z(j))) / r + area_side_get(index2z(j)) / l * (a[i - 1][j])) + w * area_side_get(
                index2z(j))) / (area_up(index2z(j)) * h_water + K * (
                               area_down(index2z(j)) / r + area_side_get(index2z(j)) / l))
        elif j == 200:
            a[i][j] = (area_up(index2z(j)) * h_air * T_air + K * (a[i][j-1] * (
                    area_down(index2z(j))) / r + area_side_get(index2z(j)) / l * (a[i - 1][j])) + w * area_side_get(
                 index2z(j))) / (area_up(index2z(j)) * h_air + K * (
                               area_down(index2z(j)) / r + area_side_get(index2z(j)) / l))
        elif 0 < j < 101:
            a[i][j] = (K / r * (area_down(index2z(j)) * a[i][j + 1] + area_up(index2z(j)) * a[i][j - 1]) + K / l * (
                    area_side_get(index2z(j))) * (a[i - 1][j]) + area_side_get(index2z(j)) * w) / (
                              K / r * (area_down(index2z(j)) + area_up(index2z(j))) + K / l * area_side_get(index2z(j)))
        else:
            a[i][j] = (K / r * (area_down(index2z(j)) * a[i][j - 1] + area_up(index2z(j)) * a[i][j + 1]) + K / l * (
                    area_side_get(index2z(j))) * (a[i - 1][j]) + area_side_get(index2z(j)) * w) / (
                              K / r * (area_down(index2z(j)) + area_up(index2z(j))) + K / l * area_side_get(index2z(j)))
for i in range(401):
    for j in range(201):
        f.write(str(int((1000*a[i][j]))/1000))
        f.write(' ')
    f.write('\n')
