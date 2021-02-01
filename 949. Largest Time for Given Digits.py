class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        ans=""
        from itertools import permutations
        seq = permutations(arr)
        s = list(seq)
        s.sort()
        s.reverse()
        for p in s:
            if p[0] ==2:
                if p[1] <4:
                    if p[2]<6:
                        return str(p[0]) + str(p[1]) + ":" + str(p[2]) + str(p[3])
            elif p[0]<2:
                if p[2]<6:
                    return str(p[0]) + str(p[1]) + ":" + str(p[2]) + str(p[3])
 
        return ans