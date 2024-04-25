# Sliding window - 5
# Finding all anagrams in a string

def all_anagrams_str(string1, string2):
  index = []
  new_str = sorted(string2)
  n = len(new_str)
  for i in range(len(string1)-n):
    window = string1[i:i+n]
    if sorted(window) == new_str:
      index.append(i)
  return index

string1 = "cbaebabacd"
string2 = "abc"
ans = all_anagrams_str(string1, string2)
print(ans)
