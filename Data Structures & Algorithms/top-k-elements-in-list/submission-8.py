class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numFreqMap = {}

        for n in nums:
            numFreqMap[n] = 1 + numFreqMap.get(n, 0)

        freqList = [[] for i in range(len(nums) + 1)]

        for n, v in numFreqMap.items():
            # ith position in the list contains list of values with i occurrences
            freqList[v].append(n)

        res = []

        for i in range(len(freqList) - 1, -1, -1):
            for v in freqList[i]:
                res.append(v)
                k -= 1
                if k == 0:
                    return res

