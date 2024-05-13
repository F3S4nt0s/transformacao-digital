#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#a) o produto do dobro do primeiro com metade do segundo .

num1 = int(input("Digite um número inteiro: "))
num2 = int(input("Digite outro número inteiro: "))
num3 = float(input("Digite um número real: "))

retorno_a = (num1*2)/(num2/2)

print(f"O produto do dobro de {num1} com metade do {num2} é {retorno_a}")



#b) a soma do triplo do primeiro com o terceiro.
retorno_b = (num1*3)+num3
print(f"A soma do triplo de {num1} com {num3} é {retorno_b}")

#c) o terceiro elevado ao cubo.
retorno_c = num3**3

print(f"O {num3} elevado ao cubo é {retorno_c}")




