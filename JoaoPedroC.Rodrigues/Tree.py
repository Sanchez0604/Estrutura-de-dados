class Tree:

    def __init__(self):
        self.raiz = None

    def insere(self, valor):    
        if self.raiz == None:
            self.raiz = No(valor)
        else:
            self.raiz.insere(valor)
       
    def somaFolhas(self,valor):    
        if self.raiz != None:
            return self.raiz.somaFolhas(valor)
    def somaNoFolhas(self):
        if self.raiz != None:
            return self.raiz.somaNoFolhas(self)
        
    def printFolhas(self):
        if self.raiz != None:
            self.raiz.printFolhas()

    def imprimirFolhas(self,valor):
        if self.raiz != None:
            return self.raiz.imprimirFolhas(valor)
    
    def printCaminho(self,valor):
        if self.raiz != None:
            return self.raiz.printCaminho(valor)



class No:

    def __init__(self, valor):
        self.info = valor
        self.esq = None
        self.dir = None

    def insere(self, valor):
        if valor < self.info:
            if self.esq == None:
                self.esq = No(valor)
            else:
                self.esq.insere(valor)
        else:
            if self.dir == None:
                self.dir = No(valor)
            else:
                self.dir.insere(valor)
    
    

    def somaNoFolhas(self):
        total=0
        if self.esq == None and self.dir == None:
            total += self.info
        if self.esq != None:
            total += self.esq.somaNoFolhas()
        if self.dir != None:
            total += self.dir.somaNoFolhas()
        return total
    
    def somaFolhas(self, valor):
        soma=0
        if valor == self.info:
            return print(self.somaNoFolhas())
        elif valor < self.info:
            self.esq.somaFolhas(valor)
        else:
            self.dir.somaFolhas(valor)
    
    def printFolhas(self):
        if self.esq != None:
            self.esq.printFolhas()
        if self.esq == None and self.dir == None:
            print(self.info,end=" ")    
        if self.dir != None:
            self.dir.printFolhas()

    def imprimirFolhas(self,valor):
        if valor == self.info:
            return self.printFolhas()
        elif valor < self.info:
            self.esq.imprimirFolhas(valor)
        else:
            self.dir.imprimirFolhas(valor)

    def printCaminho(self,valor):
        if valor == self.info:
            return (self.info)
        elif valor < self.info:
            print(self.info,self.esq.info)
            self.esq.imprimirFolhas(valor)
        elif valor > self.info:
            print(self.info,self.dir.info)
            self.dir.imprimirFolhas(valor)
            
