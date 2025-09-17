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