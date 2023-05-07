from abc import ABC
import kmean
import Algorithm

class AlgorithmFactory(Algorithm.Algorithm):
    @staticmethod
    def create(algorithmname):
        if algorithmname == 'kmean':
            curr_algorithm = kmean.kmean()
            return curr_algorithm

    def calculate(up, Ks, coords):
        pass