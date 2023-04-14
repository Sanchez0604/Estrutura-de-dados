class Conjunto:
    def __init__(self):
        self.numeros=[False] * 11
    
    def inserir(self,num):
        if num>=0 and num<=10:
            self.numeros[num]= True
        else:
            return ' Valor inválido!'
    def remover(self,num):
        if num>=0 and num<=10:
            self.numeros[num]= False
        else:
            return 'Valor inválido!'
    def show(self):
        for i in range(11):
            if self.numeros[i]:
                print(i)
    def uniao(self,conj2):
        conj_uniao=Conjunto()
        for i in range(11):
            conj_uniao.numeros[i] = self.numeros[i] or conj2.numeros[i]
        return conj_uniao
    def interseccao(self,conj2):
        conj_inter= Conjunto()
        for i in range(11):
            conj_inter.numeros[i]=self.numeros[i] and conj2.numeros[i]
        return conj_inter
        