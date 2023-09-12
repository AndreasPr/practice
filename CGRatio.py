def myGenes(numberOfLines, lines):
    lengthPerLine = len(lines[0])
    totalNumberOfCharacters = lengthPerLine * numberOfLines
    sum = 0
    for line in lines:
        for i in line:
            if i == "C" or i == "G":
                sum += 1
    
    gcRatio = (sum / totalNumberOfCharacters) * 100
    return gcRatio

if __name__ == "__main__":

    numberOfLines = int(input())

    firstInput = input()
    desired_length = len(firstInput)
    lines = []
    lines.append(firstInput)

    for i in range(numberOfLines - 1):
        record = input()
        if len(record) == desired_length:
            lines.append(record)
        else:
            print("Invalid input of characters! Please try again")
            break

    print(myGenes(numberOfLines, lines)) 