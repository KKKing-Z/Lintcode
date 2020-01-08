class Solution:
    """
    @param s: a string which consists of lowercase or uppercase letters
    @return: the length of the longest palindromes that can be built
    """
    def longestPalindrome(self, s):
        # write your code here
        lis = []
        
        for c in s:
            if c in lis:
               lis.remove(c)
            else:
                lis.append(c)
        
        if len(lis) == 0:
            return len(s)
        else:
            return len(s) - len(lis) + 1