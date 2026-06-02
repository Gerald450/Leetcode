class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        '''
        input: s: str, k:int
        ouput: int, length of longest substring with at least k chars

        edge: no substring, k > length of s, ascii

        plan:
        use recursion
        use counter to get global freqs
        partition where global freq of letter is less than k
        continue to partiton till we get a valid substring and get lengths of partioned substrings
        return maxlength
        '''

        if k > len(s):
            return 0

        freq_hashmap = Counter(s)


        for key, value in freq_hashmap.items():
            if value < k:
                return max(
                    self.longestSubstring(partition, k) for partition in s.split(key)
                )

        return len(s)


        '''
        s=abadbbcbbad, k=2
        freq_hashmap= {
            a:3,
            b:5,
            c:1,
            d:2
        }
        loop: a:d{
            c:1 < k
            longestSubstring(abadbb, k){
                freq_hashmap = {
                    a:2,
                    b:3,
                    d:1
                }
                loop: a:d{
                    d:1 < k

                }
            }
        }
        ....
        s= bb
        max = 2
        return 2

        time: O(n^2)
        space: O(n), recursion stack and freq_hashmap
        '''