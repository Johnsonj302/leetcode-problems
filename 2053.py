class Solution:
    def kthDistinct(self, arr, k):
        
        result = []
        for i in range(len(arr)):
            if arr[i] not in arr[i+1:] and arr[i] not in arr[:i]:
                result.append(arr[i])
        if k > len(result):
            return ""
        else:
            return result[k-1]
      
        