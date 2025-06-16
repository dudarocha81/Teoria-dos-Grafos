import math

vertices = {
    "PONTO INICIAL - I": (24, 23),
    "PONTO FINAL - J": (6, 36),  
    "LAB 01 - 1": (7, 10),
    "LAB 01 - 2": (15, 10),
    "LAB 02": (22, 6),
    "MESA 01 - 1": (20, 32),
    "MESA 01 - 2": (20, 34),
    "MESA 01 - 3": (18, 34),
    "MESA 01 - 4": (18, 32),
    "MESA 01 - C1 - 1": (17, 32),
    "MESA 01 - C1 - 2": (17, 33),
    "MESA 01 - C2 - 1": (18, 31),
    "MESA 01 - C2 - 2": (19,31 ),
    "MESA 01 - C3 - 1": (20,32),
    "MESA 01 - C3 - 2": (20, 33),
    "MESA 01 - C4 - 1": (18, 35),
    "MESA 01 - C4 - 2": (19, 35),
    "MESA 02 - 1": (3, 3),
    "MESA 02 - 2": (3, 4),
    "MESA 02 - 3": (1, 4),
    "MESA 02 - 4": (1, 3),
    "MESA 02 - C1 - 1": (1,3),
    "MESA 02 - C1 - 2": (1, 4),
    "MESA 02 - C3 - 1": (4,3),
    "MESA 02 - C3 - 2": (4, 4),
    "MESA 02 - C4 - 1": (3, 5),
    "MESA 02 - C4 - 2": (2, 5),
    "SALA 01 - 1": (3, 27),
    "SALA 01 - 2": (3, 35),
    "SALA 02 - 1": (22, 22),
    "SALA 02 - 2": (22, 30),
    "B. F": (4, 16),
    "B. M": (4, 24),
    "B. C - 1": (1, 30),
    "B. C - 2": (1, 32),
    "CORREDOR - 1": (12, 21),
    "CORREDOR - 2": (14, 21),
    "ESCADA 1 - 1": (22, 16),
    "ESCADA 1 - 2": (22, 17),
    "ESCADA 2 - 1": (22, 20),
    "ESCADA 2 - 2": (22, 21),
    "ELEVAS - 1": (0, 0),
    "ELEVAS - 2": (3, 0),
    "ELEVAS - 3": (3, 2),
    "ELEVAS - 4": (0, 2),
    "A1 - 1": (8, 26),
    "A1 - 2": (9, 26),
    "A2 - 1": (23, 25),
    "A2 - 2": (23, 26),

}


def distancia_euclidiana(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Gera a matriz de distâncias
distancias = {}

for nome1, coord1 in vertices.items():
    distancias[nome1] = {}
    for nome2, coord2 in vertices.items():
        if nome1 != nome2:
            dist = distancia_euclidiana(coord1, coord2)
            distancias[nome1][nome2] = dist
        else:
            distancias[nome1][nome2] = 0.0  # Distância para si mesmo é zero

# Exibe a matriz
print("Matriz de Distâncias (em metros):\n")
for origem, destinos in distancias.items():
    for destino, distancia in destinos.items():
        print(f"{origem} -> {destino}: {distancia:.2f} m")
    print()

