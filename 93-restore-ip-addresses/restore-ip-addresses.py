class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        '''
        input: str of IP
        output: arr of str, all possible valid IPs

        edge: s > 12, s is empty, no valid ip

        Plan:
        backtrack and create all valid Ips
        check for leading zeros and invalid Ips
        '''

        res = []

        if len(s) > 12:
            return res


        def backtrack(i, dot, currIP):
            #base case
            if dot == 4 and i == len(s):
                res.append(currIP[:-1])
                return
            if dot > 4 and i >= len(s):
                return

            for j in range(i, min(i+3, len(s))):
                num = s[i:j+1]
                #validate
                if int(num) < 256 and (i == j or s[i] != '0'):
                    backtrack(j + 1, dot + 1, currIP + num + '.')


        backtrack(0,0, '')
        return res