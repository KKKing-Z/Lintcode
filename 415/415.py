class Solution:
    """
    @param s: A string
    @return: Whether the string is a valid palindrome
    """
    def isPalindrome(self, s):
        # write your code here
        i = 0
        j = len(s) - 1
        
        while i < j :
            if 'A' <= s[i] <= 'Z' or 'a' <= s[i] <= 'z' or '0' <= s[i] <= '9':
                if 'A' <= s[j] <= 'Z' or 'a' <= s[j] <= 'z' or '0' <= s[j] <= '9':
                    if (s[i].upper() != s[j].upper()):
                        return False
                    
                    i += 1
                    j -= 1
                else:
                    j -= 1
                    continue
            else:
                i += 1
                continue
        
        return True