class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        ans=[]
        def rec(idx):
            if idx==len(nums):
                ans.append(nums.copy())
                return
            for i in range(idx,len(nums)):
                nums[i],nums[idx]=nums[idx],nums[i]
                rec(idx+1)
                nums[i],nums[idx]=nums[idx],nums[i]
        rec(0)
        return ans
