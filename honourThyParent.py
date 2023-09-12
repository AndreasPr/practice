def honourThy(name_list):
    if name_list[0][-1] == 'e':
        result = name_list[0] + "x" + name_list[1]
        return result
    if name_list[0][-1] == 'a' or name_list[0][-1] == 'i' or name_list[0][-1] == 'o' or name_list[0][-1] == 'u':
        result = name_list[0][:-1] + "ex" + name_list[1]
        return result
    if name_list[0][-1] == 'ex':
        result = name_list[0] + name_list[1]
        return result
    
    return name_list[0] + name_list[1]

if __name__ == "__main__":
    input_names = input("Enter the names separated by space: ")
    name_list = input_names.lower().split()
    if (len(name_list[0]) < 2 or len(name_list[0]) > 10) and (len(name_list[1]) < 2 or len(name_list[1]) > 1):
        print ("Error! Only at least 2 characters long and at most 10 characters long are permitted")
        
    print(name_list)
    print(honourThy(name_list))
