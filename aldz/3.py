class Solution:
   #Сложность данной программы O(n).
#       Args:
#         jewels (str): драгоценности, представляющие типы камней, которые являются драгоценностями.
# камни (str): камни, которые у вас есть.
#     Returns:
#         int: сколько камней у вас есть, а также драгоценности. 
   
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        total =0
        for stone in stones :
            if stone in jewels :
                total+=1
        return total

       