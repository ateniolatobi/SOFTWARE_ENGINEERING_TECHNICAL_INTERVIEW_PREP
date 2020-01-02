from collections import Counter

def palindromePermutation(str1):
  str1 = str1.replace(" ", "").lower()
  strCount = Counter(str1)
  oneDetected = False
  isPermutation = True
  print(strCount)
  for k,v in strCount.items():
    if (v%2) != 0:
      if v == 1:
        if not oneDetected:
          oneDetected = True
          continue
        isPermutation = False
        break
      else:
        isPermutation = False
        break
        
  return isPermutation

print(palindromePermutation("Tact Coa"))