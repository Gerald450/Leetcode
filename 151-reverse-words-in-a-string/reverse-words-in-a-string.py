class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.split(' ')
        newArr = []

        for i in range(len(arr) - 1, -1,-1):
            if arr[i]:
                newArr.append(arr[i])

        return " ".join(newArr)
