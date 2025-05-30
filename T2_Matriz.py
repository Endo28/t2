import random

def generar_matriz(num_pares):
    matriz = []
    for _ in range(num_pares):
        x = random.randint(-81, 81)
        y = random.randint(-81, 81)
        matriz.append([x, y])
    return matriz

def calcular_distancia(coord):
    x, y = coord
    return (x**2 + y**2)

def encontrar_maximo(matriz):
    if len(matriz) == 0:
        return None
    if len(matriz) == 1:
        x, y = matriz[0]
        if x > 0 and y < 0:
            return matriz[0]
        else:
            return None

    mitad = len(matriz) // 2
    izquierda = matriz[:mitad]
    derecha = matriz[mitad:]

    mejor_izq = encontrar_maximo(izquierda)
    mejor_der = encontrar_maximo(derecha)

    if mejor_izq and mejor_der:
        if calcular_distancia(mejor_izq) > calcular_distancia(mejor_der):
            return mejor_izq
        else:
            return mejor_der
    elif mejor_izq:
        return mejor_izq
    else:
        return mejor_der

num_pares=int(input("Ingrese la cantidad de pares de coordenadas: "))
matriz= generar_matriz(num_pares)

print ("\nCoordenadas generadas: ")
for coord in matriz:
    print(coord)

resultado= encontrar_maximo(matriz)

if resultado:
    x, y=resultado
    distancia = (x**2+y**2)**0.5
    print(f"\nLa coordenada más alejada del origen (0,0) es: {resultado}")
    print(f"Distancia: {distancia:.2f}")
else:
    print("\nNo se encontró ninguna coordenada con X>0 e Y<0.")