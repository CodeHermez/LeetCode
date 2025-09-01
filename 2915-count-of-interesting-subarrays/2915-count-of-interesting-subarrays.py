from collections import defaultdict
class Solution(object):
    def countInterestingSubarrays(self, nums, modulo, k):
        """
        :type nums: List[int]
        :type modulo: int
        :type k: int
        :rtype: int
        """
        i = defaultdict(int)
        i[0]=1
        ans=0
        behind=0
        for val in nums:
            if val%modulo==k:
                behind+=1
            mod_ans = behind%modulo
            t=(mod_ans-k+modulo)%modulo
            ans+=i[t]
            i[mod_ans]+=1
        return ans