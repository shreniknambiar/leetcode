from xmlrpc.client import boolean


class Solution:
    def pal(self, s: str, l: int, r: int ) -> bool:
        while(l<r):
            if(s[l]!=s[r]):
                return False
        return True
    def almostPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while(l<r):
            if(s[l]!= s[r]):
                return self.pal(s, l+1, r) or self.pal(s, l, r-1)
        return True
