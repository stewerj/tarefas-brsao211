distancia_percorrida = float(input("Digite a distância percorrida (em km): "))

combustivel_gasto = float(input("Digite o combustível gasto (em litros): "))

consumo_medio = distancia_percorrida / combustivel_gasto


print(f"Distância percorrida: {distancia_percorrida:.2f} km")
print(f"Combustível gasto: {combustivel_gasto:.2f} litros")
print(f"Consumo médio: {consumo_medio:.2f} km/l")
