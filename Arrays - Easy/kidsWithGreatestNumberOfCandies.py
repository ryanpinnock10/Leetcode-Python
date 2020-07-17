class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        M = max(candies)
        return [candy + extraCandies >= M for candy in candies]
        #My first attempt 
        # kids, favKid = [True]*len(candies), max(candies)
        # for i in range(len(candies)):
        #     if (candies[i] + extraCandies) < favKid:
        #         kids[i] = False
        # return kids