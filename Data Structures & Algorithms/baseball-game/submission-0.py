class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for token in operations:

            if token == "+":
                stack.append(stack[-1] + stack[-2])
            elif token == "C":
                stack.pop()
            elif token == "D":
                stack.append(2 * stack[-1])
            else:
                stack.append(int(token))

        ans = 0

        for i in stack:
            ans += i

        return ans