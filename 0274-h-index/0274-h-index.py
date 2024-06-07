from collections import Counter

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        counter = Counter(citations)
        
        # Value of h index can not exceed number of papers and max citation number.
        n = min(len(citations), max(citations))
        h = 0
        print(counter)
        # Iterate all the possible h
        for i in range(n + 1):
            # Sum number of papers whose citation number is greater than i.
            count = sum([counts for citationNum, counts in counter.items() if citationNum >= i])   
            # If count is greater or equal to i, it can be h-index. 
            if i <= count:
                h = i
            # If count is smaller than i, any i that is greater than current i cannot be h-index.
            else:
                break
                        
        return h



