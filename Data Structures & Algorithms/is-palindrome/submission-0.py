class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = s.replace(" ", "")
        for i in s:
            if i.isalnum() == False:
                s = s.replace(i, "")
        left = 0 
        right = len(s) - 1

        for i in range(len(s)):
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        
        return True