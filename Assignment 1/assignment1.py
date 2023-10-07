"""
Author: Harmanpreet Singh Phull
Desc: A basic "miniature" version of BearTracks
"""

def GetStudents():
    """
    Gets the Student Info from the file Students.txt
    Input: None
    Return: Dictionary
    """
    with open("students.txt", "r") as file:
        line = file.readline().rstrip("\n")
        StudentsInfo = {}
        # loops until there are no more lines in the file
        while not line == "":
            Temp = line.split(",")
            # makes a dictionary with the StudentID as the key
            StudentsInfo[Temp[0]] = [Temp[1].strip(), Temp[2].strip()]
            line = file.readline().rstrip("\n")
    return StudentsInfo

def GetCourses():
    """
    Gets the Course Info from the file Courses.txt
    Input: None
    Return: Dictionary
    """
    with open("courses.txt", "r") as file:
        line = file.readline().rstrip("\n")
        CoursesInfo = {}
        while not line == "":
            Temp = line.split(";")
            # makes a dictionary with the Course Name as the key
            CoursesInfo[Temp[0]] = [Temp[1].strip(), int(Temp[2].strip()), Temp[3].strip()]
            line = file.readline().rstrip("\n")
    return CoursesInfo

def GetEnrollment():
    """
    Gets the Enrollment Info from the file Enrollment.txt
    Input: None
    Return: Dictionary
    """
    with open("enrollment.txt", "r") as file:
        line = file.readline().rstrip("\n")
        EnrollmentInfo = {}
        while not line == "":
            Temp = line.split(":")
            # makes a dictionary with the StudentID as the key
            if (Temp[1].strip() not in EnrollmentInfo):
                EnrollmentInfo[Temp[1].strip()] = [Temp[0].strip()]
            else:
                EnrollmentInfo[Temp[1].strip()].append(Temp[0].strip())
            line = file.readline().rstrip("\n")
    return EnrollmentInfo

def CheckStudentID():
    """
    Checks if the entered Student is valid or not
    Input: None
    Return: String
    """
    StudentID = input("\nStudent ID: ")
    # if the StudentID entered is valid returns it
    if (StudentID in GetStudents()):
        return StudentID

def Choice1(StudentsInfo, CoursesInfo, EnrollmentInfo):
    """
    Prints the timetable - simple
    Input: Dictionaries
    Return: None
    """
    StudentID = CheckStudentID()
    if (StudentID):
        print(f"Timetable for {StudentsInfo[StudentID][1].upper()}, in the faculty of {StudentsInfo[StudentID][0]}.")
        print(
            " " * 17 + "8:00" + " " * 9 + "9:00" + " " * 8 + "10:00" + " " * 8 + "11:00" + " " * 8 + "12:00" + " " * 8 + "13:00" + " " * 8 + "14:00" + " " * 8 + "15:00" + " " * 8 + "16:00" + " " * 5)
        print(" " * 12 + "+" + "------------+" * 9)
        # stores all the mwf courses in the correct time order
        MWFCourses = ["STAT 151", "CMPUT 175", "STAT 252", "MATH 100", "MATH 101", "MATH 201", "MATH 125", "ENGL 125", ""]
        # stores all the mwf courses the student is enrolled in
        MWFCoursesU = []
        for i in MWFCourses:
            # appends the course to the updated list
            if i in EnrollmentInfo[StudentID]:
                temp = i.split(" ")
                # if the subject name is more than 4 edits it
                if (len(temp[0]) > 4):
                    temp[0] = temp[0][:3] + "*"
                    MWFCoursesU.append(f"{temp[0]} {temp[1]}")
                else:
                    MWFCoursesU.append(i)
            # appends a space to the updated list
            else:
                MWFCoursesU.append("        ")
                MWFCourses[MWFCourses.index(i)] = "x"
        Line1 = "Mon/Wed/Fri |"
        # prints all the mwf courses
        for i in range(9):
            Line1 += f"  {MWFCoursesU[i]}  |"
        print(Line1)
        Line2 = "            |"
        for i in range(9):
            if MWFCourses[i] == "x":
                Line2 += "            |"
            else:
                Line2 += f"    {CoursesInfo[MWFCourses[i]][1]:^4}    |"
        print(Line2)
        print("            +" + "--------------------------------------+" * 3)
        # stores all the tr courses in the correct time order
        TRCourses = ["CMPUT 174", "CMPUT 274", "MATH 209", "CMPUT 272", "CMPUT 101", "ENGL 102", ""]
        # stores all the tr courses the student is enrolled in
        TRCoursesU = []
        if ("CMPUT 174" in EnrollmentInfo[StudentID]):
            TRCourses.pop(1)
        else:
            TRCourses.pop(0)
        # works the same way as the mwf course loop
        for i in TRCourses:
            if i in EnrollmentInfo[StudentID]:
                temp = i.split(" ")
                if (len(temp[0]) > 4):
                    temp[0] = temp[0][:3] + "*"
                    TRCoursesU.append(f"{temp[0]} {temp[1]}")
                else:
                    TRCoursesU.append(i)
            else:
                TRCoursesU.append("        ")
                TRCourses[TRCourses.index(i)] = "x"
        Line3 = " Tues/Thurs "
        for i in range(6):
            if (i == 2 or i == 4):
                Line3 += f"     {TRCoursesU[i]}     |"
            else:
                Line3 += f"|     {TRCoursesU[i]}     |"
        print(Line3)
        Line4 = "            "
        for i in range(6):
            if (i == 2 or i == 4):
                if TRCourses[i] == "x":
                    Line4 += "                  |"
                else:
                    Line4 += f"       {CoursesInfo[TRCourses[i]][1]:^4}       |"
            else:
                if TRCourses[i] == "x":
                    Line4 += "|                  |"
                else:
                    Line4 += f"|       {CoursesInfo[TRCourses[i]][1]:^4}       |"
        print(Line4)
        print("            +" + "--------------------------------------+" * 3)
    else:
        print("Invalid student ID. Cannot print timetable.\n")

