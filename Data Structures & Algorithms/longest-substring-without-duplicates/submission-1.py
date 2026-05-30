class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        myHashSet = set()
        res = 0
        l = 0


        for r in range(len(s)):
            while (s[r] in myHashSet):
                myHashSet.remove(s[l])
                l += 1
            myHashSet.add(s[r])
            res = max(res, r-l+1)
        return res

