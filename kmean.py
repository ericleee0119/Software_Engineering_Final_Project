import numpy as np
from Algorithm import Algorithm
from sklearn.cluster import KMeans

class kmean(Algorithm):
    def __init__(self):
        pass
    def(self, up, Ks, coords):
        kmean = [KMeans(n_clusters=i).fit(coords) for i in Ks]
        return kmean