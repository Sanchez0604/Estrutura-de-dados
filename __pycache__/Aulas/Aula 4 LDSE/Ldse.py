class No:
    def __init__(self, valor, proximo):
        self.info = valor
        self.prox = proximo

class Ldse:
    def __init__(self):
        self.prim = self.ult = None
        self.quant = 0

    def remove_posicao(self,posicao):
        if self.quant==1: #Verifica se a lista possui somente um elemento
            self.prim=self.ult=None #Se for verdadeiro os atributos prim e ult recebem None
        else:
            aux= self.prim #aux recebe a posição do primeiro item da lista
            while aux.prox != posicao: #Cria um laço que percorre a lista até encontrar o valor passado como argumento
                aux= aux.prox #aux recebe o valor da proxima posição através do atributo prox
            aux2=aux.prox
            aux.prox=aux2.prox
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