# Definindo as constantes
MAX_CITIES = 100
INF = float('inf')  # INF é representado por um número muito grande

# Criando a matriz de adjacência com tamanho MAX_CITIES + 1 e inicializando com INF
m = [[INF] * (MAX_CITIES + 1) for _ in range(MAX_CITIES + 1)]

# Leitura do número de cidades (N) e número de estradas (M)
N, M = map(int, input().split())

# Leitura das estradas e pesos, e atualização da matriz
for _ in range(M):
    a, b, c = map(int, input().split())
    if m[a][b] > 100 or m[a][b] > c:
        m[a][b] = m[b][a] = c

# Inicializando a diagonal principal com 0
for i in range(N):
    m[i][i] = 0

# Algoritmo de Floyd-Warshall
for i in range(N):
    for j in range(N):
        for k in range(N):
            m[j][k] = min(m[j][k], m[j][i] + m[i][k])

# Encontrando o menor dos maiores caminhos mínimos
menor = INF
for i in range(N):
    maior = -1
    for j in range(N):
        maior = max(maior, m[j][i])
    if maior < menor:
        menor = maior

# Saída do resultado
print(menor)
