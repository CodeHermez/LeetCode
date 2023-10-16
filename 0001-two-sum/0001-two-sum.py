class Solution(object):
    def twoSum(self, nums, target):
        for x in range(len(nums)):
            for y in range(len(nums)):
                if(x!=y and (nums[x]+nums[y])==target):
                    print("[",nums[y],",",nums[x],"]")
                    return (y, x)
                    