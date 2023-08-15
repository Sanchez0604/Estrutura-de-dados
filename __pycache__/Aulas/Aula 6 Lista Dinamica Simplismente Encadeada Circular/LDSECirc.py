class No:
    def __init__(self,valor,proximo):
        self.info = valor
        self.prox = proximo
        
class Lee:
    def __init__(self,tamanho):
        self.tam_maximo = tamanho
        self.vetor = [None] * self.tam_maximo
        self.inicio = 0
        self.fim = 0
        self.quant = 0

    def inserir_fim(self, valor):
        self.vetor[self.fim] = valor
        self.fim = (self.fim + 1) % self.tam_maximo
        self.quant += 1
    
    def remover_fim(self):
        self.fim = (self.fim - 1) % self.tam_maximo
        self.quant -= 1