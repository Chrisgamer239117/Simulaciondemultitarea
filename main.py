from random import randint
from nodo import Nodo
from Lista_circular import ListaCircular
lista = ListaCircular()

for i in range(0, 300):
    lista.AgregarInicio(randint(4, 9))
    if (randint(1, 100) <= 25):
        print(f'Se creo un proceso en el ciclo {i}')
        lista.Recorrer()
        lista.AgregarFinal(randint(4, 9))

    print('Se termino el proceso en el ciclo ' + str(i))