INF = 999999
N = 6
NOMBRES = ["A", "B", "C", "D", "E", "F"]


def crear_matriz():
    mat = [[INF] * N for _ in range(N)]
    aristas = [
        (0, 1, 4),
        (0, 2, 2),
        (1, 2, 1),
        (1, 3, 5),
        (2, 4, 10),
        (3, 4, 3),
        (3, 5, 2),
        (4, 5, 1),
    ]
    for u, v, peso in aristas:
        mat[u][v] = peso
        mat[v][u] = peso
    return mat


def dijkstra(mat, origen):
    dist = [INF] * N
    visitado = [False] * N
    pred = [-1] * N
    dist[origen] = 0

    for _ in range(N):
        u = -1
        min_dist = INF
        for j in range(N):
            if not visitado[j] and dist[j] < min_dist:
                min_dist = dist[j]
                u = j
        if u == -1:
            break
        visitado[u] = True

        for j in range(N):
            if not visitado[j] and mat[u][j] < INF:
                if dist[u] + mat[u][j] < dist[j]:
                    dist[j] = dist[u] + mat[u][j]
                    pred[j] = u

    return dist, pred


def reconstruir_camino(pred, destino):
    camino = []
    actual = destino
    while actual != -1:
        camino.append(actual)
        actual = pred[actual]
    camino.reverse()
    return camino


def main():
    mat = crear_matriz()
    origen = 0
    destino = 5
    dist, pred = dijkstra(mat, origen)

    print(f"=== Distancias minimas desde {NOMBRES[origen]} ===")
    for i in range(N):
        valor = dist[i] if dist[i] < INF else "INF"
        print(f"  {NOMBRES[origen]} -> {NOMBRES[i]} = {valor}")

    camino = reconstruir_camino(pred, destino)
    print()
    print("Camino optimo: " + " -> ".join(NOMBRES[v] for v in camino))
    print(f"Distancia total: {dist[destino]}")


if __name__ == "__main__":
    main()
