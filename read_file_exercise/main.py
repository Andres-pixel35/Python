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

    average = round(float(average / num_students), 2)

    dic = {}
    dic["totalStudents"] = num_students
    dic["average"] = average
    dic["highScore"] = highest_score
    dic["lowScore"] = lowest_score

    return dic

def parse_config(filename):
    """Parse configuration file into dictionary"""
    # Your implementation here
    pass

def create_filtered_csv(students, filename, condition):
    """Create new CSV file with filtered data"""
    # Your implementation here
    pass

def main():
    config = read_text_file("config.txt")
    print("=== CONFIGURATION ===")
    for con in config:
        information, value = con.split("=")
        print(f"{information.title()}: {value.title()}")

    students = read_csv_data("students.csv")

    print("\n=== STUDENT ANALYSIS ===")
    students_analyze = analyze_student_data(students)

    print(f"Total Students: {students_analyze["totalStudents"]}")
    print(f"Average Score: {students_analyze["average"]}")
    print(f"Highest Score: {students_analyze["highScore"][1]} ({students_analyze['highScore'][0]})")
    print(f"Lowest Score: {students_analyze["lowScore"][1]} ({students_analyze['lowScore'][0]})")
    


if __name__ == "__main__":
    main()