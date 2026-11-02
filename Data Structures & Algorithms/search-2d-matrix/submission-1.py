class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Note: This solution runs in O(mlogn) time, 
        # as we are checking which row to perform bin.search on linearly
        for row in matrix:
            if target > row[-1]:
                continue
            
            l, r = 0, len(row) - 1
            while l <= r:
                mid = (l + r) // 2
                if row[mid] == target:
                    return True
                elif row[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1


        return False