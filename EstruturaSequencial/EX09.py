# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
#C = 5 * ((F-32) / 9).


print("Esse programa converte uma temperatura em graus Fahrenheit para graus Celsius")


# solicita que o usuário adicione temperatura em °F e atribui valor para variavel temp_f
temp_f = float(input("Digite valor de temperatura em graus Fahrenheit: "))

# converte temp_f para celcius e atribui a variavel temp_c
temp_c = round(5*((temp_f - 32)/9),2)

# retorna mensagem com a conversão
print(f"{temp_f}°F são o equivalente à aproximadamente {temp_c}°C.")
