class Les:
    def __init__(self,tamanho):
        self.tam_maximo=tamanho
        self.vetor=[None] * self.tam_maximo
        self.quant=0
    def inserir_fim(self,valor):
        self.vetor[self.quant]=valor
        self.quant+=1
    def show(self):
        for i in range(self.quant):
            print(self.vetor[i], end=" ")
        print()