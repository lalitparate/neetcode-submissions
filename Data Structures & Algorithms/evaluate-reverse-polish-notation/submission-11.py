class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["+", "-", "*", "/"]
        res = 0
        for sr in tokens:

            if sr in operators:
                ele1 = stack.pop()
                ele2 = stack.pop()

                if sr == "+":
                    res = int(ele2) + int(ele1)
                elif sr == "-":
                    res = int(ele2) - int(ele1)
                elif sr == "*":
                    res = int(ele2) * int(ele1)
                elif sr == "/":
                    print(ele2, ele1)
                    res = int(float(ele2 / ele1))

                stack.append(res)
            else:
                stack.append(int(sr))
        return stack[0]
            