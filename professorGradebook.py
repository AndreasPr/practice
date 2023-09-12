import math
from collections import defaultdict
def gradeBook(dictionaryForStudents, initialStudent, initialIndex, numberOfStudents, numberOfAssignments, resultDictionary):
    sumOfGradesOfStudent = 0
   
    if initialIndex < 0 or initialIndex >= len(dictionaryForStudents):
        return 

    currentStudent = initialStudent[0]
    listOfGrades = [int(numericString) for numericString in dictionaryForStudents[initialIndex][1:numberOfAssignments + 1]]
    listOfGrades.sort()
    
    sumOfGradesOfStudent = sum(listOfGrades) - listOfGrades[0]
    studentExamGrade = dictionaryForStudents[initialIndex][-1]
    studentSTotal = int(sumOfGradesOfStudent) + int(studentExamGrade)

    resultDictionary[initialIndex].append([currentStudent, studentSTotal])

    if initialIndex >= len(dictionaryForStudents) - 1:
        return 
    else:
        gradeBook(dictionaryForStudents, dictionaryForStudents[initialIndex + 1], initialIndex+1, numberOfStudents, numberOfAssignments, resultDictionary)
         
    return resultDictionary

def calculateMaxTotal(dictionaryOfStudentAndTotal, maxTotal):
    for i in range(len(dictionaryOfStudentAndTotal)):
        if dictionaryOfStudentAndTotal[i][0][1] > maxTotal:
            maxTotal = dictionaryOfStudentAndTotal[i][0][1] 
    return maxTotal

def calculateSAdjusted(maxTotalGrade, studentSTotal):

    sAdjusted = (studentSTotal / maxTotalGrade) * 100
    roundedsAdjusted = math.ceil(sAdjusted)
    return roundedsAdjusted
        

if __name__ == "__main__":
    numberOfStudents, numberOfAssignments = input().split()
    numberOfStudentsInteger = int(numberOfStudents)
    numberOfAssignmentsInteger = int(numberOfAssignments)
    dictionaryForStudents = {}
    resultDictionary = defaultdict(list)
    maxTotal = 0
    
    for i in range(numberOfStudentsInteger):
        studentPerformance = list(input().split())
        dictionaryForStudents[i] = studentPerformance
    
    dictionaryOfStudentAndTotal = gradeBook(dictionaryForStudents, dictionaryForStudents[0], 0, numberOfStudentsInteger, numberOfAssignmentsInteger, resultDictionary)
    
    maxTotalGrade = calculateMaxTotal(dictionaryOfStudentAndTotal, maxTotal)

    listOfAdjustedGrades = []
    for i in range(len(dictionaryOfStudentAndTotal)):
        sAdjusted = calculateSAdjusted(maxTotalGrade, dictionaryOfStudentAndTotal[i][0][1])
        listOfAdjustedGrades.append(sAdjusted)

    for index, value in enumerate(listOfAdjustedGrades):
        dictionaryOfStudentAndTotal[index][0].append(value)
    
    for i in dictionaryOfStudentAndTotal:
        gradeNumber = dictionaryOfStudentAndTotal[i][0][2]
        if gradeNumber in range(90, 101):
            dictionaryOfStudentAndTotal[i][0].append('A')
        if gradeNumber in range(80, 90):
            dictionaryOfStudentAndTotal[i][0].append('B')
        if gradeNumber in range(70, 80):
            dictionaryOfStudentAndTotal[i][0].append('C')
        if gradeNumber in range(60, 70):
            dictionaryOfStudentAndTotal[i][0].append('D')
        if gradeNumber in range(0, 60):
            dictionaryOfStudentAndTotal[i][0].append('F')
    
    for value in dictionaryOfStudentAndTotal.values():
        print(*value[0])