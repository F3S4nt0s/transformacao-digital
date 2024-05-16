#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7

# Esse exercício eu fiz em POO

from Classes import CalculadoraDePesoIdeal #IMPORTEI A CLASSE CalculadoraDePesoIdeal

print("Esse programa calcula o seu peso ideal, baseado na sua altura")

altura_usr = float(input("Digite, em metros, a sua altura: ")) #solicitei altura do usuário
genero_usr = input("Digite o seu gênero, 'M' para masculino e 'F' para feminino: ")

calculadora = CalculadoraDePesoIdeal(altura_usr, genero_usr) #defini o objeto calculadora, como sendo da classe CalculadoraDePesoIdeal, solicitando altura e gênero


peso_ideal = round(calculadora.calcular_peso(), 2) #arredondei a função calcular_peso

print(f"O seu peso ideal seria: {peso_ideal}  kg")
