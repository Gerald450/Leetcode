from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        '''


        edge: if cost > gas: -1, empty

        gas[i] - cost[i]
        diff = [-2, -2, -2, 3, 3]

        diff = [-1, -1, 1]

        loop through getting the differnce and adding it to globalTotal
        if it goes negative, reset globalTotal and start at the next index
        return start

        '''
        if sum(cost) > sum(gas):
            return -1
        currMax = 0
        start = 0
        for i in range(len(gas)):
            currMax += gas[i] - cost[i]

            if currMax < 0:
                currMax = 0
                start = i + 1

        return start

        '''
        -2, -2, -2, -1, 10

        i = 4 -> 5

        currMax = 6
        start = 3

        '''

            
        
        
