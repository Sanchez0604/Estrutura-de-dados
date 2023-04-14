import Conjunto
# Criação dos objetos da classe Conjunto
conjunto1= Conjunto.Conjunto()
conjunto2= Conjunto.Conjunto()
#Inserção dos valores nos conjuntos
conjunto1.inserir(5)
conjunto1.inserir(7)
conjunto1.inserir(8)
conjunto2.inserir(5)
conjunto2.inserir(9)
conjunto2.inserir(0)

#Remoção dos valores nos conjuntos
conjunto1.remover(7)
conjunto2.remover(0)
# Apresentação dos conjuntos
print('Conjunto 1:')
conjunto1.show()
print('Conjunto 2:')
conjunto2.show()
# União dos conjuntos
uniao = conjunto1.uniao(conjunto2)
print('União dos conjuntos: ')
uniao.show()
# Intersecção dos conjuntos
inter = conjunto1.interseccao(conjunto2)
print('Interseção dos conjuntos: ')
inter.show()