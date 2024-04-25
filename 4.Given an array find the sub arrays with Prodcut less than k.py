# Sliding window - 4
# Given an array find the sub arrays with Prodcut less than k

def subarray_less_prod(array, k):
  def product(arr):
    var = 1
    for i in arr:
      var *= i
    return var
  temp = []
  for i in range(1,len(array)):
    for j in range(len(array) - i + 1):
      window_product = product(array[j:j+i])
      if window_product < k:
        temp.append(array[j:j+i])
  return temp

arr = [2,5,1,5,8,9]
k = 12
ans = subarray_less_prod(arr,k)
print(ans)
