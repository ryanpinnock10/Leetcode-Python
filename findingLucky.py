class Solution:
    def findLucky(self, arr: List[int]) -> int:
        luck, luckies, ls= -1, Counter(arr), list(set(arr))
        for i in ls:
            if luckies[i] == i:
                luck = max(luck, i)
        return luck 