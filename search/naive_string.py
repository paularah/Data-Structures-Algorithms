def naiveSearch(string, pattern):
    strIdx = 0
    foundPatterns = 0 
    patternIdx = 0 

    while strIdx < len(string):
        patternIdx = 0
        while pattern[patternIdx] == string[strIdx]:
            if patternIdx == len(pattern) - 1:
                foundPatterns += 1
                patternIdx = 0 
            patternIdx += 1
            strIdx += 1
        strIdx += 1
    return foundPatterns
                    # L                      R
print(naiveSearch('comgcomgdomvrrfomgomg', 'omg'))

        

