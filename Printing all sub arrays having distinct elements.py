# Sliding window - 6
# Printing all sub-arrays of an array having distinct elements.

def distinct_subarray(array):
  temp = []
  for i in range(len(array)):
    for j in range(len(array) - i + 1):
      window = array[j:i+j]
      window_set = set(window)
      w_list = list(window_set)
      if len(window) == len(w_list) and window not in temp:
        temp.append(window)
  return temp

arr = [1,2,2,1,3,4]
ans = distinct_subarray(arr)
print(ans)
