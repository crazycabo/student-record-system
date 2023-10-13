import sys
import csv
import pprint
import math


student_records = []
invalid_student_records = []


def handle_file_input():
    file_name = input('Enter file name: ')

    # todo: validate file exists before attempting to open

    with open(file_name, 'r') as file:
        file_reader = csv.reader(file, delimiter=',')

        for row in file_reader:
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

    print(f'\nProcessed {len(student_records)} student records and {len(invalid_student_records)} invalid records.\n')


def display_user_options():
    print('Choose one of the following options')
    print('----------------------------------------------')
    print('1. Display average grade for all students')
    print('2. Display average grade for each program')
    print('3. Display highest grade record')
    print('4. Display lowest grade record')
    print('5. Display all students in MSIT program')
    print('6. Display all students in MSCM program')
    print('7. Display all students in sorted order by student ID')
    print('8. Display invalid records')
    print('9. Create new file containing invalid records')
    print('0. Exit program\n')


def handle_option_input():
    user_input = int(input('Input option by number: '))
    # todo: Validate user input is an integer

    if user_input == 1:
        calculate_average_grade_all_students()

    elif user_input == 2:
        calculate_average_grade_each_program()

    elif user_input == 3:
        get_highest_grade_record()

    elif user_input == 4:
        get_lowest_grade_record()

    elif user_input == 5:
        # todo: Display all students in MSIT program
        pass

    elif user_input == 6:
        # todo: Display all students in MSCM program
        pass

    elif user_input == 7:
        # todo: Display all students in sorted order by student ID
        pass

    elif user_input == 8:
        display_invalid_records()

    elif user_input == 9:
        # todo: Create a new file containing invalid records
        pass

    elif user_input == 0:
        # Exit the program
        sys.exit(0)

    else:
        print('Invalid option selected. Please try again.\n')


def calculate_average_grade_all_students():
    sum_of_all_grades = 0
    student_count = 0

    # Round each input grade up, add to sum, and increment student count
    for student in student_records:
        sum_of_all_grades += math.ceil(float(student[3]))
        student_count += 1

    print(f'\nAverage grade of all students: {sum_of_all_grades / student_count:.1f}\n')


def calculate_average_grade_each_program():
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

    print('\nAverage grade of all students in each program')
    print(f'MSIT: {sum_of_all_grades_msit / student_count_msit:.1f}')
    print(f'MSCM: {sum_of_all_grades_mscm / student_count_mscm:.1f}\n')


def get_highest_grade_record():
    highest_grade = 0

    for student in student_records:
        if float(student[3]) > highest_grade:
            highest_grade = float(student[3])

    print(f'\nHighest student grade: {highest_grade:.1f}\n')


def get_lowest_grade_record():
    lowest_grade = 100

    for student in student_records:
        if float(student[3]) < lowest_grade:
            lowest_grade = float(student[3])

    print(f'\nLowest student grade: {lowest_grade:.1f}\n')


def display_invalid_records():
    pp = pprint.PrettyPrinter(indent=4)

    print('\nInvalid Records')

    pp.pprint(invalid_student_records)

    print()


def verify_python_3():
    # Halt execution if Python 3 or greater is not installed
    if sys.version_info[0] < 3:
        print('Python 3 or greater is required to run this program.')
        sys.exit(1)


if __name__ == "__main__":
    verify_python_3()
    handle_file_input()

    while True:
        display_user_options()
        handle_option_input()
