def editReplace(str1, str2):
  editCount = 0
  for i in range(len(str1)):
    if str1[i] != str2[i]:
      editCount += 1
  if editCount < 2:
    return True
  return False

def editInsert(str1, str2):
  ind1 = 0
  ind2 = 0
  editCount = 0
  while ind1 < len(str1) and ind2 < len(str2):
    if str1[ind1] != str2[ind2]:
      ind1 += 1
      editCount += 1
      continue
    ind1 += 1
    ind2 += 1	
  if editCount < 2:
    return True
  return False



def editType(str1, str2):
	str1len = len(str1)
	str2len = len(str2)
	if str1len == str2len:
		return editReplace(str1, str2)
	elif str1len == (str2len + 1):
		return editInsert(str1, str2)
	elif (str1len + 1) == str2len:
		return editInsert(str2, str1)
	return False

		
		
	

editType("abba", "ab")