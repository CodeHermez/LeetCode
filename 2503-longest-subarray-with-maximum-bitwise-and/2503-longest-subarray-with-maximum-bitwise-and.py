import math
class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mx = max(nums)
        counter = 0
        lst=[]
        for x in nums:
            print(counter)
            if not x==mx:
                lst.append(counter)
                counter = 0
                continue
            counter+=1
        lst.append(counter)
        print(lst)
        return max(lst)



        return lie

        