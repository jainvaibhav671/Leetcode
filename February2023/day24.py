
# https://leetcode.com/problems/minimize-deviation-in-array/

import heapq
class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        pq = []
        mini = 1e10;
        for num in nums:
            if num % 2:
                heapq.heappush(pq, -1 * num * 2)
                mini = min(num * 2, mini)
            else:
                heapq.heappush(pq, -1 * num)
                mini = min(num, mini)

        ans = 1e10
        while pq:
            top = int(-1 * heapq.heappop(pq))
            ans = min(ans, top - mini)

            if top % 2:
                break

            mini = min(mini, top / 2)
            heapq.heappush(pq, -1 * top / 2)
        
        return int(ans)
                        
