from collections import deque

# Define os vetores de movimento para as 4 direções possíveis (direita, esquerda, baixo, cima)
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# Função principal
def main():
    # Leitura do tamanho da matriz (n x n)
    n = int(input())
    
    # Inicialização da matriz 'a' para armazenar os valores lidos
    a = [0] * (n * n)
    
    # Inicializa a matriz de distâncias 'd' com 0
    d = [0] * (n * n)
    
    # Leitura dos valores da matriz
    for i in range(n):
        row = list(map(int, input().split()))
        for j in range(n):
            a[i * n + j] = row[j]

    # Inicializa a deque para o BFS 0-1
    q = deque()
    q.append(0)
    
    # Define a distância inicial do ponto de partida (0,0) como 1
    d[0] = 1
    
    # Loop principal do BFS 0-1
    while q:
        cur = q.popleft()  # Pega o elemento do início da deque
        
        # Percorre as 4 direções possíveis
        for i in range(4):
            new_x = (cur // n) + dx[i]  # Nova coordenada x após o movimento
            new_y = (cur % n) + dy[i]   # Nova coordenada y após o movimento
            new_pos = new_x * n + new_y # Calcula a nova posição linear na matriz
            
            # Verifica se a nova posição é válida e ainda não foi visitada
            if 0 <= new_x < n and 0 <= new_y < n and d[new_pos] == 0:
                d[new_pos] = d[cur] + a[new_pos]  # Atualiza a distância
                
                # Se o valor da célula é 0, insere na frente da deque
                if a[new_pos] == 0:
                    q.appendleft(new_pos)
                else:
                    q.append(new_pos)

    # Imprime a distância mínima para chegar ao canto inferior direito
    print(d[n*n - 1] - 1)

# Chamada da função principal
if __name__ == "__main__":
    main()
