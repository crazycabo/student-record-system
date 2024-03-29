import sys
import csv
import math

student_records = []
invalid_student_records = []


def handle_file_input():
    valid_file_exists = False

    while not valid_file_exists:
        try:
            print('Enter the name of a file relative to this program\'s path.')
            file_name = input('File name (or type \'exit\' to quit): ')

            if file_name.lower() == 'exit':
                # Exit program by user request
                sys.exit(0)

            with open(file_name, 'r') as file:
                file_reader = csv.reader(file, delimiter=',')
                data = list(file_reader)

                # Check if file is empty
                if len(data) == 0:
                    raise Exception('File is empty!')

                for row in data:
                    skip_to_next_iteration = False

                    # Validate non-empty records first
                    for value in row:
                        if value == '':
                            invalid_student_records.append(row)
                            skip_to_next_iteration = True
                            break

                    # Validate student grade is within normal bounds
                    if float(row[3]) < 0 or float(row[3]) > 100:
                        invalid_student_records.append(row)
                        skip_to_next_iteration = True

                    # Validate student program is either MSIT or MSCM
                    if row[4] != 'MSIT' and row[4] != 'MSCM':
                        invalid_student_records.append(row)
                        skip_to_next_iteration = True

                    if skip_to_next_iteration:
                        continue

                    # If record is valid, add to student records list
                    student_records.append(row)

            print(f'\nImported {len(student_records) + len(invalid_student_records)} '
                  f'student records and {len(invalid_student_records)} are invalid.\n')

            valid_file_exists = True

        except FileNotFoundError:
            print(f'\nUnable to find or open file. Please try again or enter \'exit\' to stop program.\n')

        except Exception as ex:
            print(f'\nAn error occurred while processing file: {ex}')
            print(f'Please try again or enter \'exit\' to stop program.\n')


def display_user_options():
    print('\nChoose one of the following options')
    print('----------------------------------------------')
    print('1. Display average grade for all students')
    print('2. Display average grade for each program')
    print('3. Display highest grade record')
    print('4. Display lowest grade record')
    print('5. Display all students in MSIT program')
    print('6. Display all students in MSCM program')
    print('7. Display all students in sorted order by student ID')
    print('8. Display invalid records')
    print('9. Create new file containing invalid records\n')


def handle_option_input():
    valid_option_input = False
    user_input = None
    error_message = 'Invalid option entered. Please try again.\n'

    # Loop input request until valid input is received
    while not valid_option_input:
        try:
            user_input = input('Input option number (type \'menu\' to display options or \'exit\' to quit): ')

            if user_input.lower() not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'menu', 'exit']:
                print(error_message)
                continue

            else:
                valid_option_input = True

        except ValueError:
            print(error_message)

    if user_input == '1':
        display_average_grade_all_students()

    elif user_input == '2':
        display_average_grade_each_program()

    elif user_input == '3':
        display_highest_grade_record()

    elif user_input == '4':
        display_lowest_grade_record()

    elif user_input == '5':
        display_students_in_msit_program()

    elif user_input == '6':
        display_students_in_mscm_program()

    elif user_input == '7':
        display_all_students_sorted_by_student_id()

    elif user_input == '8':
        display_invalid_records()

    elif user_input == '9':
        create_invalid_records_file()

    elif user_input.lower() == 'menu':
        display_user_options()

    elif user_input.lower() == 'exit':
        print('\nExiting program...')
        sys.exit(0)

    else:
        print('\nInvalid option selected. Please try again.\n')


def display_average_grade_all_students():
    sum_of_all_grades = 0
    student_count = 0

    # Round each input grade up, add to sum, and increment student count
    for student in student_records:
        sum_of_all_grades += math.ceil(float(student[3]))
        student_count += 1

    if len(student_records) == 0:
        print('\nNo valid student records exist to calculate average grade.\n')
    else:
        print(f'\nAverage grade of all students: {sum_of_all_grades / student_count:.1f}\n')


def display_average_grade_each_program():
    sum_of_all_grades_msit = 0
    sum_of_all_grades_mscm = 0
    student_count_msit = 0
    student_count_mscm = 0

    # Round each input grade up, add to sum, and increment student count for each program
    for student in student_records:
        if student[4] == 'MSIT':
            sum_of_all_grades_msit += math.ceil(float(student[3]))
            student_count_msit += 1

        elif student[4] == 'MSCM':
            sum_of_all_grades_mscm += math.ceil(float(student[3]))
            student_count_mscm += 1

    if len(student_records) == 0:
        print('\nNo valid student records exist to calculate average grade in each program.\n')
    else:
        print('\nAverage grade of all students in each program')
        print(f'MSIT: {sum_of_all_grades_msit / student_count_msit:.1f}')
        print(f'MSCM: {sum_of_all_grades_mscm / student_count_mscm:.1f}\n')


