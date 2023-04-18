class No:
    def __init__(self,valor,proximo):
        self.info = valor
        self.prox = proximo
        
class Lee:
    def __init__(self,tamanho):
        self.tam_maximo = tamanho
        self.vetor = [None] * self.tam_maximo
        self.quant = 0
        self.primeira_posicao_vazia=self.inicializa_estrutura()
        self.prim=-1
        self.ult=-1

    def inicializa_estrutura(self):
        for i in range(self.tam_maximo-1):
            self.vetor[i] = No(None,i+1)
        self.vetor[self.tam_maximo-1] = No(None,-1)
        return 0
    def ocupa_no(self,valor,proximo):
        posicao_livre = self.primeira_posicao_vazia
        self.primeira_posicao_vazia = self.vetor[self.primeira_posicao_vazia].prox
        self.vetor[posicao_livre] = No(valor,proximo)
        return posicao_livre
    def inserir_inicio(self,valor):
        if self.quant == 0:
            self.prim = self.ult = self.ocupa_no(valor,-1)
            self.quant += 1
        else:
            self.prim = self.ocupa_no(valor,self.prim)
            self.quant += 1
    def show(self):
        aux = self.prim
        while aux != -1:
            print(self.vetor[aux].info)
            aux = self.vetor[aux].prox
    def show_vetor(self):
        print('Prim=',self.prim)
        print('Ult=',self.ult)
        print('Vetor=')
        for i in range(self.tam_maximo):
            print(i, self.vetor[i].info, self.vetor[i].prox)

        '''def inicializa_estrutura(self):
            for i in range(self.tam_maximo-1):
                self.vetor[i] = No(None,i+1)
            self.vetor[self.tam_maximo-1] = No(None,-1)
            return 0

        self.primeira_posicao_vazia = self.inicializa_estrutura()

        self.prim = -1
        self.ult = -1

        def inserir_inicio(self,valor):
            if self.quant == 0:
                self.prim = self.ult = self.ocupa_no(valor,-1)
                self.quant +=1
            else:
                self.prim = self.ocupa_no(valor,self.prim)
                self.quant +=1
        def ocupa_no(self,valor,proximo):
            posicao_livre=self.primeira_posicao_vazia
            self.primeira_posicao_vazia=self.vetor[self.primeira_posicao_vazia].prox
            self.vetor[posicao_livre] = No(valor,proximo)
            return posicao_livre
        def show(self):
            aux = self.prim
            while aux != -1:
                print(self.vetor[aux].info)
                aux = self.vetor[aux].prox
        def show_vetor(self):
            print("Prim=",self.prim)
            print("Ult=",self.ult)
            print("Vetor=")
            for i in range (self.tam_maximo):
                print(i, self.vetor[i].info, self.vetor[i].prox)'''
