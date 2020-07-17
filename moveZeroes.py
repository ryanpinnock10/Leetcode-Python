class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # Iterates to the number of times 0 occurs
        for j in range(nums.count(0)):
            nums.remove(0)
            nums.append(0)
            
        # My first attempt
#         zeroCount = 0
#         for i in nums:
#             if i == 0:
#                 nums.remove(0)
#                 zeroCount += 1
#         for i in range(zeroCount):
#             nums.extend('0')
            
#         return (list(map(int, nums)))
