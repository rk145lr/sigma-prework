from datetime import date

def import_date():
    # The purpose of this function is to ask the user for a date and to then return a list with 3 elements (day, month, year) for that date.
    valid_input = False
    while valid_input == False:
        # Keep running loop until user enters a date in the correct format.
        imported_date_str = input('Enter a date in the format dd-mm-yy: ')
        imported_date_list = imported_date_str.split('-') # Separate date into day, month, year
        if len(imported_date_list) == 3 and len(imported_date_list[0]) == 2 and len(imported_date_list[1]) == 2 and len(imported_date_list[2]) == 4:
            valid_input = True
        else:
            print('\nPlease enter a date in the format dd-mm-yyyy.\nFor example, the 25th December 2022 would be 25-12-2022.\n\n')
            continue # Invalid input, inform user and re-run while loop
        for i in range(len(imported_date_list)):
            imported_date_list[i] = int(imported_date_list[i]) # Convert inputted date string into integers
    return imported_date_list

imported_date = import_date()

def get_current_date():
    # The purpose of this function is to determine the current date, and then return this information as a list with 3 elements: day, month, year.
    current_date = date.today()
    current_year = current_date.year
    current_month = current_date.month
    current_day = current_date.day
    return [current_day, current_month, current_year]

current_date = get_current_date()

if (current_date[1] > imported_date[1]) or ((current_date[1] == imported_date[1]) and (current_date[0] >= import_date[0])):
    # Check if given date is earlier in the year than current date.
    year_diff = current_date[2] - imported_date[2]
else:
    # Given date is later in the year than current date, so subtract 1 from the year difference.
    year_diff = current_date[2] - imported_date[2] - 1

print(f'The difference in years between the entered date and today\'s date is: {year_diff} year(s).')