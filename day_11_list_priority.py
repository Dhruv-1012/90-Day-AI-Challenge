# # DAY 11: List Management & Slicing
# The Task:
# Create a List of all your remaining subjects.
# Use a List Method (.pop() or .remove()) to clear the subject you finished today (CAED).
# Use Slicing ([:]) to create a "Top 2" list of the most urgent exams

exams = ["CAED", "C-Programming", "Mathematics", "Physics", "Chemistry"]
completed = exams.pop(0) 
print(f"Completed and removed: {completed}")
exams.sort()
next_two = exams[0:2]
print(f"Remaining Exams: {exams}")
print(f"Urgent focus for tonight: {next_two}")