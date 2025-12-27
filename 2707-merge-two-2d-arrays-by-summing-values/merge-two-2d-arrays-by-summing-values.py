class Solution:
    def mergeArrays(self, nums1, nums2):
        result = []
        used = [False] * len(nums2)

        for id1, val1 in nums1:
            found = False
            for j, (id2, val2) in enumerate(nums2):
                if id1 == id2:
                    result.append([id1, val1 + val2])
                    used[j] = True
                    found = True
                    break
            if not found:
                result.append([id1, val1])

        for i in range(len(nums2)):
            if not used[i]:
                result.append(nums2[i])

        return sorted(result)
