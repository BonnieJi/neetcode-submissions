class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(openf, closef, curr):
            if openf < n:
                curr += '('
                dfs(openf+1, closef, curr)
                curr = curr[:-1]

            if closef < openf:
                curr += ')'
                dfs(openf, closef+1, curr)
                curr = curr[:-1]

            if openf==closef==n:
                res.append(curr)
        dfs(0,0, '')
        return res



        