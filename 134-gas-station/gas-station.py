from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        total, start = 0, 0

        for idx, num in enumerate(gas):
            total += (num - cost[idx])

            if total < 0:
                total = 0
                start = idx + 1
        
        return start
