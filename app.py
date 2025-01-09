def students_detail():
    name: str = input("Enter your name: ")
    student_class: int = int(input("Enter your class: "))
    rollno: int = int(input("Enter your roll number: "))
    marks: float = []
    
    for i in range(1, 6):
        input_marks = int(input(f"Enter marks for subject {i}: "))
        if input_marks >= 0 and input_marks <= 100:
            marks.append(input_marks)
        elif input_marks < 0 or input_marks > 100:
            print("Invalid marks. Marks should be between 0 and 100.")

    return {
        "name": name, 
        "class": student_class, 
        "rollno": rollno, 
        "marks": marks,
        }


def percentage_and_grade(marks):
    total_marks = sum(marks)
    percentage = (total_marks / 500) * 100
    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"
    return percentage, grade

def show_student_details(name, student_class, rollno, marks):
    print("Student Details:")
    print("Name:", name)
    print("Class:", student_class)
    print("Roll Number:", rollno)
    print("Marks:", marks)
    percentage, grade = percentage_and_grade(marks)
    print(f"Percentage:, {percentage:.2f}%")
    print("Grade:", grade)

def marks_comparing_between_two_students(student1, student2):
    print("****Marks comparing between student 1 and student 2****")
    marks1 = student1["marks"]
    marks2 = student2["marks"]
    for i in range(1, 6):
        diff = marks1[i - 1] - marks2[i - 1]
        if diff > 0:
            print(f"Student 1 scored {diff} more marks than student 2 in subject {i}")
        elif diff < 0:
            print(f"Student 2 scored {abs(diff)} more marks than student 1 in subject {i}")
        elif diff == 0:
            print(f"Student 1 and student 2 scored same marks in subject {i}")
        else:
            print("Invalid marks")

def main():
    print("****Student 1****")
    student1 = students_detail()
    print("****Student 2****")
    student2 = students_detail()
    print(student1)
    print(student2)
    marks_comparing_between_two_students(student1, student2)

if __name__ == "__main__":
    main()