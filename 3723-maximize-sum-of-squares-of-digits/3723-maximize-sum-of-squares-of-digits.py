class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
  
        if sum > num * 9 or sum < 0:
            return ""

        res = []
        def rec(rem_sum, arr):
           
            if len(arr) == num:
                if rem_sum == 0:
                    res.append("".join(map(str, arr)))
                return
            
        
            for i in range(9, -1, -1):
              
                if rem_sum >= i and rem_sum - i <= (num - len(arr) - 1) * 9:
                    arr.append(i)
                    rec(rem_sum - i, arr)
                    arr.pop()
                   
                    if res:
                        return

        rec(sum, [])
        return res[0] if res else ""