# Solução para o problema "Caminho das Pontes" da OBI 2009
# por: Igor Ribeiro de Assis

import sys

# Definições de constantes
MAXN = 1010
INF = float('inf')  # Representa infinito como um valor muito grande

# Inicializa as matrizes de adjacência e os vetores de visitados e distâncias
A = [[INF] * MAXN for _ in range(MAXN)]
visitado = [0] * MAXN
dis = [INF] * MAXN

def dijkstra():
    # Inicializa a distância do nó de origem (0) como 0
    dis[0] = 0

    while True:
        no = -1
        # Encontra o nó não visitado com a menor distância conhecida
        for i in range(n):
            if not visitado[i] and (no == -1 or dis[i] < dis[no]):
                no = i

        # Se não há mais nós a processar, saia do loop
        if no == -1:
            break
        
        # Marca o nó como visitado
        visitado[no] = 1

        # Atualiza as distâncias dos vizinhos do nó atual
        for i in range(n):
            if dis[no] + A[no][i] < dis[i]:
                dis[i] = dis[no] + A[no][i]

    # Retorna a distância mínima até o último nó
    return dis[n-1]

def main():
    # Leitura do número de nós (n) e arestas (m)
    global n, m
    n, m = map(int, input().split())
    
    # Adiciona 2 para considerar as bordas como pilares
    n += 2

    # Leitura das arestas e atualização da matriz de adjacência
    for _ in range(m):
        s, t, b = map(int, input().split())
        A[s][t] = A[t][s] = b  # Bidirecionalidade das pontes

    # Executa o algoritmo de Dijkstra e imprime o resultado
    print(dijkstra())

# Executa o programa principal
if __name__ == "__main__":
    main()
