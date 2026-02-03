# DAY 9: Exam Schedule Tracker
my_externals = {

    "CAED": "Feb 2",
    "C-Programming": "Feb 5",
    "Mathematics": "Feb 8",
    "Physics": "Feb 12"
}
print("--- MY EXTERNAL EXAM TIMETABLE ---")
for subject, date in my_externals.items():
    print(f"Subject: {subject:15} | Date: {date}")
query = "C-Programming"
print(f"\nNext focus: {query} on {my_externals[query]}")