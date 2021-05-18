class Solution(object):
    def lengthOfLastWord(self, s):
        substring=""
        for i in range(0,len(s)):
            if s[i] != " ":
                substring=substring+s[i]
            elif i==(len(s)-1) and s[i]==" ":
                substring=substring
            elif s[i]==" " and i!=(len(s)-1) and s[i+1]!=" ":
                substring=''
            else:
                substring=substring
        return len(substring)
        
