class Conjunto:
    __nombre = None
    __lista = []

    def __init__(self, nombre = 'A'):
        self.__lista = []
        self.__nombre = nombre

    def agregarNumero(self, unNumero):
        if type(unNumero) == int:
            if unNumero not in self.getConjunto():
                self.__lista.append(unNumero)    

    def getTamanoLista(self):
        return len(self.__lista)      

    def getConjunto(self):
        return self.__lista       

    def getNombre(self):
        return self.__nombre      
   
    def __str__(self):
        s = '{} = ' .format(self.getNombre()) + '{'
        for i in range(len(self.__lista)):
            if i == len(self.__lista)-1:
                s+= str(self.__lista[i])
            else:
                s += str(self.__lista[i]) +','
        s+= '}' 
        return s   

    def __add__(self, otroConjunto):
        if type(otroConjunto) == Conjunto:
            nombe_nuevo = self.getNombre() + ' + ' + otroConjunto.getNombre()
            nuevo = Conjunto(nombe_nuevo)

            for k in range((self.getTamanoLista()) + (otroConjunto.getTamanoLista())): 
                if k < self.getTamanoLista(): 
                    nuevo.agregarNumero(self.__lista[k])
                else:
                    nuevo.agregarNumero(otroConjunto.__lista[k-self.getTamanoLista()])        
                
            return nuevo        

    def __sub__(self, otroConjunto):
        if type(otroConjunto) == Conjunto:
            nombe_nuevo = self.getNombre() + ' - ' + otroConjunto.getNombre()
            nuevo = Conjunto(nombe_nuevo)
            for i in range(self.getTamanoLista()):
                if self.__lista[i] not in otroConjunto.getConjunto():
                    nuevo.agregarNumero(self.__lista[i])
            return nuevo           

    def __eq__(self, otroConjunto):
        if type(otroConjunto) == Conjunto:
            condicion1 = False
            condicion2 = False
            contador = 0
            if self.getTamanoLista() == otroConjunto.getTamanoLista():
                condicion1 = True
            for i in range(self.getTamanoLista()):
                if self.__lista[i] in otroConjunto.getConjunto():
                    contador+=1
            if contador == i+1:
                condicion2 = True

            if condicion1 and condicion2:
                return True
            else:
                return False        

if __name__ == '__main__':
    unConjunto = Conjunto()
    unConjunto.agregarNumero(1)
    unConjunto.agregarNumero(2)
    unConjunto.agregarNumero(3)
    print(unConjunto)
    otroConjunto = Conjunto()
    otroConjunto.agregarNumero(1)
    otroConjunto.agregarNumero(2)
    otroConjunto.agregarNumero(4)
    print(otroConjunto)
    nuevo = unConjunto + otroConjunto
    print(nuevo)
    nuevo2 = unConjunto - otroConjunto
    print(nuevo2)
    if unConjunto == otroConjunto:
        print('iguales')
    else:
        print('distintos')    



