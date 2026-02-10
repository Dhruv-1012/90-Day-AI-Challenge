# DAY 14: Handling Specific Exceptions
# Learning to prevent the 'ZeroDivision' crash
print("--- Average Marks Calculator ---")
try:
    total_marks = int(input("Enter total marks: "))
    total_subjects = int(input("Enter number of subjects: "))
    # Logic that might fail if subjects = 0
    average = total_marks / total_subjects
    print(f"Your average is: {average:.2f}")
except ValueError:
    print("Error: Please enter numbers only!")
except ZeroDivisionError:
# This prevents the program from crashing if the user enters 0 subject
    print("Error: You cannot divide by zero subjects!")
finally:
    print("Thank you for using the SMVIT Calculator.")