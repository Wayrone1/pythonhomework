class Solution:

# Сложность данной программы O(n*log(n)).
    
#     Args:
#         arr (list): массив различных целых чисел
#     Returns:
#         list: список пар в порядке возрастания (по отношению к парам)


    
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        
        arr.sort()          # сортируем список стандартным методом

               # найденные пары с разницей в abc, равной минимальной разнице в abc, будут сохранены здесь
        min_abs = 10**6
        for i in range(1, len(arr)):    #ищем минимальную разницу между элементами
            pair_abs = abs(arr[i] - arr[i-1])      
            if pair_abs < min_abs:                  
                min_abs = pair_abs                  
                lst = []                         
            if pair_abs == min_abs:                 
                lst.append([arr[i-1], arr[i]])    # если минимальная разница равна разности чисел добавляем в список

        return lst  