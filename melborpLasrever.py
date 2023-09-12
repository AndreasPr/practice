def reverseFunc(stringInput):
    if len(stringInput) == 0:
        return stringInput
    else:
        reversedString = reverseFunc(stringInput[1:]) + stringInput[0]
        return reversedString
    
if __name__ == "__main__":

    stringInput = input()
    print(reverseFunc(stringInput))
