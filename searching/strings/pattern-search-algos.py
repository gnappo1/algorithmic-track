# STRING PATTERN SEARCH ALGOS

#! KMP
# Build LPS array: time O(m), space O(m), where m is the pattern length.
# Search phase: time O(n), where n is the text length.
# Overall: time O(n + m), extra space O(m+r), where r is the number of matches.

def build_lps(word: str) -> list[int]:
    """
    LPS[i] = length of the longest proper prefix of word[:i+1]
             that is also a suffix of word[:i+1].
    """
    n = len(word)
    lps = [0] * n
    left = 0  # length of current longest prefix-suffix

    for right in range(1, n):
        # fall back as long as mismatch persists
        while left > 0 and word[left] != word[right]:
            left = lps[left - 1]
        # try to extend the current border
        if word[right] == word[left]:
            left += 1
            lps[right] = left
        # else left==0 and mismatch -> lps[right] stays 0
    return lps


def build_lps_alt(word: str) -> list[int]:
    """Alternative formulation (same behavior), useful as a cross-check."""
    n = len(word)
    lps = [0] * n
    j = 0
    for i in range(1, n):
        while j and word[i] != word[j]:
            j = lps[j - 1]
        if word[i] == word[j]:
            j += 1
        lps[i] = j
    return lps


def kmp(text: str, word: str) -> list[int]:
    """Return all start indices where `word` occurs in `text`."""
    if not word:
        return list(range(len(text) + 1))

    lps = build_lps(word)
    res = []
    i = j = 0  # i over text, j over pattern

    while i < len(text):
        if text[i] == word[j]:
            i += 1
            j += 1
            if j == len(word):
                res.append(i - j)
                j = lps[j - 1]  # allow overlaps
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return res


def trace_lps(word: str):
    """Print a step-by-step trace building LPS for debugging."""
    n = len(word)
    lps = [0] * n
    left = 0
    print(f"Tracing LPS for: {word!r}")
    for right in range(1, n):
        print(f"i={right}, char={word[right]!r}, left(before)={left}")
        while left > 0 and word[left] != word[right]:
            print(f"  mismatch: word[left]={word[left]!r} != {word[right]!r}; left -> lps[left-1]={lps[left-1]}")
            left = lps[left - 1]
        if word[right] == word[left]:
            left += 1
            lps[right] = left
            print(f"  match: set lps[{right}]={left}")
        else:
            print(f"  no match & left==0: lps[{right}]=0")
        print(f"  state end: left={left}, lps={lps}")
    print("Final LPS:", lps)
    return lps


# assert build_lps("ababaca")       == [0,0,1,2,3,0,1]
# assert build_lps_alt("ababaca")   == [0,0,1,2,3,0,1]
# assert build_lps("aaaa")          == [0,1,2,3]
# assert build_lps("abcab")         == [0,0,0,1,2]
# assert build_lps("aabaacaabaa")   == [0,1,0,1,2,0,1,2,3,4,5]

# assert kmp("aaabcababcababc", "abc") == [2, 7, 12]
# assert kmp("aaaaa", "aa")            == [0,1,2,3]
# assert kmp("xyz", "")                == [0,1,2,3]

# print("All tests passed.")
# trace_lps("ababaca")

# =======================================

#! Z
# Time O(n) -> Each character is compared at most twice — once when extending, once reused from [L, R].
# Space	O(n) -> You store a Z array of size n.
# Pattern Matching (p + '#' + s) O(n + m) -> Build Z array for concatenated string; scanning is linear.

def z_function(s:str):
    n = len(s)
    Z = [0] * n

    L = R = 0

    for i in range(1, n):
        if i <= R:
            Z[i] = min(Z[i - L], R - i + 1)
        while i + Z[i] < n and s[Z[i]] == s[i+Z[i]]:
            Z[i] += 1
        if i + Z[i] - 1 > R:
            L, R = i, i + Z[i] - 1
    
    return Z

def find_all_z(text:str, pattern:str) -> list:
    n, m = len(text), len(pattern)

    if not m:
        return list(range(n+1))

    combo = pattern + "#" + text

    Z = z_function(combo)
    res= []

    for i in range(m+1, len(combo)):
        if Z[i] == m:
            res.append(i-m-1)

    return res

#! SUMMARY

# KMP looks backward: when you fail, it says “how much of what I already matched can I reuse?”
# Z looks forward: for every position, it says “how much of the prefix can I match from here?”

