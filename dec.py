def compare_student_averages(student1_name, student1_marks, student2_name, student2_marks):
   
    avg1 = sum(student1_marks) / len(student1_marks)
    avg2 = sum(student2_marks) / len(student2_marks)
    
   
    print(f"{student1_name}'s average: {avg1:.2f}")
    print(f"{student2_name}'s average: {avg2:.2f}")
    
    if avg1 > avg2:
        print(f"{student1_name} has a higher average.")
    elif avg2 > avg1:
        print(f"{student2_name} has a higher average.")
    else:
        print("Both students have the same average.")


student1 = "Alice"
alice_marks = [85, 90, 88, 92, 95]

student2 = "Bob"
bob_marks = [78, 85, 90, 88, 82]

compare_student_averages(student1, alice_marks, student2, bob_marks)
