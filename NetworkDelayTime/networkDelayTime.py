class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        inf = float('inf')
        # Inicializando Memoization com valor de infinito em todas as posições
        Memoization = [inf] * (n + 1) 
        # Inicializando matriz de nós sucessores 
        sucessor = [None] * (n + 1)
        # Definindo distância mínima do nó final igual a 0
        Memoization[k] = 0

        for _ in range(n - 1):
            # Variável para verificar se houve alterações nas distâncias mínimas
            alterouDistanciaMinima = False
            for noPredecessor, noSucessor, valorAresta in times:
                if Memoization[noPredecessor] + valorAresta < Memoization[noSucessor]:
                    # Atualizando a distância mínima e o nó sucessor
                    Memoization[noSucessor] = Memoization[noPredecessor] + valorAresta
                    sucessor[noSucessor] = noPredecessor
                    alterouDistanciaMinima = True
            # Dá um break na execução se não houve alteração nas distâncias mínimas
            if alterouDistanciaMinima == False:
                break

        # For para verificar se há ciclos negativos (Bellman Ford não funciona em ciclos negativos)
        for noPredecessor, noSucessor, valorAresta in times:
            if Memoization[noPredecessor] + valorAresta < Memoization[noSucessor]:
                return -1

        # Calculando o tempo máximo entre as distâncias mínimas
        tempoMaximo = max(Memoization[1:])
        if tempoMaximo < inf:
            return tempoMaximo
        else:
            return -1
            