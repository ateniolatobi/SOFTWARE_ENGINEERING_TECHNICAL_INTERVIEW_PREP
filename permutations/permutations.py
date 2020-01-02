from collections import Counter

def permutation(str1, str2):
  str1 = str1.strip()
  str2 = str2.strip()
  if len(str1) != len(str2):
    return False
  count_str1 = Counter(str1)
  count_str2 = Counter(str2)
  return count_str1 == count_str2