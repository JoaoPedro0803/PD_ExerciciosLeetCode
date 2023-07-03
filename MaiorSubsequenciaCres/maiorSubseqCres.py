class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Obtemos o tamanho do array de entrada
        n = len(nums)
        
        # Inicializamos a lista L com n uns. 
        # Cada número por si só é uma subsequência crescente de comprimento 1.
        L = [1] * n

        # Iteramos sobre cada elemento do array nums
        for j in range(n):
            
            # Para cada elemento nums[j], comparamos com todos os elementos anteriores
            for i in range(j):
                
                # Se encontrarmos um número menor (nums[i] < nums[j]) e se a maior subsequência
                # crescente até o momento mais um é maior do que a subsequência atual, 
                # então atualizamos L[j] 
                if nums[i] < nums[j] and 1 + L[i] > L[j]:
                    L[j] = 1 + L[i]

        # Após verificar todos os elementos, retornamos o maior valor em L, 
        # que representa a maior subsequência crescente na lista nums.
        return max(L)
    #https://leetcode.com/problems/longest-increasing-subsequence/description/