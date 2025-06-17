import math
import matplotlib.pyplot as plt
import heapq

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

arestas = {
    "PONTO INICIAL - I": ["A2 - 1", "ESCADA 2 - 2", "SALA 02 - 1"],

    "A1 - 1": ["CORREDOR - 1", "A1 - 2", "ELEVAS - 4", "LAB 01 - 1", "B. F", "B. M", "SALA 01 - 1"],
    "A1 - 2": ["A1 - 1", "LAB 01 - 1", "B. F", "B. M", "CORREDOR - 1"],
    "A2 - 1": ["SALA 02 - 1", "PONTO INICIAL - I", "A2 - 2"],
    "A2 - 2": ["SALA 02 - 2", "A2 - 1"],

    "SALA 01 - 1": ["A1 - 1", "CORREDOR - 1", "ELEVAS - 4", "B. M", "B. C - 1", "B. C - 2", "SALA 01 - 2"],
    "SALA 01 - 2": ["SALA 01 - 1", "B. C - 2", "B. C - 1", "PONTO FINAL - J"],
    "SALA 02 - 1": ["A2 - 1", "SALA 02 - 2", "ESCADA 2 - 2", "PONTO INICIAL - I", "ELEVAS - 3", "ELEVAS - 4", "CORREDOR - 2"],
    "SALA 02 - 2": ["A2 - 2", "SALA 02 - 1", "MESA 01 - 1", "MESA 01 - C2 - 1", "MESA 01 - C2 - 2", "MESA 01 - C3 - 1", "MESA 01 - C3 - 2"],

    "ESCADA 1 - 1": ["ESCADA 1 - 2", "LAB 02", "LAB 01 - 2", "LAB 01 - 1", "ELEVAS - 2", "ELEVAS - 3", "B. M", "CORREDOR - 1", "CORREDOR - 2"],
    "ESCADA 1 - 2": ["ESCADA 2 - 1", "ESCADA 1 - 1", "CORREDOR - 2", "CORREDOR - 1", "LAB 01 - 2", "LAB 01 - 1", "ELEVAS - 2", "ELEVAS - 3"],
    "ESCADA 2 - 1": ["ESCADA 1 - 2", "LAB 01 - 2", "ELEVAS - 2", "ELEVAS - 3", "CORREDOR - 2"],
    "ESCADA 2 - 2": ["ESCADA 2 - 1", "SALA 02 - 1", "PONTO INICIAL - I", "LAB 01 - 2", "ELEVAS - 2", "ELEVAS - 3", "ELEVAS - 4", "CORREDOR - 2"],

    "LAB 01 - 1": ["MESA 02 - C3 - 1", "MESA 02 - C3 - 2", "MESA 02 - C4 - 1", "MESA 02 - 2", "LAB 01 - 2", "B. F", "A1 - 1", "A1 - 2", "ESCADA 1 - 1", "ESCADA 1 - 2", "ELEVAS - 1"],
    "LAB 01 - 2": ["LAB 01 - 1", "LAB 02", "B. F", "ESCADA 1 - 2", "ELEVAS - 1", "ESCADA 1 - 1", "ESCADA 2 - 1", "ESCADA 2 - 2", "CORREDOR - 2", "ELEVAS - 2"],
    "LAB 02": ["ESCADA 1 - 1", "CORREDOR - 2", "ELEVAS - 2", "ELEVAS - 3", "LAB 01 - 2"],

    "CORREDOR - 1": ["CORREDOR - 2", "A1 - 1", "A1 - 2", "SALA 01 - 1", "B. M", "B. F", "ELEVAS - 4", "ESCADA 1 - 1", "ESCADA 1 - 2", "ESCADA 2 - 1"],
    "CORREDOR - 2": ["CORREDOR - 1", "ESCADA 1 - 2", "ESCADA 1 - 1", "LAB 02", "SALA 02 - 1", "ELEVAS - 3", "ELEVAS - 4", "ESCADA 2 - 1", "ESCADA 2 - 2", "LAB 01 - 2", "B. F"],

    "B. C - 1": ["B. C - 2", "SALA 01 - 1", "SALA 01 - 2", "B. M"],
    "B. C - 2": ["SALA 01 - 1", "SALA 01 - 2", "B. C - 1"],

    "PONTO FINAL - J": ["SALA 01 - 2"],

    "B. M": ["B. C - 1", "SALA 01 - 1", "A1 - 1", "A1 - 2", "CORREDOR - 1", "ESCADA 1 - 1"],
    "B. F": ["A1 - 1", "A1 - 2", "CORREDOR - 1", "CORREDOR - 2", "ELEVAS - 4", "ELEVAS - 1", "LAB 01 - 2", "LAB 01 - 1", "MESA 02 - C4 - 2", "MESA 02 - 3", "MESA 02 - C1 - 2"],
    
    "SALA 01 - 1": ["B. F", "SALA 01 - 2"],
    "SALA 01 - 2": ["SALA 01 - 1", "B. C - 2", "PONTO FINAL - J"],

    "ELEVAS - 1": ["LAB 01 - 2", "LAB 01 - 1", "MESA 02 - C4 - 2", "B. F"],
    "ELEVAS - 2": ["LAB 01 - 2", "LAB 02", "ESCADA 1 - 1", "ESCADA 1 - 2", "ESCADA 2 - 1", "ESCADA 2 - 2"],
    "ELEVAS - 3": ["ESCADA 1 - 1", "ESCADA 1 - 2", "ESCADA 2 - 1", "ESCADA 2 - 2", "SALA 02 - 1", "CORREDOR - 2"],
    "ELEVAS - 4": ["B. F", "SALA 01 - 1", "A1 - 1", "CORREDOR - 1", "CORREDOR - 2", "SALA 02 - 1", "ESCADA 2 - 2"],

    "MESA 01 - 1": ["SALA 02 - 2", "MESA 01 - C3 - 1", "MESA 01 - C2 - 2"],    
    "MESA 01 - 2": ["MESA 01 - C3 - 2"],
    "MESA 01 - 3": ["MESA 01 - C1 - 2"],
    "MESA 01 - 4": ["MESA 01 - C2 - 1", "MESA 01 - C1 - 2"],
    "MESA 01 - C1 - 1": ["MESA 01 - C2 - 1", "MESA 01 - 4"],
    "MESA 01 - C1 - 2": ["MESA 01 - 3", "MESA 01 - C4 - 1"],
    "MESA 01 - C2 - 1": ["MESA 01 - 4", "MESA 01 - C1 - 1", "SALA 02 - 2"],
    "MESA 01 - C2 - 2": ["SALA 02 - 2", "MESA 01 - 1"],
    "MESA 01 - C3 - 1": ["MESA 01 - 1", "SALA 02 - 2"],
    "MESA 01 - C3 - 2": ["MESA 01 - 2", "MESA 01 - C4 - 2", "SALA 02 - 2"],
    "MESA 01 - C4 - 1": ["MESA 01 - C1 - 2"],
    "MESA 01 - C4 - 2": ["MESA 01 - C3 - 2"],

    "MESA 02 - 1": ["MESA 02 - C3 - 1"],
    "MESA 02 - 2": ["MESA 02 - C3 - 2", "MESA 02 - C4 - 1", "LAB 01 - 1"],
    "MESA 02 - 3": ["MESA 02 - C1 - 2", "MESA 02 - C4 - 2", "B. F"],
    "MESA 02 - 4": ["MESA 02 - C1 - 1"],
    "MESA 02 - C1 - 1": ["MESA 02 - 4"],
    "MESA 02 - C1 - 2": ["MESA 02 - 3", "MESA 02 - C4 - 2", "B. F"],
    "MESA 02 - C3 - 1": ["MESA 02 - 1", "LAB 01 - 1"],
    "MESA 02 - C3 - 2": ["MESA 02 - 2", "MESA 02 - C4 - 1", "LAB 01 - 1"],
    "MESA 02 - C4 - 1": ["MESA 02 - 2", "MESA 02 - C3 - 2", "LAB 01 - 1"],
    "MESA 02 - C4 - 2": ["MESA 02 - 3", "MESA 02 - C1 - 2", "B. F", "ELEVAS - 1"],
}



