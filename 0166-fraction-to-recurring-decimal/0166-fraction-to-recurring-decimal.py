import math as mt
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator ==0:
            return '0'
        r =[]
        if (numerator<0) ^ (denominator<0):
            print('hello man')
            r.append('-')
        numerator, denominator = abs(numerator),abs(denominator)
        r.append(str(numerator//denominator))
        rem = numerator%denominator
        
        if rem ==0:
            return ''.join(r)
        r.append(".")
        rm={}
        while not rem==0:
            if rem in rm:
                i = rm[rem]
                r.insert(i,'(')
                r.append(')')
                break
            rm[rem]=len(r)
            rem = 10*rem
            r.append(str(rem//denominator))
            rem %= denominator
        return ''.join(r)