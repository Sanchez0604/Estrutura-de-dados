class No:
    def __init__(self, valor, proximo):
        self.info = valor
        self.prox = proximo
class Ldse:
    def __init__(self):
        self.prim = self.ult = None
        self.quant = 0
    def remove_posicao(self,posicao):
        if self.quant==1:
            self.prim=self.ult=None
        else:
            aux= self.prim
            while aux.prox!= posicao:
                aux= aux.prox
            aux.prox=aux.prox.prox
        self.quant-=1
    def inserir_inicio(self,valor):
        if self.quant == 0:
            self.prim = self.ult = No(valor,None)
        else:
            self.prim = No(valor,self.prim)
        self.quant+=1
    def show(self):
        aux = self.prim
        while aux != None:
            print(aux.info, end=' ')
            aux = aux.prox
            print('\n')
    def inserir_fim(self,valor):
        if self.quant == 0:
            self.prim = self.ult = No(valor,None)
        else:
            self.ult.prox = self.ult = No(valor,None)
        self.quant+=1