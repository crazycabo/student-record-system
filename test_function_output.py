import IN501_BrianLSmith_Project


valid_student_records = [
    ['1001', 'Arthur', 'Dallas', '100', 'MSIT'],
    ['1002', 'Thomas', 'Kane', '90', 'MSCM'],
    ['1003', 'Ellen', 'Ripley', '80', 'MSIT'],
    ['1005', 'Joan', 'Lambert', '70', 'MSIT'],
    ['1004', 'Dennis', 'Parker', '60', 'MSCM'],
    ['1006', 'Samuel', 'Brett', '50', 'MSCM'],
    ['1007', 'Ash', '[Synthetic Nightmare]', '0', 'MSIT'],
]


def test_display_average_grade(capsys):
    instance = IN501_BrianLSmith_Project

    instance.student_records = valid_student_records

    instance.display_average_grade_all_students()

    captured = capsys.readouterr()
    assert captured.out == '\nAverage grade of all students: 64.3\n\n'


def test_display_average_grade_for_each_program(capsys):
    instance = IN501_BrianLSmith_Project

    instance.student_records = valid_student_records

    instance.display_average_grade_each_program()

    captured = capsys.readouterr()

    assert captured.out == '\nAverage grade of all students in each program\nMSIT: 62.5\nMSCM: 66.7\n\n'

