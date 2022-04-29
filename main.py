from claseConjunto import Conjunto
from claseMenu import Menu

def test():
    print('Iniciando test...')
    unConjunto = Conjunto()
    otroConjunto = Conjunto()
    unConjunto.agregarNumero(1)
    unConjunto.agregarNumero(2)
    unConjunto.agregarNumero(3)
    otroConjunto.agregarNumero(3)
    otroConjunto.agregarNumero(6)
    otroConjunto.agregarNumero(7)
    if unConjunto == otroConjunto:
        print('Iguales')
    else:
        print('Distintos')    

    unConjunto = unConjunto + otroConjunto
    print(unConjunto)
    unConjunto = unConjunto - otroConjunto
    print(unConjunto)
    print('Cerrando test...\n\n')

if __name__ == '__main__':
    test()
    objetoMenu = Menu()
    nombre = input('Ingrese el nombre del primer conjunto: ')
    longuitud = int(input('Ingrese la longuitud del primer conjunto: '))
    Conjunto1 = Conjunto(nombre)
    i = 0
    j = 0
    while i < longuitud:
        numero = int(input('Ingrese un elemento: '))
        Conjunto1.agregarNumero(numero)
        i+=1

    print(Conjunto1)    
    nombre = input('Ingrese el nombre del segundo conjunto: ')
    longuitud = int(input('Ingrese la longuitud del segundo conjunto: '))
    Conjunto2 = Conjunto(nombre)

    while j < longuitud:
        numero = int(input('Ingrese un elemento: '))
        Conjunto2.agregarNumero(numero)
        j+=1

    print(Conjunto2)    
    objetoMenu.MostrarMenu(Conjunto1, Conjunto2)    





  