# Student Record System
This is the course project for Purdue Global IN501 Fundamentals of Computer Programming.

## Functionality:
1. Ask user to input the name of a valid record file within the same directory as the program root.
2. If the file does not exist, print error message and request input again.
3. If user enters the word "exit", the program will terminate.
4. Parse student records file:
    - For each line in the file, split the line into a list of strings.
      - If any value is empty, print error message and skip to next record.
      - If grade value is below 0 or above 100, print error message and skip to next record.
      - If student program is not in MSIT or MSCM, print error message and skip to next record.
      - Catch any potential exceptions and request user input again.
5. Print a list of user actions.
6. Ask use to input a number corresponding to a valid action.
    - If 0, terminate program.
    - If 1, display average grade for all students.
    - If 2, display average grade for all students in a specific program.
    - If 3, display highest student grade.
    - If 4, display lowest student grade.
    - If 5, display all students in MSIT program.
    - If 6, display all students in MSCM program.
    - If 7, display all students sorted by student ID.
    - If 8, display invalid records.
    - If 9, create file named "BADRECORDS.TXT" containing all invalid input records.
    - If an unknown option exists, print error message and request input again.
