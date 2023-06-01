import Tree 
t = Tree.Tree()

t.insere(4)
t.insere(2)
t.insere(1)
t.insere(3)
t.insere(6)
t.insere(8)
t.insere(7)
t.insere(5)
print(t.raiz.info)

t.inOrdem()
print(t.busca(3))
print(t.somaFolhas())
t.printFolhas()
print(t.busca(8))