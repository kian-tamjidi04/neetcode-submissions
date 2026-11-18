class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            length = len(s)
            res += str(length) + "#" + s
        print(res)
        return res


    def decode(self, s: str) -> List[str]:
        res = []

        i = 0

        while i < len(s):
            l = ""
            while s[i].isdigit():
                l += s[i]
                i += 1

            length = int(l)
            i += 1 # Ignore hash
            word = ""

            for j in range(i, i + length):
                word += s[j]

            res.append(word)
            i += length

        return res
