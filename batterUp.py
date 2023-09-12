def batterUp(number_of_plate_appearances, plate_appearances): 
    sum = 0
    for i in plate_appearances:
        if i == "-1":
            number_of_plate_appearances = number_of_plate_appearances - 1
            continue
        else:                
            sum = int(sum) + int(i)
    
    slugging_average = sum / number_of_plate_appearances
    return slugging_average

if __name__ == "__main__":
    number_of_plate_appearances = int(input())

    plate_appearances = input().split(" ",number_of_plate_appearances)
    print(batterUp(number_of_plate_appearances, plate_appearances))
