class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        newArr, y = list(), 0
        for i in range(len(nums)):
            y += nums[i]
            nums[i] = y
        return nums