if __name__ == "__main__":

    firstname, lastname = input().split()
    lengthLastname = len(lastname)

    if lengthLastname == 5:
        newLastname = lastname * 4
    else:
        newLastname = lastname * lengthLastname
    
    print(firstname, newLastname)