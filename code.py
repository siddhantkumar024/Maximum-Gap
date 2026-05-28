class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n=len(nums)
        nums.sort()
        maxval=0
        for i in range(n-1):
            print(i)
            d=nums[i+1]-nums[i]
            maxval=max(d,maxval)
        return maxval
        
