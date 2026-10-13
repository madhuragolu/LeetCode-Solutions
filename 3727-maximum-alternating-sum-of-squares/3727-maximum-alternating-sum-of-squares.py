class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:

        for i in range(len(nums)):
            nums[i]=nums[i]*nums[i]
        nums.sort()
        
        sub=sum(nums[:len(nums)//2])
        add=sum(nums[len(nums)//2:])
        return add-sub
        
        


