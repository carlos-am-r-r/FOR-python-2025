linha='¸,ø¤º°`°º¤ø,¸¸,ø¤º°'
print(linha)
print()
print('selecione seu programa')
print()
print(linha)
print()
start=int(input('1 - sequência de 13\n2 - múltiplos de 3\n3 - sequência dobrada\n4 - sequência de parada com escolha do usuário\n5 - contagem descrecente\n\n¸,ø¤º°`°º¤ø,¸¸,ø¤º°\n\nSelecione o número:'))
print()
print(linha)
print()

#1. Elabore o programa que gere a sequência dos números naturais ímpares até 13.
# Mostre também a quantidade de números da sequência gerados, use contador.

if start == 1:
    ct=0
    for variavel_de_controle in range(1, 13+1, 2):
        ct = ct + 1
        print(variavel_de_controle, end=" ")
    print()
    print(ct , "números no total")

#2. Elabore o programa que gere a sequência dos números naturais múltiplos de 3 até 21.
# Mostre também a soma dos números da sequência gerados, use somador.

if start == 2:
    ct=0
    for variavel_de_controle in range(3, 21+1, 3):
        ct = ct + variavel_de_controle
        print(variavel_de_controle, end=" ")
    print()
    print(ct , "soma dos números")

#3. Elabore o programa que gere a sequência do dobro dos números naturais até dez na ordem crescente.
# Mostre também a soma e a média aritmética da sequência gerada.

if start == 3:
    ct=0
    soma=0
    for variavel_de_controle in range(3, 21+1, 3):
        soma = soma + variavel_de_controle
        ct = ct + 1
        print(variavel_de_controle*2, end=" ")
    print()
    print(soma , "soma dos números")
    print(soma/ct , "média artimética")

#4. Implemente o programa que gere a sequência dos números naturais na ordem crescente
# até um valor final fornecido (digitado) pelo usuário.
# Mostre também a quantidade de valores da sequência gerada.

if start == 4:
    ct=0
    soma=0
    for variavel_de_controle in range(1, int(input('insira o valor final'))+1, 1):
        soma = soma + variavel_de_controle
        ct = ct + 1
        print(variavel_de_controle, end=" ")
    print()
    print(ct, "números no total")

#5. Implemente o programa que gere a sequência dos números naturais na ordem decrescente até o valor zero e
# o valor inicial será fornecido (digitado) pelo usuário. Mostre também a quantidade de valores da sequência gerada.

if start == 5:
    ct=0
    soma=0
    for variavel_de_controle in range(int(input('insira o valor inicial\n')), -1, -1):
        soma = soma + variavel_de_controle
        ct = ct + 1
        print(variavel_de_controle, end=" ")
    print()
    print(ct, "números no total")

print()
print(linha)
