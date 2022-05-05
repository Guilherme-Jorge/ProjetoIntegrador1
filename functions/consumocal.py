'''
Projeto Integrador I => Calculadora de Consumo de Calorias por refeicao
'''

def somaRefeicao():
    vetorRefeicao = []
    ref = ['café da manhã','almoço','café da tarde','janta','ceia']
    refeicao = 0
    while refeicao < 5:
        consumoValido = False
        while not consumoValido:
            try:
                numero = float(
                    input(f'\nFavor, digite seu consumo, em calorias, do(a) {ref[refeicao]} (ex: 1234.56): ')
                )
                if numero <= 0:
                    print('<<<ERRO: Valor inválido, use APENAS números positivos>>>')
                else:
                    vetorRefeicao.append(numero)
                    refeicao += 1
                    consumoValido = True
            except ValueError:
                print('<<<ERRO: Valor inválido, use APENAS números>>>')
    sumRefeicao = sum(vetorRefeicao)
    return sumRefeicao