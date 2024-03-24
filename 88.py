class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return nums1
        if m == 0:
            for i in range(n):
                nums1[i] = nums2[i]
            return nums1 
        j = len(nums1)-1
        i = m-1
        k = n-1
        while k >= 0 and i >= 0:
            if nums1[i] > nums2[k]:
                nums1[j] = nums1[i]
                i -= 1
            else:
                nums1[j] = nums2[k]
                k -= 1
            j -= 1

        while k >= 0:
            nums1[j] = nums2[k]
            k -= 1
            j -= 1

        return nums1

        

        