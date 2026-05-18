class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        total=0
        difference= float("inf")
        for r in range(len(nums)):
            total+= nums[r]
            while total>=target:
                difference= min(difference,r-l+1)
                total-=nums[l]
                l+=1
        if difference ==float('inf'):
            return 0
        else: return difference

        