from typing import Self


class Les:
    def __init__(self,tamanho):
        self.tam_maximo=tamanho
        self.vetor=[None] * self.tam_maximo
        self.quant=0
    def inserir_fim(self,valor):
        if self.quant==self.tam_maximo:
            print('A lista está cheia!')
        else:
            self.vetor[self.quant]=valor
            self.quant+=1
    def show(self):
        for i in range(self.quant):
            print(self.vetor[i], end=" ")
        print()
    def remover_fim():
        if self.quant==self.tam_maximo:
            print('A lista está vazia')
        else:
            self.quant-=1
    def inserir_inicio(self,valor):
        for i in range(self.quant,0,-1):
            self.vetor[i]=self.vetor[i-1]
        self.vetor[0]=valor
        self.quant+=1
    def remover_inicio(self):
        for i in range(self.quant-1):
            self.vetor[i] = self.vetor[i+1]
        self.quant -=1
    def remover_elemento(self,valor):
        for i in range(self.tam_maximo):
            if self.vetor[i]== valor:
                for value in range(i,self.quant):
                    self.vetor[value]=self.vetor[value+1]
        self.quant-=1
    def buscar(self,valor):
        for i in range(self.quant):
            if self.vetor[i]== valor:
                return "encontrado"
            else:
                return "não encontrado"
            
    def lista_cheia(self):
        if self.quant == self.tam_maximo:
            return True
        else:
            return False

    def inserir_apos(self,valor1,valor2):
        if self.lista_cheia() == False:
            for i in range(self.quant):
                if self.vetor[i]== valor2:
                    for value in range(self.quant,i,-1):
                        self.vetor[value]=self.vetor[value-1]
                    self.vetor[i+1]=valor1
            self.quant+=1
    def inserir_antes(self,valor1,valor2):
        if self.lista_cheia() == False:
            for i in range(self.quant):
                if self.vetor[i]== valor2:
                    for value in range(self.quant,i,-1):
                        print(value)
                        self.vetor[value]=self.vetor[value-1]
                    self.vetor[i-1]=valor1
                    return
                
            
            
                    