
def happyCalculations(givenNumStr):
    currentSum = 0
    for digit in givenNumStr:
        digit = int(digit)
        currentSum += (digit ** 2)


def happyNumbers(originalNumStr):
    tempNum = None
    while (tempNum != 1) and (tempNum != originalNumStr): #repeat until (tempNum == 1) or (tempNum == originalMum)
        tempNum = happyCalculations(originalNumStr)
    if tempNum == 1:
        return ("Happy")
    elif tempNum == originalNumStr:
        return ("Not happy")

print("Hello world!!!")
    
print(happyNumbers("13"))