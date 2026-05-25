class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        dic={}
        for i in nums:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        
        return any(map(lambda x:x>1, dic.values()))