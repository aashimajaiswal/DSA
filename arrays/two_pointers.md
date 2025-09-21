# 2 Pointers

## Leetcode 88: Merge Sorted Array
- Link: https://leetcode.com/problems/merge-sorted-array/description/
- Mistakes
    - nums2 should be over
    - update relevant pointers in if blocks
    - check if index is not negative
- Code
```
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
```
## Leetcode 75: Sort Colors
- Link: https://leetcode.com/problems/sort-colors/description/
- Mistakes
    - Counting sort: indexes
    - Dutch National Flag: not to update mid when see 2
- Code
```
# Algorithm 1: Counting Sort Double Pass
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        # algo 1: counting sort: double pass
        counts = [0,0,0]
        for color in nums:
            counts[color] += 1

        R, W, B = counts
        nums[0:R] = R * [0]
        nums[R:R+W] = W * [1]
        nums[R+W:R+W+B] = B * [2]

        return nums

# Algorithm 2: Dutch National Flag (Single Pass)
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        # Algo 2: DNF
        # 3 pointer: start, mid, end
        # updates when mid is
            # 0 // mid and start swap, both += 1
            # 1 // mid += 1
            # 2 // mid and end swap, end -= 1
        
        start = mid = 0
        end = len(nums) - 1
        
        while mid <= end:

            if nums[mid] == 0:
                nums[start], nums[mid] = nums[mid], nums[start]
                mid += 1
                start += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[end], nums[mid] = nums[mid], nums[end]
                end -= 1
        
        return nums
        
```
## Leetcode 647: Pallindromic Substrings
- Link: https://leetcode.com/problems/palindromic-substrings/description/
- Mistakes
    - dont forget about even length strings
- Code
```
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """

        # we check for both even length and odd len
        # for odd -> center is the element itself, l=r=i
        # for even -> center is between the 2 elements, l,r = i, i+1
        
        count = 0
        left = 0
        right = 0
        
        for i in range(len(s)):

            # odd pallindrome check
            left = right = i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            
            # even pallindrome check
            left, right = i, i+1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            
        return count
```