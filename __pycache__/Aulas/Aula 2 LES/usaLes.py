import Les

# Inicializa a lista estática sequencial com tamanho máximo
# igual a 5
lista = Les.Les(5)

# Insere o elemento 3 na lista
lista.inserir_fim(3)
lista.show()

# Insere o elemento 5 na lista
lista.inserir_fim(5)
lista.show()

# Insere o elemento 7 na lista
lista.inserir_fim(7)
lista.show()

# Insere o elemento 9 na lista
lista.inserir_fim(9)
lista.show()

# Remove o elemento 7 da lista e realoca os elementos a partir da posição do 7
lista.remover_elemento(7)
lista.show()

# Busca o elemento e retorna o indice
lista.buscar(3)

# Adiciona o elemento após o elemento dado
lista.inserir_apos(6,5)
lista.show()

# Adiciona o elemento antes do elemento dado
#lista.inserir_antes(7,9)
#lista.show
