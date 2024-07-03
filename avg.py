def print_average_marks(students):
    averages = [(student, sum(marks) / len(marks)) for student, marks in students.items()]
    
    
    sorted_averages = sorted(averages, key=lambda x: x[1], reverse=True)
    
   
    for student, avg in sorted_averages:
        print(f"{student}: {avg:.2f}")


students = {
    "Alice": [85, 90, 92],
    "Bob": [78, 85, 88],
    "Charlie": [92, 95, 88],
    "David": [80, 82, 85]
}

print_average_marks(students)
