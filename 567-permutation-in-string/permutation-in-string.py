class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
        input: s1 and s2 str
        output: boolean

        edge: if s1 is empty, lower or uppercase, s1>s2

        plan:
        use hashmap and sliding window
        create hashmap for s1, and a hashmap for a window in s2
        window size is same len as s1
        move window if two hashmaps not equal
        stop if left pointer reaches end of s2
        '''

        if len(s1) > len(s2):
            return False

        from collections import Counter
        hashmap1 = Counter(s1)
        hashmap2 = Counter()

        l = 0

        for r in range(len(s2)):
            letter = s2[r]
            hashmap2[letter] += 1
            window = r - l + 1
            if window >= len(s1):
                if hashmap1 == hashmap2:
                    return True
                else:
                    hashmap2[s2[l]] -= 1
                    l += 1
                

        return False

        '''
        hashmap1 = {a: 1, b: 1}
        hashmap2 = {}
        l = 0
        r: 0 -> 8
        r = 1
        letter = i
        hashmap2 = {e: 1, i: 1}
        window = 2
        hashmap2 = {i:1}
        l = 1
        r = 2
        hashmap2 = {i:1, d: 1}
        ...
        hashmap2= {b: 1, a: 1}


        '''
    




        