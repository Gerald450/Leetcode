class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        newArr = s.split(' ')
        print(newArr)

        for i in range(len(newArr) - 1, -1, -1):
            if newArr[i] != '':
                return len(newArr[i])


        