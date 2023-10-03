file = open("short.txt","r")
text = file.read()

words = text.split(" ")
frequency = {}



for i in words:
    x = i
    x = x.lower()
    if x in frequency.keys():
        frequency[x] = frequency[x]+1
    else:
        frequency[x] = 1

z = 0
for i in frequency:
    if (frequency[i] > z):
        z = frequency[i]
        keyOfZ = i
        
        
print("The most frequent word, '"+keyOfZ+"', occurs",z,"times.")

    
