#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

#define PI como uma constante 3.1415...
PI = 3.14159265359


print("Esse programa calcula a área de uma circuferência baseada no raio.")

#define que o raio do circulo será imputado como um numero decimal
raio = float(input("Digite o raio da circunferência em cm: "))

#define que a area do circulo é aproximadamente 
area_circunferencia = round(PI * (raio**2),2)

print(f"A área de um círculo com raio {raio} cm é igual à aproximadamente{area_circunferencia} cm.")