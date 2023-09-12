def fillFunc(originalArray, originalIndexV, integeriIndex, xNewValue):
        
    if integeriIndex < 0 or integeriIndex >= len(originalArray) or originalArray[integeriIndex] == xNewValue:
        return
                    
    if originalArray[integeriIndex] != originalIndexV:
        return
    
    originalArray[integeriIndex] = xNewValue

    fillFunc(originalArray, originalIndexV, integeriIndex-1, xNewValue)
    fillFunc(originalArray, originalIndexV, integeriIndex+1, xNewValue)


if __name__ == "__main__":
    nIntegers, iIndex, xNewValue = input().split() 

    initialArray = input().split() 
    integeriIndex = int(iIndex)
    originalArray = [int(numericString) for numericString in initialArray]

    fillFunc(originalArray, originalArray[integeriIndex], integeriIndex, xNewValue)
    print(originalArray)