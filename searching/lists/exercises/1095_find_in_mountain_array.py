# helper: cached accessor
def make_get(mountainArr):
    cache = {}
    def G(i):
        if i not in cache:
            cache[i] = mountainArr.get(i)
        return cache[i]
    return G

def find_peak(n, G):
    lo, hi = 0, n - 1
    while lo < hi:
        mid = (lo + hi) // 2
        midv = G(mid)
        nxtv = G(mid + 1)  # safe since lo < hi ⇒ mid < hi
        if midv < nxtv:
            lo = mid + 1
        else:
            hi = mid
    return lo

def binary_search(n, G, target, lo, hi, desc=False):
    while lo <= hi:
        mid = (lo + hi) // 2
        v = G(mid)
        if v == target:
            return mid
        if not desc:
            if v < target:
                lo = mid + 1
            else:
                hi = mid - 1
        else:
            if v < target:
                hi = mid - 1   # left side has larger values
            else:
                lo = mid + 1
    return -1

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()
        G = make_get(mountainArr)

        peak = find_peak(n, G)
        pv = G(peak)
        if pv == target:
            return peak

        idx = binary_search(n, G, target, 0, peak - 1, desc=False)
        if idx != -1:
            return idx

        return binary_search(n, G, target, peak + 1, n - 1, desc=True)
