import matplotlib.pyplot as plt
import numpy as np

# with open("data_pickel", "rb") as file:
#    data = pickel.load(file)

# theta = np.linspace(np.pi / 2, 3 * np.pi / 2, 150)
#
# R = 1
#
# a = R * np.cos(theta) + 1
# b = R * np.sin(theta) + 2
#
# figure, axes = plt.subplots()
#
# # trace de la droite
# xl = np.array([0, 0])
# yl = np.array([-1, 1])
#
# # plot des 2
# plt.plot(a, b, xl, yl)
# plt.axis("equal")
# plt.grid()
# plt.show()

##
# TODO faire fonction
# TODO intersection concave et convexe
# TODO lecture fichier CSV
import numpy as np

def arc_de_cercle(R, repere, angles):
    #Calcule un cercle à partir d'un rayon R, d'un repère (x0, y0, z0) et d'angles

    import matplotlib.pyplot as plt

    # from math import *

    # R = 1
    # x0 = 0
    # y0 = 1
    # z0 = 2
    ##
    x0, y0, z0 = repere
    z = np.linspace(0, 3, 150)

    if R > 0:
        yp = np.sqrt(R ** 2 - (z - R) ** 2)
        yn = -np.sqrt(R ** 2 - (z - R) ** 2)
    else:
        yp = np.sqrt(R ** 2 - (z + R) ** 2)
        yn = -np.sqrt(R ** 2 - (z + R) ** 2)

    # zd = z + z0
    ypd = yp + y0
    ynd = yn + y0

    ytot = np.concatenate((np.flip(ypd), ynd))
    if R < 0:
        ztot = np.concatenate((-np.flip(z), -z))
    else:
        ztot = np.concatenate((np.flip(z), z))
    ##
    return ztot + z0, ytot

#plt.plot(ztot, ytot)
#plt.plot(zd, ynd, color='k')
#plt.plot(zd, ypd, color='k')
#plt.axis("equal")
#plt.grid()
#plt.show()

##
arc1_z, arc1_y = arc_de_cercle(2, (0,0,2), (0,0,0))
arc2_z, arc2_y = arc_de_cercle(-4, (0,0,4), (0,0,0))

plt.plot(arc1_z, arc1_y, arc2_z, arc2_y)
plt.axis("equal")
plt.grid()
plt.show()

delta = (4 * (ytot2 - ytot1))**2 - 4 * ((2 * (ytot2 - ytot1))**2 + (2 * (ztot2 - ztot1))**2)((ytot2 - ytot1)**2 + (ztot2 - ztot1)**2 - R2**2 + R1**2)
y1 = ytot1 + (4 * (ytot2 - ytot1) * ((ytot2 - ytot1)**2 + (ztot2 - ztot1)**2 - R2**2 + R1**2) - sqrt(delta))/(2 * (2 * (ytot2 - ytot1))**2 + (2 * (ztot2 - ztot1))**2)
y2 = ytot1 + (4 * (ytot2 - ytot1) * ((ytot2 - ytot1)**2 + (ztot2 - ztot1)**2 - R2**2 + R1**2) + sqrt(delta))/(2 * (2 * (ytot2 - ytot1))**2 + (2 * (ztot2 - ztot1))**2)

z1 = ztot1 + (((ytot2 - ytot1)**2 + (ztot2 - ztot1)**2 - R2**2 + R1**2) - 2 * (ytot2 - ytot1) * (ytot1 - y1))/(2 * (ztot2 - ztot1))
z2 = ztot1 + (((ytot2 - ytot1)**2 + (ztot2 - ztot1)**2 - R2**2 + R1**2) - 2 * (ytot2 - ytot1) * (ytot1 - y2))/(2 * (ztot2 - ztot1))



