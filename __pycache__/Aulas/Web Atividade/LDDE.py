class No:

    def __init__(self,anterior,valor,proximo):
        self.ant = anterior
        self.info = valor
        self.prox = proximo

class Ldde:

    def __init__(self):
        self.prim = self.ult = None
        self.quant = 0

    def remover(self,valor): #Função de Remover
        if self.quant == 1:
            self.prim=self.ult= None
        else:
            aux = self.prim
            while aux.info != valor:
                aux = aux.prox
            aux.ant.prox= aux.prox
            aux.prox.ant= aux.ant
        self.quant -=1
    def inserir_inicio(self,valor): # Função somente para adicionar itens na lista para testes
        if self.quant == 0:
            self.prim = self.ult = No(None,valor,None)
        else:
            self.prim.ant = self.prim = No(None,valor,self.prim)
        self.quant+=1
    def show(self): # Função para mostrar a situação da lista
        aux = self.prim
        while aux!=None:
            print(aux.info,end=' ')
            aux = aux.prox
        print('/n')
    def insereAposDet(self,valor1,valor2): # Função de inserir valor após
        aux=self.prim
        while aux.info != valor2:
            aux=aux.prox
        aux.prox = No(aux,valor1,aux.prox)
        self.quant +=1