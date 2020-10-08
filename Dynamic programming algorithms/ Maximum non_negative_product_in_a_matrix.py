class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        memo = {}
        m = len(grid)
        n = len(grid[0])
        MOD = 10**9+7
        
        def dp(i, j):
            if (i, j) in memo:
                return memo[(i,j)]
            if i == 0 and j == 0:
                res = grid[i][j], grid[i][j]
            else:
                candidates = []
                if i > 0:
                    top = dp(i-1, j)
                    candidates.extend([top[0]*grid[i][j], top[1]*grid[i][j]])
                if j > 0:
                    left = dp(i, j-1)
                    candidates.extend([left[0]*grid[i][j], left[1]*grid[i][j]])
                res = max(candidates), min(candidates)

            memo[(i,j)] = res
            return res

        res = dp(m-1, n-1)
        return res[0] % MOD if res[0] >= 0 else -1