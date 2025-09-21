# Sort Array

## Tricks
- if array arranged, or partly arranged -> binary search possible
    - hence interviewer might be looking for a solution faster than O(n)
- sometimes sorting the array makes the problem much simpler
    - python inbuilt timsort O(nlogn)

## Leetcode 56: Merge Intervals
- Link: https://leetcode.com/problems/merge-intervals/description/
- Mistakes
    - sort first
    - list.sort(key = lamda: x:x[0])
- Code
```python
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """

        # first sort on firt element
        intervals.sort(key = lambda x: x[0])

        merged = []
        
        # compare if there is an overlap
        for interval in intervals:
            # no overlap, add whole interval
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            # else update the existing interval in merged
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        
        return merged
```