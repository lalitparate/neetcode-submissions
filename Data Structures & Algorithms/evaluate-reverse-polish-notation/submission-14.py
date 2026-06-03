class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def dfs():
            sr = tokens.pop()
            if sr not in "+-*/":
                return int(sr)
            
            ele1 = dfs()
            ele2 = dfs()

            if sr == "+":
                res = int(ele2) + int(ele1)
            elif sr == "-":
                res = int(ele2) - int(ele1)
            elif sr == "*":
                res = int(ele2) * int(ele1)
            elif sr == "/":
                res = int(int(ele2) / int(ele1))
            return res
        
        return dfs()