def display_highest_grade_record():
    highest_grade = None

    # Loop through all records and compare grade to current highest grade
    for student in student_records:
        if highest_grade is None or float(student[3]) > float(highest_grade[3]):
            highest_grade = [student[0], f'{student[2]}, {student[1]}', student[4], student[3]]

    if len(student_records) == 0:
        print('\nNo valid student records exist to calculate highest grade.\n')
    else:
        print('\nHighest student grade\n')
        draw_table([highest_grade], ['Student ID', 'Last, First Name', 'Program', 'Grade'])


def display_lowest_grade_record():
    lowest_grade = None

    # Loop through all records and compare grade to current lowest grade
    for student in student_records:
        if lowest_grade is None or float(student[3]) < float(lowest_grade[3]):
            lowest_grade = [student[0], f'{student[2]}, {student[1]}', student[4], student[3]]

    if len(student_records) == 0:
        print('\nNo valid student records exist to calculate lowest grade.\n')
    else:
        print(f'\nLowest student grade\n')
        draw_table([lowest_grade], ['Student ID', 'Last, First Name', 'Program', 'Grade'])


def display_students_in_msit_program():
    formatted_records = []

    # Loop through all records and add to formatted records list if program is MSIT
    for student in student_records:
        if student[4] == 'MSIT':
            formatted_records.append([student[0], f'{student[2]}, {student[1]}', student[3]])

    formatted_records.sort(key=lambda x: x[1])  # sort records by last name for easier reading

    if len(student_records) == 0:
        print('\nNo valid student records exist to display students in MSIT program.\n')
    else:
        print('\nStudents in MSIT program:\n')
        draw_table(formatted_records, ['Student ID', 'Last, First Name', 'Grade'])


def display_students_in_mscm_program():
    formatted_records = []

    # Loop through all records and add to formatted records list if program is MSCM
    for student in student_records:
        if student[4] == 'MSCM':
            formatted_records.append([student[0], f'{student[2]}, {student[1]}', student[3]])

    formatted_records.sort(key=lambda x: x[1])  # sort records by last name for easier reading

    if len(student_records) == 0:
        print('\nNo valid student records exist to display students in MSCM program.\n')
    else:
        print('\nStudents in MSCM program:\n')
        draw_table(formatted_records, ['Student ID', 'Last, First Name', 'Grade'])


def display_all_students_sorted_by_student_id():
    sorted_records = sorted(student_records, key=lambda x: x[0])  # Sort where x[0] is student ID
    formatted_records = []

    for record in sorted_records:
        formatted_records.append([record[0], f'{record[2]}, {record[1]}', record[4], record[3]])

    if len(student_records) == 0:
        print('\nNo valid student records exist to display all students sorted by student ID.\n')
    else:
        print('\nAll students sorted by student ID:\n')
        draw_table(formatted_records, ['Student ID', 'Last, First Name', 'Program', 'Grade'])


def draw_table(data, labels):
    data.insert(0, labels)  # Insert labels as first row of data for correct column spacing

    # calculate max width for each column by finding longest string in each column
    column_widths = [max(map(len, col)) for col in zip(*data)]

    for rowIndex in range(len(data)):
        # create rows of data with correct spacing based on column width calculations
        print(' | '.join(format(val, f'{width}s') for val, width in zip(data[rowIndex], column_widths)))

        if rowIndex == 0:
            # print header row separator
            print('-' * (sum(column_widths) + 3 * len(column_widths) - 1))

    print()  # Add spacing between calls


def display_invalid_records():
    if len(invalid_student_records) > 0:
        print('\nInvalid Records')
        print('---------------')

        for student in invalid_student_records:
            print(student)

    else:
        print('No invalid records exist to display.')

    print()  # Add spacing between calls


def create_invalid_records_file():
    if len(invalid_student_records) > 0:
        try:
            with open('BADRECORDS.TXT', 'w') as file:
                file_writer = csv.writer(file)

                for student in invalid_student_records:
                    file_writer.writerow(student)

            print(f'\nBADRECORDS.TXT file created with {len(invalid_student_records)} invalid records.\n')

        except Exception as ex:
            print(f'\nUnable to create BADRECORDS.TXT file. {ex}\n')

    else:
        print('\nNo invalid records exist to write to file.\n')


def verify_python_3():
    # Halt execution if Python 3 or greater is not installed
    if sys.version_info[0] < 3:
        print('Python 3 or greater is required to run this program.')
        sys.exit(1)


def main():
    verify_python_3()
    handle_file_input()

    while True:
        handle_option_input()


if __name__ == "__main__":
    main()
