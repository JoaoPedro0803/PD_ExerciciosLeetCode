class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Inicializar a matriz dp com zeros
        dp = [[0]*n for _ in range(m)]
        
        # Preencher a primeira linha e a primeira coluna com 1, 
        # pois há apenas um caminho para chegar a cada célula na primeira linha/coluna
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1

        # Para cada célula na matriz (excluindo a primeira linha e a primeira coluna),
        # o número de caminhos para chegar a essa célula é a soma do número de caminhos
        # para chegar à célula acima dela e à célula à sua esquerda.
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        # O número de caminhos para chegar ao canto inferior direito é armazenado em dp[m-1][n-1]
        return dp[m-1][n-1]
    
    # https://leetcode.com/problems/unique-paths/description/