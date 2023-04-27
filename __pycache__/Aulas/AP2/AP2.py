class No:
    def __init__(self, valor, proximo):
        self.info = valor
        self.prox = proximo
        
class Fila:
    def __init__(self):
        self.prim = self.ult = None
        self.quant = 0

    def insere(self,valor):
        if self.quant == 0:
            self.prim = self.ult = No(valor,None)
        else:
            self.ult.prox = No(valor,None)
        self.quant += 1

    def remove(self):
        if self.quant == 1:
            self.prim = self.ult = None
        else:
            self.prim=self.prim.prox
        self.quant -=1

    def ver_primeiro(self):
        return self.prim.info
    
    def ver_quantidade(self):
        return self.quant
