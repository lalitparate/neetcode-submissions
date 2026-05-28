class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict

        my_dict = defaultdict(list)
        final = []
        for istr in strs:
            sistr = "".join(sorted(istr))
            my_dict[sistr].append(istr)
        for key, value in my_dict.items():
            final.append(value)
        return final        


