class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """j=0
        for i in range(0,len(nums)-1):
            for k in range(i+1,len(nums)):
                if target-nums[i]==nums[k]:
                    return [i,k] """
        dic={}
        for i, v in enumerate(nums):
            dic[v]=i

        for i, v in enumerate(nums):
            diff=target-v
            if diff in dic and dic[diff]!=i:
                return [i,dic[diff]]
        return []
           