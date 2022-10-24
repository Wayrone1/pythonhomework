class Solution:
    #Сложность данной программы O(n).
    
    #Args:
        #num (int): число, которое мы уменьшаем до нуля
   # Returns:
        #int:  количество шагов, чтобы уменьшить его до нуля.
   
    def numberOfSteps (self, num: int) -> int:
        a = 0 # считает шаги 
        while num > 0:
            if num % 2: num -= 1
            else: num /= 2
            a += 1
        return a