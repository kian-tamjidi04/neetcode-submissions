class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        print(res)
        return res


    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i

            # Keep incrementing j until delimiter found
            # Deals with case of len(s) > 9 (ie length has more than 1 number)
            while s[j] != "#":
                j += 1

            length = int(s[i:j])

            # Add the string from the starting position to end
            res.append(s[j + 1 : j + 1 + length])
            
            # Increment i
            i = j + 1 + length

        return res

        