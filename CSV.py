import csv

# Initialize subject totals
total_math = 0
total_science = 0
total_english = 0
num_students = 0
top_student = ""
top_avg = 0

with open("marks.csv", newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    
    print("Student Averages:")
    for row in reader:
        name = row["Name"]
        math = int(row["Math"])
        science = int(row["Science"])
        english = int(row["English"])
        
        # Student average
        average = (math + science + english) / 3
        print(f"{name} - Average: {average:.2f}")
        
        # Update top student
        if average > top_avg:
            top_avg = average
            top_student = name
        
        # Update subject totals
        total_math += math
        total_science += science
        total_english += english
        num_students += 1

# Calculate class averages
class_avg_math = total_math / num_students
class_avg_science = total_science / num_students
class_avg_english = total_english / num_students

print("\nClass Average per Subject:")
print(f"Math: {class_avg_math:.2f}")
print(f"Science: {class_avg_science:.2f}")
print(f"English: {class_avg_english:.2f}")

print(f"\nTop Student: {top_student} with Average: {top_avg:.2f}")
