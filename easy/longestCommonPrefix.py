class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        low = strs[0]
        j=0
        for i in range(0,len(strs)-1):
            if(len(strs[i])<len(strs[i+1])):
                low = strs[i]
                
        while j < len(strs):
            if strs[j].startswith(low):
                j=j+1
                continue
            else:
                low=low[:-1]
                j=0
        
        return low
