# Sliding window - 7
# Given an array and integer k, find a contiguous subarray whole length is equal to k 
# and has the maximum average value

def subarray_max_avg(array, k):
    temp = []
    window_avg = sum(array[:k])/k
    temp.append(window_avg)
    for i in range(k,len(array)):
        window_avg = (window_avg * k + array[i] - array[i-k])/k
        temp.append(window_avg)
    return max(temp)
        
arr = [1,12,-5,-6,50,3]
k = 4
ans = subarray_max_avg(arr,k)
print(ans)
