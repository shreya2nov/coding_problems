class Solution(object):
    def isValid(self, s):
        open=['(','{','[']
        close=[']','}',')']
        stack=[]
        if len(s) == 1:
            return False
        if s[0] in open:
            stack.append(s[0])
        else:
            return False
        for i in range(1,len(s)):
            if s[i] in open:
                stack.append(s[i])
            elif s[i] == ')':
                if len(stack)==0:
                    return False
                elif stack[-1]=='(' :
                    stack.pop()
                else:
                    return False
            elif s[i] == '}':
                if len(stack)==0:
                    return False
                elif stack[-1]=='{' :
                    stack.pop()
                else:
                    return False
            else:
                if len(stack)==0:
                    return False
                elif stack[-1]=='[' :
                    stack.pop()
                else:
                    return False
        if len(stack)==0:
            return True
        else:
            return False
            
                
        """
        :type s: str
        :rtype: bool
        """
        
