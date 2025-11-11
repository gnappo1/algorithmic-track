from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            # always partition the shortest collection
            nums1, nums2 = nums2, nums1

        # the total length will give us the midpoint for the sorted left
        n, m = len(nums1), len(nums2)
        total = n + m
        half = (total + 1) // 2  # left half included for odd

        low, high = 0, n
        while low <= high:
            # pick middle of curr window
            i = (low + high) // 2
            # we need to have half elements at all times -> i + j = half -> i + (half - i) = half
            j = half - i

            # create left and right values for boundaries
            left_1 = nums1[i - 1] if i > 0 else float("-inf")
            right_1 = nums1[i] if i < n else float("inf")
            left_2 = nums2[j - 1] if j > 0 else float("-inf")
            right_2 = nums2[j] if j < m else float("inf")

            if left_1 <= right_2 and left_2 <= right_1:
                # if both left values are smaller than both right values
                # then we know these are the four center elements
                # if total is odd: use the greatest of the left values (half included it)
                if total % 2 == 1:
                    return max(left_1, left_2)

                # otherwise if even, the average will be between the two center values -> (max(left values) + min(right values)) / 2
                return (max(left_1, left_2) + min(right_1, right_2)) / 2

            # if nums1 left value is greater than nums2 right -> move left with i
            if left_1 > right_2:
                high = i - 1
            else:
                # if left_1 < right_2 BUT left_2 > right_1, they haven't crossed yet
                low = i + 1

        # ============================
        # Time: O(m+n)
        # Space: O(1)
        # strategy: why would you form the entire merged list??
        # instead go over half of the total length -> +1 otherwise even elements will not include both elements around the center but only the lower one
        # use prev and curr to keep track of contiguous pairs -> useful when final collection is even
        # i and j help going over nums1 and nums2
        # the loop is equivalent to ruby's .times() we just want to track pairs until we reach the center, no need for that variable -> _
        # the problem seems to want results in floats
        # n, m = len(nums1), len(nums2)
        # total = n+m
        # i, j = 0, 0
        # prev = curr = 0

        # for _ in range(total // 2 + 1):
        #     prev = curr

        #     if (i < n) and (j == m or nums1[i] <= nums2[j]):
        #         curr = nums1[i]
        #         i += 1
        #     else:
        #         curr = nums2[j]
        #         j += 1

        # if total % 2 == 1:
        #     return float(curr)

        # return (curr + prev) / 2.0


        # ===================
        # if not nums1 and not nums2:
        #     return nums1

        # # not to modify the initial collection
        # merged_array = []

        # i, j = 0, 0

        # while i < len(nums1) and j < len(nums2):
        #     if nums1[i] < nums2[j]:
        #         merged_array.append(nums1[i])
        #         i += 1
        #     else:
        #         merged_array.append(nums2[j])
        #         j += 1

        # if i < len(nums1):
        #     merged_array.extend(nums1[i:])
        # if j < len(nums2):
        #     merged_array.extend(nums2[j:])


        # n = len(merged_array)
        # mid = n >> 1

        # return (merged_array[mid -1] + merged_array[mid]) / 2  if n & 1 == 0 else merged_array[mid]
