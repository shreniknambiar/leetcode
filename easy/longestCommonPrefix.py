class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        low = strs[0]
        j=0     
        while j < len(strs):
            if strs[j].startswith(low):
                j=j+1
                continue
            else:
                low=low[:-1]
                j=0
        
        return low
