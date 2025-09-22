# Precomputation
Calculate values to reduce complexity

## Leetcode: Product of Array except Self
- Link
- Mistakes
    - multiplier to be 1 always in case 1st/last element is 0
- Code
```python
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        # ...L... 4 ...R...
        # ans at 4 is L*R

        n = len(nums)
        L = [1] * n
        for i in range(1,n):
            L[i] = L[i-1] * nums[i-1]
        
        R = [1] * n
        for j in range(n-2,-1,-1):
            R[j] = R[j+1] * nums[j+1]
        
        answer = [1] * n
        for k in range(n):
            answer[k] = L[k]*R[k]
        
        return answer
```