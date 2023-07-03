from collections import deque

class Solution:
    def minCost(self, grade):
        # Inicializa o número de linhas e colunas
        num_linhas, num_colunas = len(grade), len(grade[0])
        
        # Inicializa a matriz de custos com "infinito" para todas as células
        custos = [[float('inf')] * num_colunas for _ in range(num_linhas)]
        
        # Define o custo da célula inicial como 0
        custos[0][0] = 0
        
        # Define as possíveis direções de movimento (direita, esquerda, para baixo, para cima)
        direcoes = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        # Cria uma fila para armazenar as células a serem visitadas, começando pela célula inicial
        fila = deque([(0, 0)])
        
        # Enquanto houver células na fila para visitar
        while fila:
            # Remove e obtém a próxima célula da fila
            x, y = fila.popleft()
            
            # Para cada direção possível
            for i, (dx, dy) in enumerate(direcoes):
                # Calcula as coordenadas da célula vizinha
                novo_x, novo_y = x + dx, y + dy
                
                # Se a célula vizinha está dentro da grade
                if 0 <= novo_x < num_linhas and 0 <= novo_y < num_colunas:
                    # Calcula o custo para mover para a célula vizinha
                    # Se a direção da célula atual é a mesma da direção atual, o custo é o mesmo da célula atual
                    # Caso contrário, o custo é o da célula atual mais 1 (pois precisa mudar a direção)
                    custo = custos[x][y] if grade[x][y] == i + 1 else custos[x][y] + 1
                    
                    # Se o novo custo é menor que o custo atual da célula vizinha
                    if custo < custos[novo_x][novo_y]:
                        # Atualiza o custo da célula vizinha
                        custos[novo_x][novo_y] = custo
                        
                        # Se a direção da célula atual é a mesma da direção atual
                        # Adiciona a célula vizinha no início da fila para dar prioridade ao movimento sem mudança de direção
                        # Caso contrário, adiciona a célula vizinha no final da fila
                        if grade[x][y] == i + 1:
                            fila.appendleft((novo_x, novo_y))
                        else:
                            fila.append((novo_x, novo_y))
                            
        # Retorna o custo da célula inferior direita, que é o custo mínimo para tornar a grade válida
        return custos[num_linhas - 1][num_colunas - 1]

#https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/description/