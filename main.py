import numpy as np
r1 = 4/2
r = 4
l = 5
length = 1000
R = 200
K = 0.0339/1000
h_air = 4.5/1000000
h_water = 890/1000000
T_air = 30
T_water = 20
#r function from x y z
def r_Up_get(z):
    if z == 50:
        return 200
    return r1+z*r
def A_side_get(z):
    if z == 0:
        return np.pi*(r_Up_get(z)**2)
    return np.pi*(r_Up_get(z)**2-r_Up_get(z-1)**2)/2
def A_Up(z):
    return np.pi*r_Up_get(z)*l
def A_Down(z):
    if z == 0:
        return 2*r1*l
    return np.pi*r_Up_get(z-1)*l
Coefficient = np.zeros((201*101,201*101))
def indexer(x, y, z):
    if y == 2:
        return (50-z)*201+x
    return (50+z)*201+x
eqNum = 0
a = np.zeros((201*101))
# first boundry condition
Coefficient[eqNum][indexer(0,0,0)] = 1
a[eqNum] = 40
eqNum = eqNum + 1
for i in range(1, 3):
    for j in range(1, 51):
        Coefficient[eqNum][indexer(0,i,j)] = 1
        a[eqNum] = 40
        eqNum = eqNum + 1
# eq for evry unnow node
for i in range(1, 200):
    # vasat
    Coefficient[eqNum][indexer(i - 1, 0, 0)] = K * A_side_get(0) / l
    Coefficient[eqNum][indexer(i + 1, 0, 0)] = K * A_side_get(0) / l
    Coefficient[eqNum][indexer(i, 1, 1)] = K * A_Down(0) / r
    Coefficient[eqNum][indexer(i, 2, 1)] = K * A_Down(0) / r
    Coefficient[eqNum][indexer(i, 0, 0)] = -2 * K * A_side_get(0) / l - 2 *K * A_Down(0) / r
    eqNum = eqNum + 1
    for j in range(1, 3):
        for k in range(1,51):
            if k == 50:
                Coefficient[eqNum][indexer(i-1, j, k)] = K*A_side_get(k)/l
                Coefficient[eqNum][indexer(i+1, j, k)] = K*A_side_get(k)/l
                Coefficient[eqNum][indexer(i, j, k-1)] = K*A_Down(k)/r
                # air
                if j == 1:
                    Coefficient[eqNum][indexer(i, j, k)] = -2 * K * A_side_get(k)/l  - K*A_Down(k)/r-h_air*A_Up(k)
                    a[eqNum] = -h_air*A_Up(k)*T_air
                    eqNum = eqNum +1
                else:
                    Coefficient[eqNum][indexer(i, j, k)] = -2 * K * A_side_get(k) / l - h_water * A_Up(k)
                    a[eqNum] = -h_air*A_Up(k)*T_water
            else:
                Coefficient[eqNum][indexer(i-1, j, k)] = K*A_side_get(k)/l
                Coefficient[eqNum][indexer(i+1, j, k)] = K*A_side_get(k)/l
                Coefficient[eqNum][indexer(i, j, k-1)] = K*A_Down(k)/r
                Coefficient[eqNum][indexer(i, j, k+1)] = K*A_Down(k)/r
                Coefficient[eqNum][indexer(i, j, k)] = -2*K*A_side_get(k)/l - K*A_Down(k)/r - K*A_Up(k)/r
                eqNum = eqNum + 1
# for heat coming
for j in range(1, 3)
    for k in range(1:50)














