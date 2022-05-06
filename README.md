# Projeto Integrador 1 - Cálculo de IMC e Consumo de Calorias

Este projeto consiste em uma atividade avaliativa da Pontifícia Universidade Católica Campinas (PUC-Campinas), do curso de Engenharia de Software, da turma do ano de 2022 (1º Semestre). Foi exigido a criação de um sistema que calcule o IMC de um indivíduo, assim como o consumo de calorias do mesmo.

Para usá-lo apenas rode o arquivo `Projeto1.py`

---

### Funcionamento do Sistema

O sistema inicia com a apresentação dos integrantes:
```
=============================================================
|| Seja bem vindo ao Projeto Final de Projeto integrador 1 ||
||        Calculadora de IMC e Ingestão de calorias        ||
||                                                         ||
|| Alunos: 22001646 - André Laudares Soares                ||
||         22007283 - Guilherme Ferreira Jorge             ||
||         20195509 - Lucas Muterle                        ||
||         22004817 - Matheus Ribeiro Marafon              ||
||         22005575 - Raul Migliari                        ||
=============================================================
Press Enter to start
```
Em seguida, ele pedirá a entrada do peso e da altura do indivíduo:
```
Favor, digite seu peso, em quilogramas (ex: 70.6): a
<<<ERRO: Valor inválido, use APENAS números>>>

Favor, digite seu peso, em quilogramas (ex: 70.6): -1
<<<ERRO: Valor inválido, use APENAS números positivos>>>

Favor, digite seu peso, em quilogramas (ex: 70.6): 70.6

Favor, digite sua altura, em metros (ex: 1.70): 1.7
```
Com esses dados, o sistema irá calcular e reportar o IMC do usuário, assim como sua classificação de peso de acordo com o valor:
```
==========================================================
||------------------<Relatório do IMC>------------------||
||                                                      ||
||                  Seu IMC é: 24.43                    ||
||        Você foi classificado com Peso Normal         ||
||                                                      ||
==========================================================

Press Enter to continue
```
Em seguida, ele irá pedir a entrada de sexo e idade:
```
Você é:   
Homem (H) 
Mulher (M)
[H/M]?: 1 

<<<ERRO: Sexo inválido, digite H ou M>>>

Você é:
Homem (H)
Mulher (M)
[H/M]?: a

<<<ERRO: Sexo inválido, digite H ou M>>>

Você é:
Homem (H)
Mulher (M)
[H/M]?: h

Favor, digite sua idade: 18.1
<<<ERRO: Valor inválido, use APENAS números sem vírgula>>>

Favor, digite sua idade: 18
```
Assim como o IMC, o sistema usará estes dados para calcular o gasto energético basal do usuário e depois irá mostrá-lo:
```
==========================================================
||--------------<Relatório do gasto base>---------------||
||                                                      ||
||     Seu gasto energético basal é 1637.51 calorias    ||
||                                                      ||
==========================================================

Press Enter to continue
```
Em seguida, o sistema irá pedir a entrada do consumo de calorias de acordo com as refeições padrões (café da manhã, almoço, café da tarde, janta, ceia):
```
Favor, digite seu consumo, em calorias, do(a) café da manhã (ex: 1234.56): 1234.56

Favor, digite seu consumo, em calorias, do(a) almoço (ex: 1234.56): 1234.56

Favor, digite seu consumo, em calorias, do(a) café da tarde (ex: 1234.56): 1234.56

Favor, digite seu consumo, em calorias, do(a) janta (ex: 1234.56): 1234.56

Favor, digite seu consumo, em calorias, do(a) ceia (ex: 1234.56): 1234.56
```
Por fim, o sistema irá fazer o relatório final com todas as informações obtidas do usuário:
```
===================================================================  
||-----------------------<Relatório final>-----------------------||  
||                                                               ||  
||                      Seu IMC é: 24.43                         ||  
||             Você foi classificado com Peso Normal             ||  
||                                                               ||  
||         Seu gasto energético basal é 1637.51 calorias         ||  
||                                                               ||  
||       Seu consumo total de calorias é de 6172.80 calorias     ||  
|| A diferença da ingestão com o gasto calorico é 4535.29 calorias ||
||     Voce está ingerindo mais calorias do que o necessário     ||  
||                                                               ||  
===================================================================
```

---

Este é apenas o projeto base, o projeto final irá adcionar:

- Suporte para múltiplos usuários
- Cálculo de ingestão calórica mais robusto
- Integração com banco de dados [AINDA NÃO FINAL]
- Interface gráfica do sistema [AINDA NÃO FINAL]