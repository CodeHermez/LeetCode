class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        lst = sorted(nums1 + nums2)
        size = len(lst)
        print(lst)
        if size%2==0:
            print("1st: ",lst[(size//2-1)])
            print("2nd: ",lst[(size//2)])
            print("result: ", float((lst[size//2-1] + lst[size//2]))/2)
            return float(lst[size//2-1] + lst[size//2])/2
        else:
            return lst[(size//2)]