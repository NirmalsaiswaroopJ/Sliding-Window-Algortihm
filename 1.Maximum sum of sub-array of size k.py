# Sliding window - 1
# Given an array and size of sub-array = k, find the maximum sum out of
# all sum of sub-arrays that can be formed.

def max_subarray_sum(array, k):
    if len(array) < k:
        return 0
    window_sum = sum(array[:k])
    temp = []
    temp.append(window_sum)
    for i in range(k,len(array)):
        window_sum += array[i] - array[i-k]
        temp.append(window_sum)
    return max(temp)

array = [1,2,3,4,1,2,3,9,1,2,6,8,0]
k = 3
ans = max_subarray_sum(array,k)
print(ans)
