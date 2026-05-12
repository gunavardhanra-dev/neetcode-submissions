class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        if not nums:
            return nums
        if nums[0]>=0:
            return [num**2 for num in nums]
        if nums[-1] < 0: 
            return [num**2 for num in reversed(nums)]
        m=0
        for i,n in enumerate(nums):
            if n>=0:
                m=i
                break

        A,B= nums[m:],[-1*num for num in reversed(nums[:m])]
        def merging(A,B):
            ret=[]
            a=b=0
            while a<len(A) and b<len(B):
                if A[a]<B[b]:
                    ret.append(A[a])
                    a+=1
                else:
                    ret.append(B[b])
                    b+=1
            if a<len(A):
                ret.extend(A[a:])
            else:
                ret.extend(B[b:])
            return [num**2 for num in ret]
        return merging(A,B)
