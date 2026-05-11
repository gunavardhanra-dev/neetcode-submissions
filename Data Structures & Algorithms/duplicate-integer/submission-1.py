class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
      length_1=len(nums)
      nums=set(nums)   
      if length_1 > len(nums):
        return True
      return False
            