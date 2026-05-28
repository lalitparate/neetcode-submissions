class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_out = defaultdict(list)

        for stri in strs:
            arr = [0]*26
            for s in stri:
                arr[ord(s) - ord('a')] += 1
            
            my_out[tuple(arr)].append(stri)

        return list(my_out.values())
