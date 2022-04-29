from claseConjunto import Conjunto

class Menu:
    __opcion = 0

    def __init__(self, op = 0):
        self.__opcion = op


    def MostrarMenu(self, unConjunto, otroConjunto):
        if type(unConjunto) == Conjunto and type(otroConjunto) == Conjunto:
            print(' === MENU ===')
            cerrar = False
            while not cerrar:
                print('\n')
                print('a- Unir los dos conjuntos')
                print('b- Difereciar los dos conjuntos')
                print('c- Verificar si son igaules')  
                print('d- Salir')

                self.__opcion = input('Seleccione una opcion: ') 

                if self.__opcion.lower() == 'a':
                    self.EjecutarA(unConjunto, otroConjunto)

                elif self.__opcion.lower() == 'b':
                    self.EjecutarB(unConjunto, otroConjunto)

                elif self.__opcion.lower() == 'c':
                    self.EjecutarC(unConjunto, otroConjunto)

                elif self.__opcion.lower() == 'd':
                    cerrar = True
                    print('Cerrando Menu...')
                else:
                    print('Opcion ingresada invalida')
                    input('Presione ENTER para continuar...')

    def EjecutarA(self, unConjunto, otroConjunto):
        print(' === Union de dos conjuntos ===')
        resultante = unConjunto + otroConjunto
        print(resultante)  

    def EjecutarB(self, unConjunto, otroConjunto):
        print(' === Diferecia de dos conjuntos ===')
        resultante = unConjunto - otroConjunto
        print(resultante)   

    def EjecutarC(self, unConjunto, otroConjunto):
        if unConjunto == otroConjunto:
            print('Los conjuntos {} y {} son iguales' .format(unConjunto.getNombre(), otroConjunto.getNombre()))
        else:
            print('Los conjuntos {} y {} son distintos' .format(unConjunto.getNombre(), otroConjunto.getNombre()))
                





                     