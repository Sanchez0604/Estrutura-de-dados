class Tree:

    def __init__(self):
        self.raiz = None

    def insere(self, valor):
        if self.raiz == None:
            self.raiz = No(valor)
        else:
            self.raiz.insere(valor)

    def inOrdem(self):
        if self.raiz != None:
            self.raiz.inOrdem()
    
    def preOrdem(self):
        if self.raiz != None:
            self.raiz.preOrdem()
    
    def posOrdem(self):
        if self.raiz != None:
            self.raiz.posOrdem()
    
    def printFolhas(self):
        if self.raiz != None:
            self.raiz.printFolhas()
    
    def busca(self, valor):
        if self.raiz == None:
            return False
        else:
            return self.raiz.busca(valor)
    
    def soma(self):
        if self.raiz != None:
            return self.raiz.soma()
    
    def somaFolhas(self):
        if self.raiz != None:
            return self.raiz.somaFolhas()
class No:

    def __init__(self, valor):
        self.info = valor
        self.esq = None
        self.dir = None
    
    def insere(self, valor):

        if valor < self.info:
            if self.esq == None:
                self.esq = No(valor)
                print('*')
            else:
                self.esq.insere(valor)
                print('+')

        else:
            if self.dir == None:
                self.dir = No(valor)
                print('-')
            else:
                self.dir.insere(valor)
                print('#')
    
    def inOrdem(self):
        if self.esq != None:
            self.esq.inOrdem()
        print(self.info,end=" ")
        if self.dir != None:
            self.dir.inOrdem()
    
    def preOrdem(self):

        print(self.info,end=" ")
        if self.esq != None:
            self.esq.preOrdem()
        if self.dir != None:
            self.dir.preOrdem()
    
    def posOrdem(self):
            
        if self.esq != None:
            self.esq.posOrdem()
        if self.dir != None:
            self.dir.posOrdem()
        print(self.info,end=" ")
    
    def qualOrdem(self):

        if self.dir != None:
            self.dir.qualOrdem()
        print(self.info,end=" ")
        if self.esq != None:
            self.esq.qualOrdem()
    
    def printFolhas(self):
        if self.esq != None:
            self.esq.printFolhas()
        if self.esq == None and self.dir == None:
            print(self.info,end=" ")    
        if self.dir != None:
            self.dir.printFolhas()
    
    def busca(self, valor):
        if valor == self.info:
            return True
        elif valor < self.info:
            if self.esq == None:
                return False
            else:
                return self.esq.busca(valor)
        else:
            if self.dir == None:
                return False
            else:
                return self.dir.busca(valor)
    
    def soma(self):
        total = self.info
        if self.esq != None:
            total += self.esq.soma()
        if self.dir != None:
            total += self.dir.soma()
        return total
    
    def somaFolhas(self):
        total = 0
        if self.esq==None and self.dir == None:
            total = self.info
        if self.esq != None:
            total += self.esq.somaFolhas()
        if self.dir != None:
            total += self.dir.somaFolhas()
        return total