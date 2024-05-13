#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.


print("Esse programa converte uma temperatura em graus Celsius para graus Fahrenheit")


# solicita que o usuário adicione temperatura em °C e atribui valor para variavel temp_c

temp_c = float(input("Digite valor de temperatura em graus Celsius: "))


# converte temp_C para Fahrenheit e atribui a variavel temp_f

temp_f = (temp_c * 9/5) + 32


# retorna mensagem com a conversão
print(f"{temp_c}°C são o equivalente à aproximadamente {temp_f}°F.")