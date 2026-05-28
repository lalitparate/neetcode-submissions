class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count = [0] * 26

        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1
        for val in count:
            if val != 0:
                return False
        return True 
        
        """
        d1 = {}
        d2 = {}
        st = set()
        for s1 in s:
            st.add(s1)
            if s1 not in d1:
                d1[s1] = 1
            d1[s1] += 1
        
        for s1 in t:
            st.add(s1)
            if s1 not in d2:
                d2[s1] = 1
            d2[s1] += 1
        
        for s1 in st:
            if s1 in d1 and s1 in d2 and d1[s1] == d2[s1]:
                continue
            else:
                return False
        return True
        """
