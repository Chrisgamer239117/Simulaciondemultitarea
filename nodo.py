from random import randint
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.__duracion=randint(4, 9)
        self.siguiente=None

    def getDuracion(self):
            return self.__duracion

    def descontar(self):
        self.__duracion -=1