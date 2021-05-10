import numpy as np

def represente_rayon(origine, arrive="", direction=""):
    # de depart a arrive, return z et y
    x0, y0, z0 = origine
    if arrive is not "":
        x1, y1, z1 = arrive
    else:
        x1, y1, z1 = origine + 10*direction
    a = (y1 - y0) / (z1 - z0)
    b = y0 - a * z0
    z = np.linspace(z0, z1, 100)
    return (z, a*z + b)