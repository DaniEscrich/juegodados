import random


class Dado:
    __caras = 6

    def __init__(self, fcaras):
        """
        Constructor de la clase Dado
        :param fcaras: int
        """
        self.setCaras(fcaras)

    def lanzar(self):
        """
        Funcion que lanzza automatic
        :return: int
        """
        return random.randint(1, self.__caras)

    def getCaras(self):
        """
        Devuelve las caras
        :return: int
        """
        return self.__caras

    def setCaras(self, fcaras):
        """
        Establece las caras
        :param fcaras: int
        :return: int
        """
        caras_permitidas = [4, 6, 8, 10, 12, 20, 120,200,300]
        if fcaras in caras_permitidas:
            self.__caras = fcaras
        else:
            raise Exception("Numero de caras incorrecto")
