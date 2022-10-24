class Solution:
 # Сложность данной программы O(n).

#    Args:
#         n (int): количество команд в турнире
#     Returns:
#         int: количество матчей, 
# сыгранных в турнире до тех пор, 
# пока не будет определен победитель
   
    def numberOfMatches(self, n: int) -> int:
        return n-1