from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # O(NlogM) for time, summing inside the while loop, where M=max_pile
        # O(1) constant space
        #! YOU COULD SET A TIGHTER BOUND ON low (see below)
        
        low, high = 1, max(piles)

        if h == len(piles):
            return high

        def can_finish(bph: int):
            hours = 0
            for pile in piles:
                hours += (pile + bph -1) // bph
                if hours > h:
                    return False
            return True


        while low < high: # O(logM)
            middle = (low + high) // 2
            
            if can_finish(middle):
                high = middle
            else:
                low = middle + 1
        return low
        
        #!------ TIGHTER low BOUND --------
        #! For performance, Python’s built-in sum(piles) and max(piles) are in C and often faster than a single Python loop.
        #! One pass is fine, but two built-ins are usually faster in practice.
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # O(NlogM) for time, summing inside the while loop, where M=max_pile
        # O(1) constant space

        total = sum(piles)
        high = max(piles)
        low = max(1, (total + h - 1) // h)


        if h == len(piles):
            return high

        def can_finish(bph: int):
            hours = 0
            for pile in piles:
                hours += (pile + bph -1) // bph
                if hours > h:
                    return False
            return True


        while low < high: # O(logM)
            middle = (low + high) // 2
            
            if can_finish(middle):
                high = middle
            else:
                low = middle + 1
        return low
        