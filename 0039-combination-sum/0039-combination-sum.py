class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        ans=[]
        def com(idx,t,arr):
            if idx>=len(candidates):
                if t==0:
                    ans.append(arr.copy())
                return
            if candidates[idx]<=t:
                arr.append(candidates[idx])
                com(idx,t-candidates[idx],arr)
                arr.pop()
            com(idx+1,t,arr)
        com(0,target,[])
        return ans