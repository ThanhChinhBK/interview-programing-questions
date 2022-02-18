class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for n in num:
            while k > 0 and stack and stack[-1] > n:
                stack.pop(-1)
                k -= 1
            stack.append(n)
        if k > 0  and stack:
            stack = stack[:-k]
        return str(int(''.join(stack))) if stack else '0'
