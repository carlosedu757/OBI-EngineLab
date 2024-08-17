#!/usr/bin/env python2.7

import sys
from heapq import heappush, heappop

# Leitura do número de vértices (n) e arestas (m) do grafo
n, m = map(int, sys.stdin.readline().split())

# Inicializa a lista de adjacência para armazenar o grafo
adj = [[] for _ in range(n)]

# Leitura das arestas e preenchimento da lista de adjacência
for _ in range(m):
    u, v, c = map(int, sys.stdin.readline().split())
    u -= 1  # Ajusta para índice baseado em 0
    v -= 1  # Ajusta para índice baseado em 0
    adj[u].append((v, c))  # Adiciona a aresta (v, c) ao vértice u
    adj[v].append((u, c))  # Adiciona a aresta (u, c) ao vértice v (grafo não-direcionado)

# Leitura do vértice inicial
s = int(sys.stdin.readline())
s -= 1  # Ajusta para índice baseado em 0

# Inicialização das distâncias: 'None' indica que o vértice ainda não foi visitado
dist = [None] * n
dist[s] = 0  # Distância do vértice inicial para ele mesmo é 0

# Inicializa as variáveis para armazenar as distâncias mínima e máxima
mindist = None
maxdist = None

# Inicializa a fila de prioridade (heap) e insere o vértice inicial com distância 0
heap = []
heappush(heap, (dist[s], s))

# Processamento do algoritmo de Dijkstra
while len(heap) > 0:
    d, u = heappop(heap)  # Extrai o vértice com a menor distância

    # Se a distância atual é maior que a registrada, continua
    if dist[u] < d:
        continue

    # Atualiza as distâncias mínima e máxima, se necessário
    if u != s:
        if mindist is None or dist[u] < mindist:
            mindist = dist[u]
        if maxdist is None or dist[u] > maxdist:
            maxdist = dist[u]

    # Relaxamento das arestas adjacentes ao vértice u
    for v, c in adj[u]:
        if dist[v] is None or dist[u] + c < dist[v]:  # Verifica se encontrou um caminho mais curto
            dist[v] = dist[u] + c  # Atualiza a distância
            heappush(heap, (dist[v], v))  # Adiciona o vértice adjacente na heap

# Verificações para garantir que as distâncias mínima e máxima foram definidas
assert(mindist is not None)
assert(maxdist is not None)
assert(mindist <= maxdist)
assert(None not in dist)

# Impressão da diferença entre a distância máxima e mínima encontradas
print(maxdist - mindist)
