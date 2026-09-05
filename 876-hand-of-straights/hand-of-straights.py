class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        '''
        input: hand[int], size
        output: bool

        edge: size>hand, size=1

        plan:
        len(hand) % size should be 0, if not return false immediately
        get the freqs of cards
        sort hand
        make groups from smallest  num available and update counter freqs
        '''
        if len(hand) % groupSize:
            return False

        freqs = Counter(hand)

        hand.sort()

        for i in range(len(hand)):
            #card -> card + groupSize - 1
            card = hand[i]
            if freqs[card] == 0:
                continue

            for i in range(card, card + groupSize):
                if freqs[i] == 0:
                    return False
                freqs[i] -= 1

        return True

        '''
        [1, 2, 2, 3, 3, 4, 4, 5], 4
                              ^
        1: 0
        2: 0
        3: 0
        4: 0
        5: 0

        1 -> 1 + 4=5-1= 5
        runtime: O(nlogn)
        space: O(distinct nums) worst case O(n)
        '''
