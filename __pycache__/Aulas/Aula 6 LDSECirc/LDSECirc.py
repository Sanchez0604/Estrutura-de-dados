class No:
    def __init__(self, valor, proximo):
        self.info = valor
        self.prox = proximo
class Ldse:
    def __init__(self):
        self.prim = self.ult = None
        self.quant = 0
    def inserir_inicio(self,valor):
        if self.quant==0: #Verifica se a lista está vazia
            self.prim=self.ult = No(valor,None) # Os atributos prim e ult apontam para o novo nó que vai ser criado
            self.ult.prox=self.prim # O apontador prox do ultimo elemento recebe self.prim, ou seja, aponta para o elemento fazendo o circulo
        else:
            self.prim=self.ult.prox = No(valor,self.prim) # O atributo prim recebe self.ult.prox, que vai receber o nó, e assim faz o circulo
        self.quant +=1 #self.quant recebe + 1
    def inserir_fim(self,valor):
        