'''
7. Leia uma temperatura em graus Fahrenheit e apresente-a convertida em graus Celcius.
A fórmula de conversão é: C = 5.0*(F-32.0)/9.0, sendo C a temperatira em Celcius e
F a temperatura em Fahrenheit.
'''

F = float(input('Digite uma Temperatura em Fahrenheit...:'))
C = 5.0*(F-32.0)/9.0
print(f' temperatura {F}° graus Fahrenheit é igual a {C}° graus Celcius')
