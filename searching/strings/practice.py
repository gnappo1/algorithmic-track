def lps_maker(pattern):
    n = len(pattern)
    lps = [0] * n
    left = 0
    
    for right in range(1, n):
        while left > 0 and pattern[left] != pattern[right]:
            left = lps[left-1]
        
        if pattern[left] == pattern[right]:
            left += 1
            lps[right] = left
    
    return lps


def kmp(text, pattern):
    n, m = len(text), len(pattern)

    if not pattern:
        return list(range(n + 1))

    lps = lps_maker(pattern)

    i, j = 0, 0
    res = []

    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j+= 1
            if j == m:
                res.append(i-j)
                j = lps[j-1]
        else:
            if j > 0:
                j = lps[j-1]
            else:
                i += 1

    return res


# print(kmp("ababcabcabababd", "ababd"))


def z_maker(s:str) -> list:
    n = len(s)
    Z = [0] * n

    left = right = 0
    for i in range(1, n):
        if i <= right:
            Z[i] = min(right - i + 1, Z[i - left])
        while i + Z[i] < n and s[Z[i]] == s[i+Z[i]]:
            Z[i] += 1
        if i + Z[i] - 1 > right:
            left, right = i, i + Z[i] - 1

    return Z


def z(text:str, pattern:str) -> list:
    n, m = len(text), len(pattern)

    if not m:
        return list(range(n+1))

    combo = pattern + "#" + text
    p = len(combo)
    Z = z_maker(combo)

    res = []

    for i in range(m+1, p):
        if Z[i] == m:
            res.append(i - m - 1)

    return res

# print(z("thisisatextabaceababaca", "ababaca"))


def lps_maker(p:str) -> list:
    n = len(p)
    lps = [0] * n

    left = 0

    for right in range(1, n):
        while left > 0 and p[left] != p[right]:
            left = lps[left-1]
        if p[left] == p[right]:
            left += 1
            lps[right] = left
    return lps


print(z_maker("abcabcabc"))
