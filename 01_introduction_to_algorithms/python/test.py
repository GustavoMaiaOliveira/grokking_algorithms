minha_lista = [11, 22, 33, 44, 55, 66, 77, 88, 99, 111]

def pesquisa_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1
    print('baixo -> ', baixo)
    print('alto -> ', alto)
    print('baixo + alto // 2 -> ', (baixo + alto) // 2)

    while baixo <= alto:
        meio = (baixo + alto) // 2
        print('meio -> ', meio)
        chute = lista[meio]
        print('chute -> ', chute)
        if chute == item:
            return meio
        if chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1
    return None

# print('resultado pesquisa 1 --->', pesquisa_binaria(minha_lista, 11))
# print('resultado pesquisa 2 --->', pesquisa_binaria(minha_lista, 22))
print('resultado pesquisa 3 --->', pesquisa_binaria(minha_lista, 33))
# print('resultado pesquisa 4 --->', pesquisa_binaria(minha_lista, 44))
# print('resultado pesquisa 5 --->', pesquisa_binaria(minha_lista, 55))
# print('resultado pesquisa 6 --->', pesquisa_binaria(minha_lista, 66))
# print('resultado pesquisa 7 --->', pesquisa_binaria(minha_lista, 77))
# print('resultado pesquisa 8 --->', pesquisa_binaria(minha_lista, 88))
# print('resultado pesquisa 9 --->', pesquisa_binaria(minha_lista, 99))
# print('resultado pesquisa 10 --->', pesquisa_binaria(minha_lista, 111))
