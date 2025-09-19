class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # keep freq counts of both s and t
        # compare to update min_window and min subarray accordingly

        # freq count of t
        t_freq = {}
        for letter in t:
            t_freq[letter] = t_freq.get(letter,0) + 1

        # matched criteria vars
        matched = 0
        req_matched = len(t_freq)

        # other vars
        left = 0
        min_window = ""
        min_len = len(s) + 1
        win_freq = {}

        for right in range(len(s)):

            win_freq[s[right]] = win_freq.get(s[right], 0) + 1

            # updated matched
            if s[right] in t_freq and t_freq[s[right]] == win_freq[s[right]]:
                matched += 1

            # match req met
            while matched == req_matched:

                if min_len > right-left+1:
                    min_window = s[left:right+1]
                    min_len = right-left+1

                # take out left
                win_freq[s[left]] -= 1
                if s[left] in t_freq and t_freq[s[left]] > win_freq[s[left]]:
                    matched -= 1
                    
                left += 1
        
        return min_window


