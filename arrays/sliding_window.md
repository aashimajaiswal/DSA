# Sliding Window Technique

## Overview
The sliding window technique helps optimize computations by avoiding redundant calculations. Instead of recalculating from scratch, it maintains a "window" of elements and efficiently updates the result.

## Fixed Window Approach

### Problem Example
Find a subarray of size `k = 4` that gives the maximum sum.

**Array:** `[3, 5, 2, 1, 5, 2, 6, 7]`

### Brute Force Solution
- Calculate sums for all 4-length subarrays
- Shift `(n - k + 1)` times
- Add `k` elements together each time
- **Time Complexity:** `O(n × k)`

### Optimized Sliding Window Solution
**Key Insight:** Only the first and last elements change when sliding the window.

**Formula:** `sum(n) = sum(n-1) + last(n) - first(n-1)`

**Time Complexity:** `O(n)` - significant improvement when `k` is large

## Variable Window (Two Pointer) Approach

### Problem Example
Find the longest subarray with sum ≤ `S = 15`

**Array:** `[3, 1, 5, 6, 9]`

### Algorithm
1. Initialize two pointers: `left = -1`, `right = 0`
2. **Expand window:** Move `right` pointer while `sum ≤ S`
   - Track current length and sum
3. **Contract window:** When `sum > S`, move `left` pointer forward (`left++`)
4. **Continue:** Resume expanding when `left` and `right` are adjacent
5. **Time Complexity:** `O(n)`

### Implementation Pattern
```
left = 0, right = 0, sum = 0, maxLength = 0

while right < array.length:
    sum += array[right]

    while sum > target:
        sum -= array[left]
        left++

    maxLength = max(maxLength, right - left + 1)
    right++
```

## Key Benefits
- **Time Optimization:** From `O(n × k)` to `O(n)`
- **Space Efficient:** Constant extra space
- **Versatile:** Works for both fixed and variable window problems

## Leetcode 3. Longest Substring Without Repeating Characters (Medium)
- Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
- Mistakes
    - left pointer to be after previous occurance of duplicate just seen
    - if duplicate seen make sure its previous occurance is in the sliding window
- Code
    ```
    class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        # Logic
        # 2 pointers left and right
        # right moves by 1 everytime
        # left only moves when a character occurs again
        # when right sees a duplicate
        # checks be looking at seen dict (has element, location seen)
        # checks if seen before is in the current sliding window , like for "abba"
        # because if its repeated but is not in the window, its not repeated in the substring

        left = 0
        max_len = 0
        seen = {}

        for right in range(len(s)):

            # check if its seen
            # if its seen check if its in the sliding window
            if s[right] in seen and seen[s[right]] >= left:
                left = seen[s[right]] + 1

            # register seen in dict
            seen[s[right]] = right

            max_len = max(max_len, right - left + 1)

        return max_len        
    ```
