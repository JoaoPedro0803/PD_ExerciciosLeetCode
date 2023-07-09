class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        quantNumeros = len(nums)
        # Se a quantidade de números no array for 0, retorna 0
        if quantNumeros == 0:
            return 0

        # Array para tamanho das sequências
        tamanhoSequencias = [1] * quantNumeros
        # Array para número de sequências crescentes
        numSequenciasCrescentes = [1] * quantNumeros

        # For para calcular os tamanhos e predecessores
        for j in range(quantNumeros):
            for i in range(j):
                if nums[i] < nums[j] and tamanhoSequencias[i] + 1 > tamanhoSequencias[j]:
                    # Atualizando o tamanho e o número de sequências em j
                    tamanhoSequencias[j] = tamanhoSequencias[i] + 1
                    numSequenciasCrescentes[j] = numSequenciasCrescentes[i]
                elif nums[i] < nums[j] and tamanhoSequencias[i] + 1 == tamanhoSequencias[j]:
                    # Aumentando o número de sequências em j
                    numSequenciasCrescentes[j] += numSequenciasCrescentes[i]

        # maiorSequencia armazenando o valor da(s) maior(es) sequência(s)
        maiorSequencia = max(tamanhoSequencias)

        quantMaioresSequencias = 0
        # For para contar a quantidade de maiores sequências
        for i in range(quantNumeros):
            if tamanhoSequencias[i] == maiorSequencia:
                quantMaioresSequencias += numSequenciasCrescentes[i]

        return quantMaioresSequencias
