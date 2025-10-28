class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        paperCount = [0] * (n+1)

        for c in citations:
            paperCount[min(n, c)] += 1
        
        h = n
        papers = paperCount[h]

        while h > papers:
            h -= 1
            papers += paperCount[h]

        return h



        