class Solution(object):
    def removeDuplicates(self, s):
        ans=""
        for i in range(len(s)):
            if ans=="" or ans[-1] != s[i]:
                ans+=s[i]
            elif ans[-1] == s[i]:
                ans=ans[:-1]        
        return ans
                    
        """
        :type s: str
        :rtype: str
        """
        