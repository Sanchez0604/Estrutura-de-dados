import LDDE

lista = LDDE.Ldde()

# Inserir elementos no início
lista.inserir_inicio('E')
lista.inserir_inicio('D')
lista.inserir_inicio('C')
lista.inserir_inicio('B')
lista.inserir_inicio('A')
# Mostrar a lista
lista.show()
# Remove itens da lista
lista.remover('C')
lista.show()
# Insere valor na lista após o valor passado como argumento
lista.insereAposDet('C','B')
lista.show()