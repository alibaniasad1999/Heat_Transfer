import numpy as np

r1 = 4 / 2
r = 4
l = 5
length = 1000
R = 200
K = 0.055 / 1000
h_air = 4.5 / 1000000
h_water = 890 / 1000000
T_air = 30
T_water = 20
w = 0.1 / 1000


# r function from x y z
def r_up_get(z):
    if z == 50:
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
    if j == 50:
        return 0
    elif j > 50:
        return j - 50
    else:
        return 50 - j
f = open("radius.txt", "w")
for j in range(101):
    f.write(str(area_side_get(index2z(j))))
    f.write(' ')