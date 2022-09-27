from collections import Counter
class Solution:
    def uniqChar(word):
        char_hash = [False]*256
        isRepeated = False
        if len(word) > 128:
            return True
        for i in range(len(word)):
            # print(char_hash[ord(word[i])])
            if char_hash[ord(word[i])] == False:
                char_hash[ord(word[i])] = True
            else:
                isRepeated = True
            break
        return isRepeated

            
