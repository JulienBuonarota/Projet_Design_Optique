import numpy as np

def matrice_rotation(alpha, beta, gamma):
    Rgamma = np.array([[np.cos(gamma), -np.sin(gamma), 0],
                       [np.sin(gamma), np.cos(gamma), 0],
                       [0, 0, 1]]).reshape((3, 3))
    Rbeta = np.array([[1, 0, 0],
                      [0, np.cos(beta), -np.sin(beta)],
                      [0, np.sin(beta), np.cos(beta)]]).reshape((3, 3))
    Ralpha = np.array([[np.cos(alpha), 0, -np.sin(alpha)],
                       [0, 1, 0],
                       [np.sin(alpha), 0, np.cos(alpha)]]).reshape((3, 3))
    return np.matmul(Rgamma, np.matmul(Rbeta, Ralpha))

def rayon_centroid(X, Y):
    Xm, Ym = [np.mean(X), np.mean(Y)]
    rayon = np.mean(np.sqrt((X-Xm)**2 + (Y-Ym)**2))
    return rayon
    
def math1(x):
    return x