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
        