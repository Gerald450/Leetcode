class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #time = (target - pos)/speed
        #need to merge the two 
        #[0, 3, 5, 7, 8]
        #use stack to keep track of fleets
        #[[pos, speed]]
        
        stack = []
        otp = []

        for pos, spe in zip(position, speed):
            otp.append([pos, spe])

        otp.sort(key =lambda x:x[0])

        for i in range(len(otp) - 1, -1, -1):
            pos, spe = otp[i]
            time = (target - pos) / spe

            if not stack:
                stack.append(time)
            else:
                if time > stack[-1]:
                    stack.append(time)

        return len(stack)


           

        

        


        