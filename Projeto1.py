'''
Projeto Integrador I => Sistema completo

Coisas para fazer:
- Codigo da ingestao de calorias (Fazer uma tabela de valores para os alimentos e somar para saber o valor total)
'''

from functions.peso import *
from functions.imc import *
from functions.gastobasal import *
from functions.consumocal import *
import os

os.system('cls')

'''Apresentação do Sistema'''
print('=' * 61 )
print('|| Seja bem vindo ao Projeto Final de Projeto integrador 1 ||')
print('||        Calculadora de IMC e Ingestão de calorias        ||')
print('||                                                         ||')
print('|| Alunos: 22001646 - André Laudares Soares                ||')
print('||         22007283 - Guilherme Ferreira Jorge             ||')
print('||         20195509 - Lucas Muterle                        ||')
print('||         22004817 - Matheus Ribeiro Marafon              ||')
print('||         22005575 - Raul Migliari                        ||')
print('=' * 61)

input('\nPress Enter to start')

os.system('cls')

peso = pesoValor()

'''Calculo do IMC'''
IMC = valorIMC(peso)

os.system('cls')

'''Relatorio do IMC e Classificação'''
print('=' * 58)
print('||------------------<Relatório do IMC>------------------||')
print('||                                                      ||')
print(f'||                  Seu IMC é: {IMC:.2f}                    ||')
if (IMC < 18.5):
    print('||        Você foi classificado com Peso Baixo          ||')
elif (18.5 <= IMC < 25):
    print('||        Você foi classificado com Peso Normal         ||')
elif (25 <= IMC < 30):
    print('||         Você foi classificado com Sobrepeso          ||')
elif (30 <= IMC < 35):
    print('||     Você foi classificado com Obesidade (Grau 1)     ||')
elif (35 <= IMC < 40):
    print('||  Você foi classificado com Obesidade Severa (Grau 2) ||')
elif (40 <= IMC):
    print('|| Você foi classificado com Obesidade Mórbida (Grau 3) ||')
print('||                                                      ||')
print( '=' * 58 )
input('\nPress enter to continue')

os.system('cls')

'''Calculo do gasto energetico para saber ate quanto a pessoa pode ingerir no dia'''
gasto = gastoEnergetico(peso)

os.system('cls')

'''Relatório do Gasto energético basal'''
print('=' * 58)
print('||--------------<Relatório do gasto base>---------------||')
print('||                                                      ||')
print(f'||     Seu gasto energético basal é {gasto:.2f} calorias    ||')
print('||                                                      ||')
print('=' * 58)
input('\nPress enter to continue')

os.system('cls')

'''Calculo do consumo de calorias que uma pessoa tem de acordo com as refeições (café da manhã, almoço, café da tarde, jantar, ceia)'''
sumRefeicao = somaRefeicao()
diferenca = (sumRefeicao - gasto)

'''Relatorio final do sistema geral'''
os.system('cls')

print('=' * 67)
print('||-----------------------<Relatório final>-----------------------||')
print('||                                                               ||')

'''Relatorio do IMC e Classificação'''
print(f'||                      Seu IMC é: {IMC:.2f}                         ||')
if (IMC < 18.5):
    print('||             Você foi classificado com Peso Baixo              ||')
elif (18.5 <= IMC < 25):
    print('||             Você foi classificado com Peso Normal             ||')
elif (25 <= IMC < 30):
    print('||              Você foi classificado com Sobrepeso              ||')
elif (30 <= IMC < 35):
    print('||          Você foi classificado com Obesidade (Grau 1)         ||')
elif (35 <= IMC < 40):
    print('||       Você foi classificado com Obesidade Severa (Grau 2)     ||')
elif (40 <= IMC):
    print('||       Você foi classificado com Obesidade Mórbida (Grau 3)    ||')

print('||                                                               ||')

'''Relatório do Gasto Energético Basal'''

print(f'||         Seu gasto energético basal é {gasto:.2f} calorias         ||')

print('||                                                               ||')

'''Relatório do Consumo de calorias por refeição'''
print(f'||       Seu consumo total de calorias é de {sumRefeicao:.2f} calorias     ||')
print(f'|| A diferença da ingestão com o gasto calorico é {diferenca:.2f} calorias ||')
if (diferenca > 0):
    print(f'||     Voce está ingerindo mais calorias do que o necessário     ||')
else:
    print(f'||      Voce está dentro do padrao de calorias necessárias       ||')
print('||                                                               ||')

print('=' * 67)