# * Conceptual differences
# ? What it stores
# (KMP)  For each index i, LPS[i] = length of the longest proper prefix of pattern[:i+1] that’s also a suffix.
# (Z) For each index i, Z[i] = length of the longest substring starting at i that matches the prefix of the entire string.
# ? Intuition
# (KMP)  "How much of the prefix can I keep when a mismatch happens?"
# (Z) "How much of the prefix matches starting from here?"
# ? Primary use
# (KMP)  Fast pattern matching with fallback logic (e.g., strStr).
# (Z) Fast prefix matching at all positions (e.g., pattern concatenation tricks).
# ? Orientation
# (KMP)  Works within the pattern to precompute failure jumps.
# (Z)Works across the whole string to precompute prefix matches.
# ? Algorithm type
# (KMP)  Failure-function-based automaton.
# (Z) Sliding window + reuse previous matches.

# ? You can actually derive one from the other:
# Z[i] tells you where the prefix repeats later.
# LPS[i] tells you the longest border (prefix = suffix) up to i.

#! Rabin-Karp
# Compute a hash of the pattern.
# Compute a rolling hash for every substring of the text of the same length.
# Compare hashes first — only if they match, confirm with direct comparison.
# If the hash function is designed well (using modular arithmetic), this reduces the average complexity to O(n + m).

# Time: Average O(n + m), worst O(n * m) when the character by character check is done way more often that necessary due to collisions (same hash different substring when improper base is chosen or low mod).
# Space: O(1) for the hash calculation, but O(n) in the worst case due to the results list

# For most interview cases, using base 256 is a solid default because it maps well to ASCII characters.
# However, there are a few situations where you might choose a different base:
    # Smaller Alphabet: If you know your input is limited to lowercase letters, you might choose a smaller base, like 26. This can reduce hash values and possibly lower the chance of collisions in that context.
    # Prime Base: Some choose a prime base (e.g., 31, 101, or 257) because it can reduce patterns where certain sequences might produce the same hash value more often. This is common in theoretical applications or competitive programming.
    # Hashing Unicode: If you’re dealing with Unicode, you might use a larger base or adapt the hashing to handle UTF-8 encoding.
    
def rabin_karp(text: str, pattern: str) -> list:
    n , m = len(text), len(pattern)
    
    if not m or n < m:
        return []
    
    base = 256 # 31, 101
    mod = 10**9 + 7
    power = pow(base, m-1, mod)
    
    hp = 0
    hs = 0
    
    for i in range(m):
        hp = (hp * base + ord(pattern[i])) % mod
        hs = (hs * base + ord(text[i])) % mod
    
    res = []
    
    for i in range(n-m+1):
        if hp == hs:
            if text[i:i+m] == pattern:
                res.append(i)
        
        # can we extend?
        if i < n - m:
            hs = (hs - ord(text[i]) * power) % mod
            hs = (hs * base + ord(text[i+m])) % mod
            hs = (hs + mod) % mod
    
    return res

print(rabin_karp("aaabcababcababc", "abc"))


#! MORE

# 🧩 Optional or Advanced String Searching


#! 1. Finite Automaton / DFA Search
    # Essentially a deterministic state machine built from the pattern.
    # Preprocesses the pattern in O(m * Σ) time (Σ = alphabet size).
    # Search is linear O(n).
    # It’s how some low-level libraries implement str.find.
    # ✅ When to learn: only if you’re interested in compiler design or automata theory.

#! 2. Boyer–Moore (and variants like Horspool, Sunday)
    # Skips ahead using mismatched characters and suffix heuristics.
    # Best-case O(n/m), worst-case O(n + m).
    # Real-world fastest for plain text search (used in grep, strstr implementations).
    # ✅ When to learn: for completeness or systems-level optimization questions.
#? ⚙️ Variants:
    # Boyer–Moore–Horspool (simplified version)
    # Sunday (rightmost-character jump)

#! 3. Aho–Corasick (multi-pattern search)
    # Builds a trie of multiple patterns with failure links (like multi-KMP).
    # Time: O(n + total pattern length).
    # Space: O(sum of all pattern lengths).
    # ✅ When to learn: if you want to search many keywords at once (e.g. dictionary filtering, plagiarism detection).

#! 4. Suffix-based structures
    # Suffix Array / Suffix Tree — heavy-duty text indexing.
    # Used in bioinformatics, compression (LZ77, BWT), and substring problems.
    # Enables O(m log n) or even O(m) substring queries after O(n log n) preprocessing.
    # ✅ When to learn: in advanced courses or if you do competitive programming.