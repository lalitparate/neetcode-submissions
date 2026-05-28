class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strsNtup = []
        final = []
        if len(strs) == 1:
            return [strs]
        for sstr in strs:
            strsNtup.append((sstr, "".join(sorted(sstr))))
        
        strsN = sorted(strsNtup, key=lambda x: x[1])
        print(strsN)
        ln = len(strsN)
        i = 0
        while i <= ln-1:
            temp = [strsN[i][0]]
            print(temp, i)
            while i <= ln-2 and (strsN[i][1] == strsN[i+1][1]):
                print("in")
                temp.append(strsN[i+1][0])
                i+= 1
            final.append(temp)
            i+= 1
        return final

