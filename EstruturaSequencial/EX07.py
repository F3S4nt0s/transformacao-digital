#Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
print("Esse programa retorna o dobro da área de um quadrado baseado no tamanho dos lados desse quadrado")

#Solicita o tamanho do lado do quadrado
lado_quadrado = float(input("Insira o tamanho do lado do quadrado em cm: "))

#define que a área do quadrado seria o lado do quadrado multiplicado por ele mesmo (elevado a segunda potência)
area_quadrado = lado_quadrado ** 2

# define o dobro da área do quadrado
dobro_area_quadrado = area_quadrado * 2

#retorna mensagem informando o tamanho do lado, area e dobro da area do quadrado
print(f"Um quadrado de lado {lado_quadrado} cm tem uma área de {area_quadrado} cm e o dobro de sua área é de {dobro_area_quadrado} cm.")