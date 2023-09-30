file = open("long.txt","r")
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

print(frequency)
