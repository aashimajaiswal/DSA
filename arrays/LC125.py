class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # convert to lowercase, remove all alpha numeric chars
        cleaned = ""
        for char in s:
            if char.isalnum():
                cleaned += char.lower()

        for i in range(len(cleaned) // 2 ):
            if cleaned[i] != cleaned[len(cleaned)-i-1]:
                return False
        
        return True
        