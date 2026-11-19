class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Get frequency of each number (nums : freq)
        # Group values by frequencies (freq : [nums])
        # Output list built from this map, descending in freq, while k > 0

        numFreqMap = {}

        for n in nums:
            numFreqMap[n] = 1 + numFreqMap.get(n, 0)

        freqNumsMap = [[] for i in range(len(nums) + 1)]

        for num, freq in numFreqMap.items():
            freqNumsMap[freq].append(num)

        res = []

        for i in range(len(freqNumsMap) - 1, -1, -1):
            for v in freqNumsMap[i]:
                res.append(v)
                k -= 1
                if k == 0:
                    return res
