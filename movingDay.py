def movingDay(list_of_inputs, v_value):
    maximum = 0
    for list_element in list_of_inputs:
        volume = int(list_element[0]) * int(list_element[1]) * int(list_element[2])
        if volume > maximum:
            maximum = volume
    difference = int(maximum) - int(v_value)
    return difference

if __name__ == "__main__":
    number_of_boxes, v_value = input().split()
    list_of_inputs = []

    for _ in range(int(number_of_boxes)):
        length, width, height = input().split()
        list_of_inputs.append([length, width, height])

    print(movingDay(list_of_inputs, v_value))