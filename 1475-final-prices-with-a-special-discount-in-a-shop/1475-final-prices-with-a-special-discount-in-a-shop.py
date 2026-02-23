from collections import deque
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        q = deque()
        ans = [-1] * len(prices)

        for idx, p in enumerate(prices):
            while q and q[-1][1] >= p:
                t_idx, t_val = q.pop()
                ans[t_idx] = t_val - p
                print(t_idx, t_val, p)

            q.append((idx, p))
    
        for i in range(len(prices)):
            if ans[i] == -1:
                ans[i] = prices[i]
        
        return ans
            


        