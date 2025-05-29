
def happyCalculations(givenNumInt):
    givenNumInt = str(givenNumInt)
    currentSum = 0
    for digit in givenNumInt:
        digit = int(digit)
        currentSum += (digit ** 2)
    return currentSum


def happyNumbers(originalNumStr):
    usedNumsList = []
    tempNum = int(originalNumStr)
    while tempNum != 1 and tempNum not in usedNumsList:
        usedNumsList.append(tempNum)
        tempNum = happyCalculations(str(tempNum))
    if tempNum == 1:
        return "Happy"
    elif tempNum in usedNumsList:
        return "Not happy"
    else:
        return "there's an error lol"
    



print("Hello world!!!")
    
print(happyNumbers("13"))

print("hi")

