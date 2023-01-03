class Solution:
    value = (1, 5, 10, 50, 100, 500, 1000)
    ch = 'IVXLCDM'
    roman_values = {
        'I': (1,0),
        'V': (5,1),
        'X': (10,2),
        'L': (50,3),
        'C': (100,4),
        'D': (500,5),
        'M': (1000,6),
    }
    
    def romanToInt(self, s: str) -> int:
        pos = 0
        result = 0
        
        for c in reversed(s):
            current = self.roman_values[c]
            if current[1] >= pos:
                pos = current[1]
                result+=current[0]
            else:
                result-=current[0]
        
        return result
    
    def romanToInt_alt(self, s: str) -> int:
        pos = 0
        result = 0
        
        for c in reversed(s):
            index = self.ch.index(c)
            if index >= pos:
                pos = index
                result+=self.value[index]
            else:
                result-=self.value[index]
        
        return result


def do_test(i: int, s, r):
    c = Solution()
    resp = c.romanToInt(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, "III", 3)
    do_test(1, "LVIII", 58)
    do_test(2, "MCMXCIV", 1994)
    do_test(3, "X", 10)
    do_test(4, "XX", 20)
