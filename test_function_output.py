import IN501_BrianLSmith_Project

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

