'''
Projeto Integrador I => Calculadora de IMC
'''

def valorIMC():
    from functions.peso import pesoValor

    peso = pesoValor()

    alturaValida = False
    while not alturaValida:
        try:
            altura = float(
                input('\nFavor, digite sua altura, em metros (ex: 1.70): ')
            )
            if altura <= 0:
                print('<<<ERRO: Valor inválido, use APENAS números positivos>>>')
            else:
                alturaValida = True

        except ValueError:
            print('<<<ERRO: Valor inválido, use APENAS números>>>')

    IMC = peso / ( altura ** 2 )

    return IMC