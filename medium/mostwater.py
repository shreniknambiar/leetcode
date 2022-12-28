class Solution:
    def mostwater(self, strs: List[int]) -> int:
        left = 0
        right = len(strs)-1
        area = 0

        if len(strs) <=1:
            return 0
    
        while(left<right):
            area = max(area, (right - left)*min(strs[left], strs[right]))
            if(strs[left] >= strs[right]):
                right-=1
            else:
                left+=1
        
        return area