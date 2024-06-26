class lista:
    def __init__(self, info = None):
        self.info = info
        self.prox = None

def lista_cria():
    return lista()

def lista_insere(lst,valor):
    atual = lst
    novo = lista(valor)
    novo.prox = lst
    return novo


def lista_imprime(lst):
    atual = lst
    while atual is not None:
        print(atual.info)
        atual = atual.prox

def lista_circular(lst):
    atual = lst
    pos = 0
    size = 5
    for i in range(pos, pos - size):
        aux = pos % size
    print(aux)


lst = lista_cria()
lst = lista_insere(lst, 10)
lst = lista_insere(lst, 11)
lst = lista_insere(lst, 12)
lst = lista_insere(lst, 13)
lst = lista_insere(lst, 14)
lista_circular(lst)

circular = lista_circular(lst)
print("CIRCULAR", circular)