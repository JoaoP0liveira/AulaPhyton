# verificar se é impar ou par 


"""
Digite um numero inteiro
Verifique se o numero é impar ou par
Escreva a mensagem correspondente
"""

print("Digite um numero para verificar se ele é impar ou par:")
numero = int(input())

if numero %2 == 0: 
    print(numero, "é par")
else: 
    print(numero, "é impar")