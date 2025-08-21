import csv

def read_text_file(filename):
    """Read and return contents of a text file"""
    with open(filename, mode="r", encoding="utf-8") as file:
        lines = [line.strip() for line in file]
        return lines

def read_csv_data(filename):
    """Read CSV file and return list of dictionaries"""
    with open(filename, mode="r", encoding="utf-8") as file:
        csv_reader = csv.DictReader(file)
        list = []
        for i in csv_reader:
            list.append(i)
        return list

def analyze_student_data(students):
    """Perform statistical analysis on student data"""
    num_students = len(students)
    average = 0
    score = -1
    score_2 = 100
    a = 0
    b = 0
    c = 0
    highest_score = ["", 0]
    lowest_score = ["", 0]
    for student in students:
        current_score = int(student["score"])
        average = average + current_score

        if current_score > score:
            highest_score[0] = student["name"]
            highest_score[1] = student["score"]
            score = current_score
        
        if current_score < score_2:
            lowest_score[0] = student["name"]
            lowest_score[1] = student["score"]
            score_2 = current_score

        if student["grade"].lower() == "a":
            a = a + 1
        elif student["grade"].lower() == "b":
            b = b + 1
        elif student["grade"].lower() == "c":
            c = c + 1
    

    average = round(float(average / num_students), 2)

    dic = {}
    dic["totalStudents"] = num_students
    dic["average"] = average
    dic["highScore"] = highest_score
    dic["lowScore"] = lowest_score
    dic["a"] = a
    dic["b"] = b
    dic["c"] = c

    return dic

def subject_analysis(students):
    math_average = 0
    english_average = 0
    science_average = 0
    math_students = 0
    english_students = 0
    science_students = 0

    for student in students:
        current_score = int(student["score"])
        if student["subject"].lower() == "math":
            math_average = math_average + current_score
            math_students = math_students + 1
        elif student["subject"].lower() == "science":
            science_average = science_average + current_score
            science_students = science_students + 1
        elif student["subject"].lower() == "english":
            english_average = english_average + current_score
            english_students = english_students + 1
    
    math_average = round(float(math_average / math_students), 2)
    english_average = round(float(english_average / english_students), 2)
    science_average = round(float(science_average / science_students), 2)
    
    dic = {}
    dic["math_average"] = math_average
    dic["science_average"] = science_average
    dic["english_average"] = english_average
    
    return dic

def parse_config(filename):
    """Parse configuration file into dictionary"""
    config = read_text_file(filename)
    dic = {}
    for con in config:
        information, value = con.split("=")
        information = " ".join(information.split("_"))
        dic[information] = value
    
    return dic

def create_filtered_csv(students, filename, condition):
    """Create new CSV file with filtered data"""
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        fieldnames = students[0].keys()
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for student in students:
            current_score = int(student["score"])

            if current_score >= condition:
                writer.writerow(student)

def main():
    config = parse_config("config.txt")
    keys = list(config.keys())
    length = len(keys)
    for i in range(length):
        print(f"{keys[i].title()}: {config[keys[i]].title()}")

    students = read_csv_data("students.csv")

    print("\n=== STUDENT ANALYSIS ===")
    students_analyze = analyze_student_data(students)

    print(f"Total Students: {students_analyze["totalStudents"]}")
    print(f"Average Score: {students_analyze["average"]}")
    print(f"Highest Score: {students_analyze["highScore"][1]} ({students_analyze['highScore'][0]})")
    print(f"Lowest Score: {students_analyze["lowScore"][1]} ({students_analyze['lowScore'][0]})")

    print("\nGrade Distribution:")
    grades = ["a", "b", "c"]
    for grade in grades:
        print(f"{grade.upper()}: {students_analyze[grade]} students")

    print("\n=== SUBJECT ANALYSIS ===")
    subject_analist = subject_analysis(students)

    keys_subject = list(subject_analist.keys())
    subject = []
    for key in keys_subject:
        a = ": ".join(key.split("_"))
        subject.append(a)
    length_subject = len(keys_subject)

    for x in range(length_subject):
        print(f"{subject[x].title()} {subject_analist[keys_subject[x]]}")

    print("\n=== STUDENTS NEEDING TUTORING ===")
    for student in students:
        current_score = int(student["score"])
        min_score = int(config["passing grade"])

        if current_score < min_score:
            print(f"{student["name"].title()} ({student["subject"].capitalize()}): {current_score}")

    create_filtered_csv(students, "high_performers.csv", 90)
    print("\n\nHigh Perfomers csv file created.")
    

if __name__ == "__main__":
    main()