class Solution(object):
    def minimumSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=[]
        for i in range(len(nums)-2):
            for j in range(i+1,len(nums)-1):
                for k in range(j+1,len(nums)):
                    if nums[i]<nums[j] and nums[k]<nums[j]:
                        l.append(nums[i] + nums[j] + nums[k])
        if l:
            return min(l)   
        else:
            return -1                    
