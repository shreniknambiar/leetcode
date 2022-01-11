class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i=0
        j=0
        l=len(digits)-1
        res=0
	#for last digit not ending with 9
        if digits[l] != 9:
            digits[l] = digits[l]+1
            return digits
        else:
            while i<len(digits):
                dig = digits[l]
                num = dig*(10**i)
                res = res + num
                i+=1
                l-=1
            res+=1
            res_list = []
            while j<res:
                mod = res%10
                res_list.insert(0,mod)
                res=res//10
            return res_list

