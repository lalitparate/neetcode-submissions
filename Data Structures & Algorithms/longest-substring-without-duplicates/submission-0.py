class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        myHashSet = set()
        res = 0
        i = 0

        for i in range(len(s)):
            myHashSet = set()
            for j in range(i, len(s)):
                if s[j] in myHashSet:
                    break
                myHashSet.add(s[j])
            res = max(res, len(myHashSet))
        return res