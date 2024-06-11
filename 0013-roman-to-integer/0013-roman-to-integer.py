class Solution:
    def romanToInt(self, s: str) -> int:
        n = len(s)
        symbols = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        values = [1, 5, 10, 50, 100, 500, 1000]
        result = 0
        
        for i in range(1, n):
            print(i)
            s1 = s[i-1]
            s2 = s[i]
            if self.isInOrder(symbols, s1, s2):
                result += values[symbols.index(s1)]
            else:
                result -= values[symbols.index(s1)]
            print(result)
        
        result += values[symbols.index(s[n-1])]
        return result


    def isInOrder(self, symbols: list[str], s1: str, s2: str) -> bool:
        distance = symbols.index(s1) - symbols.index(s2)
        # If distance is -1, it is valid roman in reverse order. 
        if distance == -1:
            return False
        # If distance is greater or equal to 0, it is valid roman in forwards order.
        elif distance >= 0:
            return True
        # Otherwise, it is invalid roman. 
        else:
            print('Invalid Roman')

