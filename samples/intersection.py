"""
    An interview question to return the character that had the
    greatest intersection between two strings.
    i.e. "aaabbcc" and "babaacddd" would have character intersections
    of a=3 b=2 c=1 d=0 and would return 'a'
"""
def stringIntersection ( stringA, stringB ):
    charCountsA = {}
    charCountsB = {}
    
    for char in stringA:
        if charCountsA.has_key(char):
            charCountsA[char] = charCountsA[char] + 1
        else:
            charCountsA[char] = 1

    for char in stringB:
        if charCountsB.has_key(char):
            charCountsB[char] = charCountsB[char] + 1
        else:
            charCountsB[char] = 1

    # at this point have counts for both strings
    
    maxChar = ''
    maxCount = 0
    countAKeys = charCountsA.keys()    
    for key in countAKeys:
        if charCountsB.has_key(key):
            countA = charCountsA[key]
            countB = charCountsB[key]
            intersectionCount = 0
            if countA < countB:
                # go with countA
                intersectionCount = countA
            else:
                # go with countB
                intersectionCount = countB
                
            if intersectionCount > maxCount:
                maxChar = key
                maxCount = intersectionCount
                
    return maxChar
    
print stringIntersection('aabcbcbd', 'abbbccccceeeeeeeeeeeeeeee')           
print stringIntersection('abcabcabcabcabcabcabcabdbacdbacacdacabd', 'ddddddddddddddbbbbbbbbbbbccccccccaaaaaa')           
