class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def pal(l):
            for i in range(len(l)):
                if l[i] != l[len(l)-1-i]:
                    return False
            return True

        for i in words:
            if pal(i):
                return i
        return ""