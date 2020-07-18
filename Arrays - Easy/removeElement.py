class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i in range(nums.count(val)):
            nums.remove(val)
        return len(nums)

        #very similar to removing zeroes question
        #moving to hash tables or company specific questions next 