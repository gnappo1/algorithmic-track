class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return len(s) == len(goal) and goal in s + s

        # KMP
        # • Time: O(m) to build LPS + O(2n) to scan s+s, which is O(n). Total O(n + m).
        # • Space: O(m) for LPS + O(2n) for the doubled string, which is O(n + m).
        
        # n, m = len(s), len(goal)

        # if n != m:
        #     return False

        # def build_lps(word):
        #     l = len(word)
        #     lps = [0] * l

        #     left = 0
        #     for right in range(1, l):
        #         while left > 0 and word[left] != word[right]:
        #             left = lps[left - 1]

        #         if word[left] == word[right]:
        #             left += 1
        #             lps[right] = left

        #     return lps

        # lps = build_lps(goal)
        ## text = s * 2
        # i = j = 0  # i over s+s, j over goal

        # while i < 2 * n:
        ##     if text[i] == goal[j]:
        #     if s[i%n] == goal[j]:
        #         i += 1
        #         j += 1
        #         if j == m:
        #             return True
        #     else:
        #         if j > 0:
        #             j = lps[j - 1]
        #         else:
        #             i += 1

        # return False
