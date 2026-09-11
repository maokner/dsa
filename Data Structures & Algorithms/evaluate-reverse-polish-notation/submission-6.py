class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = "+-/*"
        for token in tokens:
            if token not in ops:
                stack.append(int(token))
            else:
                term2 = stack.pop()
                term1 = stack.pop()
                if token == "+":
                    stack.append(term1 + term2)
                elif token == "-":
                    stack.append(term1 - term2)
                elif token == "*":
                    stack.append(term1 * term2)
                else:
                    val = abs(term1) // abs(term2)
                    if term1 < 0:
                        val *= -1
                    if term2 < 0:
                        val *= -1
                    stack.append(val)
        return stack[0]
            
        