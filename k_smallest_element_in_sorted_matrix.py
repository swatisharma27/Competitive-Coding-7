
class Solution:

    ## Binary Search
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int: 
        """
        TC: O(n * log(max - min))
        AS: O(1)
        """
        m = len(matrix)
        n = len(matrix[0])

        def countLessEqual(mid):
            count = 0
            row = m-1
            col = 0
            while row >= 0 and col < n: # starting from bottom-left or we can do from top-right ()
                if matrix[row][col] <= mid:
                    count += row + 1
                    col += 1
                else:
                    row -= 1
            return count

        low = matrix[0][0] #first element
        high = matrix[m-1][n-1] # columns

        while low < high:
            mid = low + (high-low)//2
            if countLessEqual(mid) < k:
                low = mid + 1
            else:
                high = mid
        return low        


    ## Heap Solution
    # import heapq
    # def kthSmallest(self, matrix: List[List[int]], k: int) -> int: 
    #     """
    #     TC: O(m*n log k)
    #     AS: O(k)
    #     """
    #     max_heap = []

    #     m = len(matrix) #rows
    #     n = len(matrix[0]) #columns

    #     for i in range(m):
    #         for j in range(n):
    #             heapq.heappush(max_heap, -matrix[i][j])

    #             if len(max_heap) > k:
    #                 heapq.heappop(max_heap)
    #     print(max_heap)
    #     return -max_heap[0]
            

    ## Brute Force
    # def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
    #     """
    #     TC: O(n^2) + O(n^2 log n^2) + O(1) = O(n^2 log n)
    #     AS: 
    #     """

    #     result = []

    #     for mat in matrix:
    #         result.extend(mat)

    #     result.sort()
    #     print(result)

    #     return result[k-1]
        
