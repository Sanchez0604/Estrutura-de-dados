import Ldse

lista = Ldse.Ldse()

# Inserir elementos no início
lista.inserir_inicio('C')
lista.inserir_fim('B')
lista.inserir_fim('A')
# Inserir elementos no fim
lista.inserir_fim('D')
lista.inserir_fim('E')
# Mostrar a lista
lista.show()
lista.remove_posicao(3)
lista.show()
lista.show()
