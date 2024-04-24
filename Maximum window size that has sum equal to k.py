# Sliding window - 3
# Given an array and sum of sub-array = k, find the maximum size of window
# all possible windows of sub-arrays that can be formed.

def largest_window_sum(array, k):
    temp = []
    for i in range(1,len(array)):
        for j in range(len(array) - i + 1):
            window_sum = sum(array[j:j+i])
            if window_sum == k:
                temp.append(len(array[j:j+i]))
    return max(temp)

arr = [1,2,1,1]
k = 2
ans = largest_window_sum(arr,k)
print(ans)
