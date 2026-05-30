class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix=[]
        total_count=0
        for i in nums:
            total_count= total_count+i
            self.prefix.append(total_count)

    def sumRange(self, left: int, right: int) -> int:
        if left==0:
            return self.prefix[right]
        return self.prefix[right] - self.prefix[left-1]

        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)