class No:
    
    def __init__(self, valor, prioridade, proximo):
        self.info = valor
        self.prioridade = prioridade #Recebe o nivel de prioridade do item ficando assim ||info|prioridade|prox||
        self.prox = proximo

class Fila_prioridade:
    
    def __init__(self):
        self.prim = self.ult = None
        self.quant = 0

    def inserir(self, valor, prioridade):
        if self.quant == 0:
            self.prim = self.ult = No(valor, prioridade, None)#Se for o primeiro item da lista, prim e ult vão receber o nó criado.
        else:
            self.ult.prox = self.ult = No(valor, prioridade, None)# Se não o campo prox do ultimo item e o atributo ult vão receber o novo nó criado.
        self.quant += 1

    def inserir(self, valor, prioridade):
        if self.quant == 0: #Se a lista está vazia, chama o construtor e cria o nó sem verificação de prioridade
            self.prim = self.ult = No(valor, prioridade, None)
        else:
            aux = self.prim #Se a lista não está vazia, cria-se as variaveis aux e ant para percorrer a lista
            ant = None
        while aux != None and aux.prioridade <= prioridade:
            ant = aux
            aux = aux.prox
        if aux == self.prim:
            self.prim = No(valor, prioridade, self.prim)
        elif aux == None:
            self.ult.prox = self.ult = No(valor, prioridade, None)
        else:
            ant.prox = No(valor, prioridade, aux)
        self.quant += 1

    def remover(self):
        if self.quant == 1:
            self.prim = self.ult = None #Se existir somente um item na lista, ele a remove pois não vai existir prioridade de remoção.
        else:
            aux = maior = self.prim # Se não, criam-se duas variaveis que vão receber,de inicio o primeiro nó, sendo aux um auxiliar para percorrer a lista e maior para apontar o item de maior prioridade.
            maior_prioridade = self.prim.prioridade # Outra variavel é criada para receber o nivel de prioridade do nó presente em aux.
            ant = None # E por ultimo a variavel ant, que vai receber o nó anterior a aux já que é uma lista simplesmente encadeada
        while aux is not None:#Aqui se percorre a lista
            if aux.prioridade > maior_prioridade: #Verifica se o nivel de prioridade de aux, é maior que a da variavel maior_prioridade
                maior_prioridade = aux.prioridade #Caso for verdade, maior_prioridade vai receber o nivel de prioridade de aux
                print(aux.info, maior_prioridade)
                maior = aux #A variavel maior vai apontar para o nó presente em aux
                ant_maior = ant # Cria-se outra variavel para indicar o nó anterior ao nó de maior prioridade
            ant = aux #A variavel ant começa a apontar o nó presente em aux
            aux = aux.prox #E aux começa a apontar para o nó seguinte
        if maior == self.prim: #Se após percorrer a lista, verificar que o item de maior prioridade é o primeiro
            self.prim = self.prim.prox #O atributo prim vai apontar para o proximo item indicado em prim.prox
        else:
            ant_maior.prox = maior.prox #A variavel anterior ao maior vai receber em seu atributo prox, o proximo nó depois do nó de maior valor
            if maior == self.ult: #Se o nó de maior valor for o ultimo
                self.ult = ant_maior #O atributo ult vai apontar para o ant_maior, ou seja para o nó anterior ao maior
                self.ult.prox = None #Adiciona None para o atributo prox ultimo nó
        self.quant -= 1 #Decrementa a fila em 1 item

    def esta_vazia(self):
        return self.quant == 0
    
    def tamanho_atual(self):
        return self.quant
    
    def ver_primeiro(self):
        return self.prim.info
    
    def show(self):
        aux = self.prim
        while aux != None:
            print('Valor: ', aux.info, ' - prioridade: ', aux.prioridade)
            aux = aux.prox
        print('\n')