def Choice2(StudentsInfo, CoursesInfo, EnrollmentInfo):
    """
    Enrolls in a selected course if it's valid and there's no time conflict
    Input: Dictionaries
    Return: None
    """
    StudentID = CheckStudentID()
    if (StudentID):
        EnrollCourse = input("Course Name: ")
        if (EnrollCourse in CoursesInfo):
            Conflict = False
            for Course in EnrollmentInfo[StudentID]:
                if (CoursesInfo[Course][0] == CoursesInfo[EnrollCourse][0]):
                    Conflict = True
            if (Conflict):
                print(f"Schedule conflict: Already registered for a course on {CoursesInfo[EnrollCourse][0]}")
            else:
                if (CoursesInfo[EnrollCourse][1] > 0):
                    CoursesInfo[EnrollCourse][1] -= 1
                    EnrollmentInfo[StudentID].append(EnrollCourse)
                    print(f"{StudentsInfo[StudentID][1]} has successfully been enrolled in {EnrollCourse}, on {CoursesInfo[EnrollCourse][0]}")
                else:
                    print("No more available seats.")
        else:
            print("Invalid course name.\n")
    else:
        print("Invalid student ID. Cannot continue with course enrollment.\n")

def Choice3(CoursesInfo, EnrollmentInfo):
    """
    Drops the selected course
    Input: Dictionaries
    Return: None
    """
    StudentID = CheckStudentID()
    if (StudentID):
        print("Select course to drop:")
        # prints the course in ascending order
        for Course in sorted(EnrollmentInfo[StudentID]):
            print(f"- {Course}")
        DropCourse = input("> ")
        #removes the course from the EnrollmentInfo and subtracts 1 from the available seats
        if (DropCourse in CoursesInfo):
            EnrollmentInfo[StudentID].pop(EnrollmentInfo[StudentID].index(DropCourse))
            CoursesInfo[DropCourse][1] += 1
        else:
            print("Invalid course name.\n")
    else:
        print("Invalid student ID. Cannot continue with course drop.\n")

def Menu():
    """
    Displays the menu and loops until the user wants to
    Input: None
    Return: None
    """
    StudentsInfo = GetStudents()
    CoursesInfo = GetCourses()
    EnrollmentInfo = GetEnrollment()
    print("==========================")
    print("Welcome to Mini-BearTracks")
    print("==========================")
    Quit = False
    while not Quit:
        print("\nWhat would you like to do?")
        print("1. Print Timetable")
        print("2. Enroll in course")
        print("3. Drop Course")
        print("4. Quit")
        Choice = input("> ")
        # loops until the option isn't correct
        while Choice not in ["1", "2", "3", "4"]:
            print("\nSorry, invalid entry. Please enter a choice from 1 to 4.")
            Choice = input("> ")
        if (Choice == "1"):
            Choice1(StudentsInfo, CoursesInfo, EnrollmentInfo)
        elif (Choice == "2"):
            Choice2(StudentsInfo, CoursesInfo, EnrollmentInfo)
        elif (Choice == "3"):
            Choice3(CoursesInfo, EnrollmentInfo)
        elif (Choice == "4"):
            print("Goodbye")
            Quit = True

def Main():
    Menu()

Main()