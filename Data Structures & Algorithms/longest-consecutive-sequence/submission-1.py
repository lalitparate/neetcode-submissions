class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hshSet = set()
        if not nums:
            return 0
        for num in nums:
            hshSet.add(num)
        print(hshSet)
        maxSeq = 1
        for num in nums:
            if num not in hshSet:
                continue
            if num-1 not in hshSet:
                tmp = 1
                while(True):
                    if num+1 in hshSet:
                        tmp +=1
                        hshSet.remove(num+1)
                        num = num+1
                    else:
                        break
                maxSeq = max(tmp, maxSeq)
        return maxSeq