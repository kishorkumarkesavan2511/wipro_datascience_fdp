import sys

list_of_students = {"Krishna":[67,68,69], "Arjun":[70,98,63], "Malika":[52,56,60]}

student_name = input("Enter the name of the student: ")
if student_name in list_of_students:
    student_scores = list_of_students[student_name]
    average_score = sum(student_scores) / len(student_scores)
    print(f"Marks for {student_name} are {student_scores} The average score is: {average_score}")