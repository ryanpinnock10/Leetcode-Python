class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #Implemented the binary search method to gauge where to start adding 
        #list elements to see if they ae equal to the target 
        start, end = 0, len(numbers) -1
        
        while start < end:
            sumC = numbers[start] + numbers[end]
            if sumC == target:
                return [start +1,end+ 1]
            elif sumC < target:
                start += 1
            else:
                end -= 1
            
        #return [-1, -1]