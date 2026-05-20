class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        '''
        input: list of str
        output: top k freq words in lex order

        edge: same freq, uppe/ lower case, k>len(words), empty str in words, other
        chars

        plan:
        bucket sort, an list of heaps
        get freqs using a Counter
        pop until empty and then move to next bucket
        '''

        hashmap = Counter(words)
        
        bucket = [[] for i in range(len(words) + 1)]

        for key, value in hashmap.items():
            heapq.heappush(bucket[value], key)
        
        output = []
        for i in range(len(words), -1, -1):
            while bucket[i]:
                output.append(heapq.heappop(bucket[i]))
                if len(output) == k:
                    return output
        
        return output
        


