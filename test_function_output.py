import IN501_BrianLSmith_Project
import csv

valid_student_records = [
    ['1001', 'Arthur', 'Dallas', '100', 'MSIT'],
    ['1002', 'Thomas', 'Kane', '90', 'MSCM'],
    ['1003', 'Ellen', 'Ripley', '80', 'MSIT'],
    ['1005', 'Joan', 'Lambert', '70', 'MSIT'],
    ['1004', 'Dennis', 'Parker', '60', 'MSCM'],
    ['1006', 'Samuel', 'Brett', '50', 'MSCM'],
    ['1007', 'Ash', '[Synthetic]', '0', 'MSIT'],
]

invalid_student_records = [
    ['', 'Alpha', 'User', '45', 'MSIT'],
    ['2000', '', 'User', '20', 'MSCM'],
    ['3000', 'Charlie', '', '10', 'MSCM'],
    ['4000', 'Delta', 'User', '', 'MSIT'],
    ['5000', 'Echo', 'User', '95', ''],
    ['6000', 'Golf', 'User', '-50', 'MSIT'],
    ['7000', 'Hotel', 'User', '120', 'MSCM'],
    ['8000', 'Foxtrot', 'User', '100', 'BUJI'],
]


def setup_application_instance():
    instance = IN501_BrianLSmith_Project
    instance.student_records = valid_student_records
    instance.invalid_student_records = invalid_student_records

    return instance


def test_display_average_grade(capsys):
    instance = setup_application_instance()
    instance.display_average_grade_all_students()

    captured = capsys.readouterr()

    assert captured.out == '\nAverage grade of all students: 64.3\n\n'


def test_display_average_grade_for_each_program(capsys):
    instance = setup_application_instance()
    instance.display_average_grade_each_program()

    captured = capsys.readouterr()

    assert captured.out == '\nAverage grade of all students in each program\nMSIT: 62.5\nMSCM: 66.7\n\n'


def test_display_highest_grade_record(capsys):
    instance = setup_application_instance()
    instance.display_highest_grade_record()

    captured = capsys.readouterr()

    assert captured.out == '\nHighest student grade\n\n' \
                           'Student ID | Last, First Name | Program | Grade\n' \
                           '-------------------------------------------------\n' \
                           '1001       | Dallas, Arthur   | MSIT    | 100  \n\n'


def test_display_lowest_grade_record(capsys):
    instance = setup_application_instance()
    instance.display_lowest_grade_record()

    captured = capsys.readouterr()

    assert captured.out == '\nLowest student grade\n\n' \
                           'Student ID | Last, First Name | Program | Grade\n' \
                           '-------------------------------------------------\n' \
                           '1007       | [Synthetic], Ash | MSIT    | 0    \n\n'


def test_display_students_in_msit_program(capsys):
    instance = setup_application_instance()
    instance.display_students_in_msit_program()

    captured = capsys.readouterr()

    assert captured.out == '\nStudents in MSIT program:\n\n' \
                           'Student ID | Last, First Name | Grade\n' \
                           '---------------------------------------\n' \
                           '1001       | Dallas, Arthur   | 100  \n' \
                           '1005       | Lambert, Joan    | 70   \n' \
                           '1003       | Ripley, Ellen    | 80   \n' \
                           '1007       | [Synthetic], Ash | 0    \n\n'


def test_display_students_in_mscm_program(capsys):
    instance = setup_application_instance()
    instance.display_students_in_mscm_program()

    captured = capsys.readouterr()

    assert captured.out == '\nStudents in MSCM program:\n\n' \
                           'Student ID | Last, First Name | Grade\n' \
                           '---------------------------------------\n' \
                           '1006       | Brett, Samuel    | 50   \n' \
                           '1002       | Kane, Thomas     | 90   \n' \
                           '1004       | Parker, Dennis   | 60   \n\n'


def test_display_all_students_sorted_by_student_id(capsys):
    instance = setup_application_instance()
    instance.display_all_students_sorted_by_student_id()

    captured = capsys.readouterr()

    assert captured.out == '\nAll students sorted by student ID:\n\n' \
                           'Student ID | Last, First Name | Program | Grade\n' \
                           '-------------------------------------------------\n' \
                           '1001       | Dallas, Arthur   | MSIT    | 100  \n' \
                           '1002       | Kane, Thomas     | MSCM    | 90   \n' \
                           '1003       | Ripley, Ellen    | MSIT    | 80   \n' \
                           '1004       | Parker, Dennis   | MSCM    | 60   \n' \
                           '1005       | Lambert, Joan    | MSIT    | 70   \n' \
                           '1006       | Brett, Samuel    | MSCM    | 50   \n' \
                           '1007       | [Synthetic], Ash | MSIT    | 0    \n\n'


def test_display_invalid_records(capsys):
    instance = setup_application_instance()
    instance.display_invalid_records()

    captured = capsys.readouterr()

    assert captured.out == '\nInvalid Records\n' \
                           '---------------\n' \
                           "['', 'Alpha', 'User', '45', 'MSIT']\n" \
                           "['2000', '', 'User', '20', 'MSCM']\n" \
                           "['3000', 'Charlie', '', '10', 'MSCM']\n" \
                           "['4000', 'Delta', 'User', '', 'MSIT']\n" \
                           "['5000', 'Echo', 'User', '95', '']\n" \
                           "['6000', 'Golf', 'User', '-50', 'MSIT']\n" \
                           "['7000', 'Hotel', 'User', '120', 'MSCM']\n" \
                           "['8000', 'Foxtrot', 'User', '100', 'BUJI']\n\n"


def test_create_invalid_records_file(capsys):
    instance = setup_application_instance()
    instance.create_invalid_records_file()

    with open('BADRECORDS.TXT', 'r') as file:
        file_reader = csv.reader(file, delimiter=',')
        data = list(file_reader)

        for row in data:
            if row not in invalid_student_records:
                assert False
