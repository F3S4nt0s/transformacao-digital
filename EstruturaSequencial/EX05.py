#Faça um Programa que converta metros para centímetros.

print("Esse programa converte metros para centímetros")


#atribui um valor digitado a variavel valor_em_metros
valor_em_metros = float(input("Digite o valor, em metros, que deseja transformar em centímetros: "))

#converte o valor em metros para centimetros
valor_em_centimetros = valor_em_metros*100

#retorna a mensagem informando que x metros são x*100 cm
print(f"{valor_em_metros} m são {valor_em_centimetros} cm")

