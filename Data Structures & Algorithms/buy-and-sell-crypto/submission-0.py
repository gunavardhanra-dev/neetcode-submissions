class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r=0,1
        temp=0
        while r<len(prices):
            pro= prices[r]-prices[l]
            if prices[l]>prices[r]:
                l=r
            if pro>temp:
                temp=pro
            r+=1
        return temp


        