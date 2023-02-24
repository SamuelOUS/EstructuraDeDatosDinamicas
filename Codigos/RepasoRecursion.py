def SumaElementosLista(lista):
    if len(lista) == 0:
        return 0
    else:
        cont = lista[0]
        return cont + SumaElementosLista(lista[1:])


print(SumaElementosLista([1, 2, 3, 4, 5]))


def ElementosLista(Lista):
    if len(Lista) == 0:
        return 0
    else:
        cont = 1
        return cont + ElementosLista(Lista[1:])

print(ElementosLista([1, 2, 3, 5, 5]))

def FactorialNumero(numero):
    if numero == 0:
        return 1
    else:

        return numero * FactorialNumero(numero-1)

print(FactorialNumero(990))