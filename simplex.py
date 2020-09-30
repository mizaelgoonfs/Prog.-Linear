''' determina em qual linha está a variável que sairá da base '''


def teste(matriz, coluna, b):
    sai_base = b  # maior elemento da matriz original
    linha = -1  # inicializando variável linha
    for i in range(len(matriz)):
        if (matriz[i][coluna] != 0 and matriz[i][len(matriz[0]) - 1] / matriz[i][coluna] <= sai_base):
            sai_base = matriz[i][len(matriz[0]) - 1] / matriz[i][coluna]
            linha = i

    return linha


''' pivoteamento da nova base em X[linha][coluna]'''


def troca_de_base(matriz, linha, coluna, fobjetivo):
    mult = fobjetivo[coluna]  # variáveis auxiliares para o pivoteamento
    div = matriz[linha][coluna]

    for i in range(len(matriz[0])):  # fazendo o pivô ser igual a 1
        matriz[linha][i] /= div
        fobjetivo[i] -= matriz[linha][i] * mult

    for i in range(len(matriz)):  # zerando elementos acima e abaixo do pivô
        if ((i != linha) and (matriz[i][coluna] != 0)):
            mult = matriz[i][coluna]
            for j in range(len(matriz[0])):
                matriz[i][j] -= matriz[linha][j] * mult


''' determina qual variável não-básica entrará na base '''


def entra_base(vetor):
    valor_min = min(vetor[0:len(vetor) - 1], key=int)
    if not (valor_min >= 0):
        return vetor.index(valor_min)
    else:
        return -1

def variaveis_basicas(matrizNova):
    var_basicas = []
    for x in range(len(matrizNova[0]) - 1):
        forma_canonica = []
        soma_canonica = 0
        for y in range(len(matrizNova)):
            if ((matrizNova[y][x] != 0) and (matrizNova[y][x] != 1)):
                soma_canonica += 1
            forma_canonica.append(matrizNova[y][x])

        if ((forma_canonica.count(1) == 1) and (soma_canonica == 0)):
            var_basicas.append(x)

    return var_basicas

def print_tablo(matriz, fobjetivo, var_basicas):
    print("\nEssa é a matriz:")
    text = '| '
    for i in range(len(matriz[0]) - 1):
        text += 'X{} | '.format(i + 1)

    print(text, 'b ')
    for i in range(len(matriz)):
        print('{}'.format(matriz[i]))

    print("Essa é a função objetivo a ser minimizada:")
    print(fobjetivo, "\n")

    print('Variáveis básicas: ')
    for i in range(len(var_basicas)):
        print('| X{} |'.format(var_basicas[i] + 1))


entrada = open('PPL2.txt', 'r').readlines()
matrizNova = []
for line in entrada:
    linhas = []
    for i in line.split(' '):
        num = round(float(i), 2)
        linhas.append(num)
    matrizNova.append(linhas)

matriz = matrizNova[1:]
fobjetivo = matrizNova[0]

A = 0
for i in range(len(matriz)):  # loucura
    if (max(matriz[i], key=int) > A):
        A = max(matriz[i], key=int)

var_basicas = variaveis_basicas(matrizNova)
print_tablo(matriz, fobjetivo, var_basicas)

question = 's'
''' aplicando o simplex (+ou-) '''
while (question != 'f'):
    coluna_entra_base = entra_base(fobjetivo)
    if coluna_entra_base == -1:
        break

    troca_de_base(matriz, teste(matriz, coluna_entra_base, A), coluna_entra_base, fobjetivo)

    var_basicas = variaveis_basicas(matriz)
    print_tablo(matriz, fobjetivo, var_basicas)

    question = input("continuar: 's', parar: 'f'.\n")