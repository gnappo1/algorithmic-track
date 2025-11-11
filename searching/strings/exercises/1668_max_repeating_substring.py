class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        n, m = len(sequence), len(word)
        for k in range(n // m, 0, -1):
            if word * k in sequence:
                return k
        return 0

        # n, m = len(sequence), len(word)

        # def build_lps(text):
        #     l = len(text)
        #     lps = [0] * l

        #     left = 0

        #     for right in range(1, l):
        #         while left > 0 and text[left] != text[right]:
        #             left = lps[left - 1]

        #         if text[left] == text[right]:
        #             left += 1
        #             lps[right] = left

        #     return lps

        # output = 0
        # for i in range(1, n // m + 1):
        #     combo = word*i
        #     lps = build_lps(combo)
        #     left = right = 0

        #     prev_output = output
        #     while left < n:
        #         if sequence[left] == combo[right]:
        #             left += 1
        #             right += 1
        #             if right == m * i:
        #                 output = i
        #                 break
        #         else:
        #             if right > 0:
        #                 right = lps[right - 1]
        #             else:
        #                 left += 1

        #     if prev_output == output:
        #         break

        # return output
