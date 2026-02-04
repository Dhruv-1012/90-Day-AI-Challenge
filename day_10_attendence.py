# DAY 10: Attendance Logic Challenge

total_class = ["Dhruv", "Aryan", "Shubham", "Sahil", "Varun"]
attended_lab = ["Dhruv", "Shubham", "Varun"]
print("--- ABSENTEE REPORT ---")
for student in total_class:
    if student not in attended_lab:
        print(f"ALERT: {student} was absent from the lab.")
print(f"\nTotal present: {len(attended_lab)} out of {len(total_class)}")