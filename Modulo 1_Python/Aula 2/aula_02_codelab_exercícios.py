# -*- coding: utf-8 -*-
"""Aula 02 Codelab Exercícios.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mv6mLrehAUIbj1STvWblgancdDOc5CGG

Exercício 01 - Conversor de moedas

Crie um programa que solicite um um valor em real ao usuário e converta esse valor, para:

DOLAR,
EURO,
LIBRA ESTERLINA,
DÓLAR CANADENSE,
PESO ARGENTINO,
PESO CHILENO.

Para esse exercício você precisará realizar uma pesquisa para saber a cotação de cada moeda em real. Mostrar o resultado no formato $ XXXX.XX
"""

valor_Dolar = 5.04
valor_Euro = 6.13
valor_Libra = 7.13
valor_PesoChileno = 0.0070
valor_PesoArgentino = 0.053
valor_DolarCanadense = 4.16

quantidade_Real = float(input('Qual o valor em R$ a ser convertido? '))

quantidade_Dolar = quantidade_Real / valor_Dolar
print('Total de ' +str(quantidade_Dolar) + ' dólares')
print()
print('Total de ' +str(quantidade_Real / valor_Euro) + ' Euros')
print()
print('Total de ' +str(quantidade_Real / valor_Libra) + ' Libras')
print()
print('Total de ' +str(quantidade_Real / valor_PesoChileno) + ' Pesos Chilenos')
print()
print('Total de ' +str(quantidade_Real / valor_PesoArgentino) + ' Pesos Argentinos')
print()
print('Total de ' +str(quantidade_Real / valor_DolarCanadense) + ' Dolares Canadenses')

"""Exercício 02 - Calculadora de aumento de aluguel
Vamos construir um programa que irá calcular o aumento anual do seu aluguel.

A sua calculadora vai receber o valor do aluguel e calcular o aumento baseado no IGPM de 31%. A calculadora deve apresentar o aluguel reajustado no formato R$ XXXX.XX.
"""

igpm = 31

valor_Aluguel_Atual = float(input("Qual o valor atual do aluguel? "))

aumento = (igpm/100)*valor_Aluguel_Atual
print("Vai aumentar", aumento)
valor_Final = valor_Aluguel_Atual + aumento
print(f"O valor após o reajuste é de: R$ {(valor_Final):.2f}")