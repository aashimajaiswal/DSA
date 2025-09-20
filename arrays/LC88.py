class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # algorithm
        # 3 pointers- end of nums1, nums2, actual end of nums1
        # fill up pointer at nums1 accordingly

        # set pointers
        n1 = m-1
        n2 = n-1
        n1end = m+n-1

        while n2 >= 0:

            if n1 >= 0 and nums1[n1] > nums2[n2]:
                nums1[n1end] = nums1[n1]
                n1 -= 1
            else:
                nums1[n1end] = nums2[n2]
                n2 -= 1

            n1end -=1
        
        return nums1