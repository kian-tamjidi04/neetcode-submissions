class Solution:
    def isHappy(self, n: int) -> bool:
        myMap = {}
        res = 0

        while n not in myMap:
            myMap[n] = 1
            total = 0
            while n:
                total += (n % 10) ** 2
                n = n // 10
            
            n = total
            if n == 1:
                return True
        
        return False