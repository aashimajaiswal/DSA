class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # If open parentheses -> push to stack
        # if close parentheses -> pop stack, check if match if not return false else return true

        stack = []
        mapping = {')':'(', ']':'[', '}': '{'}

        for char in s:
            
            if char in mapping:

                # pop stack
                top = stack.pop() if stack else '#'

                # see match
                if top != mapping[char]:
                    return False
            
            else:
                stack.append(char)

        return len(stack) == 0