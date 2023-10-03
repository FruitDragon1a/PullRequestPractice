amount = 0
mostfrequentword = " "

for word in spWordsList:
    if word in wordsDict:
        wordsDict[word] += 1
    else: 
        wordsDict[word] = 1

maxValue=1
wWord = ""

for word in wordsDict:
    if wordsDict[word] > maxValue:
        maxValue = wordsDict[word]
        wWord = word

print("\n\nThe word that is seen the most: " + Wword + "\nThe number of times it occured: " + str(maxValue) + "\n")