def distancia_euclidiana(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)


distancias = {}

for origem, vizinhos in arestas.items():
    distancias[origem] = {}
    for destino in vizinhos:
        coord1 = vertices[origem]
        coord2 = vertices[destino]
        dist = distancia_euclidiana(coord1, coord2)
        distancias[origem][destino] = dist

print("Matriz de Distâncias (em metros):\n")
for origem, destinos in distancias.items():
    for destino, distancia in destinos.items():
        print(f"{origem} -> {destino}: {distancia:.2f} m")
    print()

def a_estrela(inicio, fim):
    # Fila de prioridade: (f_score, nó atual)
    fila = []
    heapq.heappush(fila, (0, inicio))

    # g: custo do início até o nó atual
    g = {inicio: 0}

    # f: custo total estimado (g + h)
    f = {inicio: distancia_euclidiana(vertices[inicio], vertices[fim])}

    # Para reconstruir o caminho
    anterior = {}

    while fila:
        _, atual = heapq.heappop(fila)

        if atual == fim:
            # Reconstrói o caminho
            caminho = []
            while atual in anterior:
                caminho.append(atual)
                atual = anterior[atual]
            caminho.append(inicio)
            caminho.reverse()
            return caminho

        for vizinho in arestas.get(atual, []):
            custo = distancias[atual][vizinho]
            novo_g = g[atual] + custo

            if vizinho not in g or novo_g < g[vizinho]:
                g[vizinho] = novo_g
                h = distancia_euclidiana(vertices[vizinho], vertices[fim])
                f[vizinho] = novo_g + h
                anterior[vizinho] = atual
                heapq.heappush(fila, (f[vizinho], vizinho))

    return None  # Se não encontrar caminho


caminho = a_estrela("PONTO INICIAL - I", "PONTO FINAL - J")

if caminho:
    print("\nMelhor caminho encontrado pelo A*:")
    for passo in caminho:
        print(f"→ {passo}")
else:
    print("Nenhum caminho encontrado.")

