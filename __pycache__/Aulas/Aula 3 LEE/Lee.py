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
    def inserir_fim(self,valor):
        if self.quant == 0:
            self.prim = self.ult = self.ocupa_no(valor,-1)
            self.quant += 1
        else:
            self.vetor[self.ult].prox = self.ult = self.ocupa_no(valor,-1)
            self.quant += 1
    def devolve_no(self, no):
        self.vetor[no].prox = self.primeira_posicao_vazia
        self.primeira_posicao_vazia = no
    def remover_inicio(self):
        if self.quant == 1:
            self.devolve_no(self.prim)
            self.prim = self.ult = -1
        else:
            novo_prim = self.vetor[self.prim].prox
            self.devolve_no(self.prim)
            self.prim = novo_prim
        self.quant-=1
    def remover_fim(self):
        if self.quant == 1: #Verifica se a lista só possui um elemento
            self.devolve_no(self.prim) # se for verdadeiro, a função devolve_no recebe o endereço do primeiro elemento
            self.prim = self.ult =-1 # self.prim e self.ult recebem -1 indicando que a lista está vazia
        else:
            aux=self.prim #Recebe o primeiro elemento da lista
            while self.vetor[aux].prox != self.ult: #Enquanto o self.vetor[aux].prox for diferente do ultimo nó
                aux = self.vetor[aux].prox #Aux recebe o endereço do proximo nó
            self.devolve_no(self.ult)  # Fora do laço while, a função devolve nó recebe como paramentro o ultimo elemento da lista
            self.vetor[aux].prox = -1 # O Atributo prox de self.vetor[aux].prox recebe -1 indicando ser o ultimo elemento da lista
            self.ult = aux # sel.ult recebe aux como ultimo elemento
        self.quant -=1 #self.quant é decrementado em 1 elemento


        
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
