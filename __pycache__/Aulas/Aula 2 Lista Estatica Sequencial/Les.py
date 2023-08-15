from typing import Self


class Les:
    def __init__(self,tamanho):
        self.tam_maximo=tamanho #Define o tamanho da lista
        self.vetor=[None] * self.tam_maximo #Cria os vetores da lista de acordo com o seu tamanho
        self.quant=0 #Contador de itens na lista

    def inserir_fim(self,valor):
        if self.quant==self.tam_maximo:#Verifica se a quantidade de itens na lista é o mesmo do seu tamanho
            print('A lista está cheia!') #Se for verdade a lista está cheia e não pode mais ser povoada
        else:
            self.vetor[self.quant]=valor #Se a lista não estiver cheia o vetor na posição de quantidade da lista vai receber o novo valor
            self.quant+=1 #A quantidade de itens na lista é encrementada em mais um item

    def show(self):
        for i in range(self.quant): #Cria um laço de repetição com o tamanho da lista
            print(self.vetor[i], end=" ") #Printa o vetor na posição [i] e retira o \n para continuar na mesma linha
        print()

    def remover_fim():
        if self.quant==self.tam_maximo:
            print('A lista está vazia')
        else:
            self.quant-=1 #Decrementa o atributo quant em 1 item

    def inserir_inicio(self,valor):
        for i in range(self.quant,0,-1): #Inicia um loop que inicia na quantidade de itens na lista, termina em 0 e vai decrementando de 1 em 1
            self.vetor[i]=self.vetor[i-1] #Pega o item na posição [i] e o envia para o vetor ao lado, deixando assim a posição 0 vazia
        self.vetor[0]=valor #Fora do laço, com a posição 0 já vazia, o valor passado como parametro é colocado nesta istancia
        self.quant+=1 #Acrescenta o atributo quant em 1 item

    def remover_inicio(self):
        for i in range(self.quant-1): #Inicia um loop que peecorre todos os itens da lista
            self.vetor[i] = self.vetor[i+1] #Pega o item na posição [i] e o envia para o vetor a sua frente
        self.quant -=1 #Decrementa o atributo quant em 1 item

    def remover_elemento(self,valor):
        for i in range(self.tam_maximo): #Inicia um laço que percorre todos vetores da lista
            if self.vetor[i]== valor: #Verifica se o item na posição [i] é o valor passado
                for value in range(i,self.quant): #Inicia um loop a partir do ponto [i] até a quantidade de intens da lista
                    self.vetor[value]=self.vetor[value+1] #O vetor na posição value, recebe o valor do proximo vetor, preenchendo o local onde foi removido
        self.quant-=1 #Decrementa o atributo quant em 1 item

    def buscar(self,valor):
        for i in range(self.quant): #Inicia um loop com a quantidade itens na lista
            if self.vetor[i] == valor: #Verifica se o vetor na posição [i] é igual ao valor passado
                return "encontrado"
            else:
                return "não encontrado"
            
    def lista_vazia(self):
        if self.quant != self.tam_maximo: #Verifica se a quantidade de itens na lista é diferente do seu tamanho maximo
            return True
        else:
            return False

    def inserir_apos(self,valor1,valor2):
        if self.lista_vazia(): #Verifica se a lista possui espaço para fazer a operação
            for i in range(self.quant): #Inicia um loop na quantidade de itens da lista
                if self.vetor[i] == valor2: #Verifica se o valor de [i] é igual à um dos valores parametros passado como argumento
                    for value in range(self.quant,i,-1): #Inicia um loop que inicia no ultimo item da lista e termina em [i] e vai decrementando em 1 item
                        self.vetor[value]=self.vetor[value-1] #Empurra os itens em um vetor à frente
                    self.vetor[i+1]=valor1 #Vetor na posição após o valor2 é adicionado
            self.quant+=1

    def inserir_antes(self,valor1,valor2):
        if self.lista_vazia():
            for i in range(self.quant):
                if self.vetor[i] == valor2:
                    for value in range(self.quant,i,-1):
                        print(value)
                        self.vetor[value]=self.vetor[value-1]
                    self.vetor[i-1]=valor1
                    return
                
            
            
                    