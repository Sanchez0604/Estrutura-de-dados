import Lee

lista = Lee.Lee(5)

print('Lista:')
lista.show()
lista.show_vetor()
lista.inserir_inicio('C')
print('Lista após inserir início C: (esperado - C)')
print('Lista')
lista.show()
lista.show_vetor()
lista.inserir_inicio('D')
print('Lista após inserir início D: (esperado - DC)')
lista.show()
lista.show_vetor()