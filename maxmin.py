inputted_list = [100, -100, 15, -4, 96.364823, 0, 2.21]

def find_min(list):
    # This function finds the smallest number in a list by inspecting each number and checking if it is smaller than the previously smallest number.
    # If the number is smaller it is stored. The number stored at the end is the smallest number in the list.
    current_min_val = list[0] # Initialise the smallest number in the list so far.
    for i in range(len(list)):
        if list[i] < current_min_val: # Number is smaller than the previously stored number
            current_min_val = list[i]
    return current_min_val

def find_max(list):
    # This function finds the largest number in a list by inspecting each number and checking if it is larger than the previously largest number.
    # If the number is larger it is stored. The number stored at the end is the largest number in the list.
    current_max_val = list[0] # Initialise the largest number in the list so far.
    for i in range(len(list)):
        if list[i] > current_max_val: # Number is larger than the previously stored number
            current_max_val = list[i]
    return current_max_val    

min_max = [find_min(inputted_list), find_max(inputted_list)]

print (min_max)
