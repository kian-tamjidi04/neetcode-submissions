class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT = {}

        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        window = {} # char : count for the current window
        have = 0 # characters that currently meet the required count
        need = len(countT) # characters we need to match
        
        # Best window indices and length of best window
        res = [-1, -1]
        resLen = float("infinity")
        l = 0

        for r in range(len(s)):
            char = s[r]

            # Add character to window
            window[char] = 1 + window.get(char, 0)

            # If (1) character in t 
            # and (2) we've reached the number of occurrences of char in t
            if char in countT and window[char] == countT[char]:
                have += 1

            # While we're in a window that contains everything from t
            while have == need:
                # Update shortest substring
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                
                # Decrement value of s[l] (ie preparing to shift l to the right)
                window[s[l]] -= 1

                # If (1) s[l] was a character of interest 
                # and (2) the value is below the desired threshold in t, update have
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1

                # Shift l right                
                l += 1 

        l, r = res

        return s[l:r+1] if resLen != float("infinity") else ""
            