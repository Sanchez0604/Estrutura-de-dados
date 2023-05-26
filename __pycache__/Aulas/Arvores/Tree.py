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