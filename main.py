import random

wordList = []
realWord = ''
wordLen = int(input("Word Len: "))
exists = False


def CreateWord():
    tempword = ''
    for c in range(wordLen):
        nextnum = random.randint(1, 2)
        if nextnum == 1:
            tempword += 'a'
        else:
            tempword += 'b'
    return tempword


# No Duplicates
for t in range(wordLen):
    word = CreateWord()
    while word in wordList:
        word = CreateWord()
    wordList.append(word)

# Duplicates
# for t in range(wordLen):
#     word = CreateWord()
#     wordList.append(word)

for i in range(len(wordList)):
    word = wordList[i]
    if word[i] == 'a':
        realWord += 'b'
    else:
        realWord += 'a'

if realWord in wordList:
    exists = True

print(realWord)
print(wordList)
print(exists)
