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
