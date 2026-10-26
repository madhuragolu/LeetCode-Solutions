class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hMap = {}
        for index,num in enumerate(nums):
            diff = target-num
            if diff in hMap:
                return [hMap[diff],index]
            hMap[num]=index
        return