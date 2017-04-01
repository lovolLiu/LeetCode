"""
Description:
There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:
nums1 = [1, 3]
nums2 = [2]
The median is 2.0

Example 2:
nums1 = [1, 2]
nums2 = [3, 4]
The median is (2 + 3)/2 = 2.5

Solution1:
If there is no O(log (m + n)) run time complexity requirement, it is easy to come up with a solution with the similar
consideration of mergeSort.
Merge the two sorted array into one and return the median of the sorted array, the time complexity is O(m + n)

Solution2:
A better solution would be similar to Binary Search, the median of the two sorted arrays is:
    the (length / 2 + 1)th number in the merged array if the length of the merged array is odd,
    the (length / 2)th number + the (length / 2 + 1)th number / 2 if the length of the merged array is even.
So the key to this problem is to find the kth number in the merged array.
we compare nums1[k / 2] and nums2[k / 2]:
    if nums1[k / 2] < nums2[k / 2], as the two arrays are sorted, the kth number in the merged array must be greater
than nums1[k / 2], so we can skip k / 2 elements in nums1 and find the kth number in the remainder of nums1 and nums2
    if nums1[k / 2] > nums2[k / 2], we can skip k / 2 elements in nums2 and find the kth number in nums1 and the
remainder of nums2
    if nums1[k / 2] = nums2[k / 2], we have found the kth number in the merged sort.
"""


class Solution(object):
    # solution 1 with O(m + n) time complexity
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        i = j = k = 0
        merged = []
        length = len(nums1) + len(nums2)
        for index in range(length):
            merged.append(0)
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                merged[k] = nums1[i]
                i += 1
            else:
                merged[k] = nums2[j]
                j += 1
            k += 1
        while i < len(nums1):
            merged[k] = nums1[i]
            i += 1
            k += 1
        while j < len(nums2):
            merged[k] = nums2[j]
            j += 1
            k += 1
        if length % 2 == 0:
            return (merged[length / 2 - 1] + merged[length / 2]) / 2.0
        else:
            return merged[length / 2] * 1.0

    # solution 2 with O(log (m + n)) time complexity
    def findMedianSortedArrays1(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        def findKth(a, b, k):
            lena = len(a)
            lenb = len(b)
            if lena > lenb:
                return findKth(b, a, k)
            if a == []:
                return b[k - 1]
            if k == 1:
                return min(a[0], b[0])
            parta = min(k // 2, lena)
            partb = k - parta
            if a[parta - 1] < b[partb - 1]:
                return findKth(a[parta:], b, k - parta)
            else:
                return findKth(a, b[partb:], k - partb)
        length = len(nums1) + len(nums2)
        if length % 2 == 0:
            return (findKth(nums1, nums2, length / 2) +
                    findKth(nums1, nums2, length / 2 + 1)) / 2.0
        else:
            return findKth(nums1, nums2, length / 2 + 1) * 1.0
