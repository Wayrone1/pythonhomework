
#Сложность данной программы O(n * log(k)), что равно O(n).

#Args:                   
#   nums (список): целочисленный список с числами
#   k (int): k  по величине элемент.
       
# Returns:
#     int: k по величине элемент в массиве

class Solution:            
    def removeOuterParentheses(self, s: str) -> str:
        st = []
        finansw = []
        ct=0
        for val in s:
            st.append(val)
            if val=='(':
                ct+=1
            elif val==')':
                ct-=1
            if ct==0:
                finansw+=st[1:-1]
                st=[]
        
        return "".join(finansw)
