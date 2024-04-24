# Sliding window - 2
# Given an array and size of sub-array = k, find the maximum product out of
# all possible products of sub-arrays that can be formed.

def max_subarray_product(array,k):
    def product(arr):
        temp = 1
        for i in arr:
            temp *= i
        return temp

    if len(array)<k:
        return 0

    window_product = product(array[:k])
    temp1 = []
    temp1.append(window_product)
    for i in range(k,len(array)):
        window_product = (window_product * array[i])/(array[i-k])
        temp1.append(window_product)
    return max(temp1)

array = [1,2,3,4]
k = 2
ans = max_subarray_product(array,k)
print(ans)
