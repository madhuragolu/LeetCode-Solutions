class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        n=len(candidates)
        candidates.sort()
        ans=[]
        def rec(idx,t,arr):
            if t==0:
                ans.append(arr.copy())
                return
            if idx==n:
                return
            for i in range(idx,n):
                if i>idx and candidates[i]==candidates[i-1]:
                    continue
                if candidates[i]>t:
                    break
                arr.append(candidates[i])
                rec(i+1,t-candidates[i],arr)
                arr.pop()
        rec(0,target,[])
        return ans
