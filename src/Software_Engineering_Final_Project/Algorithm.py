import abc

class Algorithm(abc.ABC):

    
    @abc.abstractmethod
    def calculate(self, up, Ks, coords):
        pass