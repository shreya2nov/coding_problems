class Solution(object):
    def lengthOfLongestSubstring(self, s):
        seen={}
        max_len=0
        start=0
        for end in range(len(s)):
            if s[end] in seen:
                start = max(start,seen[s[end]]+1)
            seen[s[end]]=end
            max_len=max(max_len,end-start+1)
        return max_len
