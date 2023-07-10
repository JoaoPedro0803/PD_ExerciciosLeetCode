class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # Ordenando as tarefas pelo horário de término
        tarefas = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        
        # Alterando as listas startTime, endTime e profit de acordo com a ordenação
        startTime, endTime, profit = zip(*tarefas)
        
        # Calculando p(t) para cada tarefa t
        p = [0] * len(startTime)
        for i in range(len(startTime)):
            for j in range(i - 1, -1, -1):
                if endTime[j] <= startTime[i]:
                    p[i] = j + 1
                    break
        
        # Inicializando o memoization
        memoization = [0] * (len(startTime) + 1)
        
        # Função para calcular o valor máximo
        def M_Compute_Opt(j):
            if j == 0: return 0
            if memoization[j] == 0:
                memoization[j] = max(profit[j-1] + M_Compute_Opt(p[j-1]), M_Compute_Opt(j-1))
            return memoization[j]
        
        # Retornando o valor máximo
        return M_Compute_Opt(len(startTime))