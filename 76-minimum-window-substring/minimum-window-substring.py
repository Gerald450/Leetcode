from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""



        l = 0
        res, window =[-1, -1], float('inf')
        tDic = Counter(t)
        sDic = Counter()
        have, need = 0, len(tDic)



        for r in range(len(s)):
            c = s[r]
            sDic[c] += 1

            if c in tDic and sDic[c] == tDic[c]:
                have += 1

            while have == need:
                if (r - l) < window:
                    res = [l, r]
                    window = r - l
                a = s[l]
                sDic[a] -= 1
                if a in tDic and sDic[a] < tDic[a]:
                    have -= 1
                l += 1
        l, r = res
        return s[l:r + 1] if window != float('inf') else ""
            


            
                
                    



        