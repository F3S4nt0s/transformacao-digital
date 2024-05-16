#Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula:
 #(72.7*altura) - 58


# Esse exercício eu fiz em POO

from Classes import CalculadoraDePesoIdeal #IMPORTEI A CLASSE CalculadoraDePesoIdeal

print("Esse programa calcula o seu peso ideal, baseado na sua altura")

altura_usr = float(input("Digite, em metros, a sua altura: ")) #solicitei altura do usuário


calculadora = CalculadoraDePesoIdeal(altura_usr,"M") #defini o objeto calculadora, como sendo da classe CalculadoraDePesoIdeal, solicitando altura e gênero como sendo M (nesse exercicio não solicitamos o genero)


peso_ideal = round(calculadora.calcular_peso(), 2) #arredondei a função calcular_peso

print(f"O seu peso ideal seria: {peso_ideal}  kg")
