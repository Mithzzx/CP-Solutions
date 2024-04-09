class Solution:
    def maxDepth(self, s: str) -> int:
        c = 0
        m = 0
        for i in s:
            if i == "(":
                c += 1
            elif i == ")":
                if c > m:
                    m = c
                c -= 1
        return m

