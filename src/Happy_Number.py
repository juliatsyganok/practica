class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        while n != 1:
            if n in s:
                return False
            s.add(n)
            summ = 0
            while n > 0:
                d = n % 10 
                summ += d * d
                n = n // 10
            n = summ 
        
        return True