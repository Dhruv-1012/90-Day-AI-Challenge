# DAY 8 PROJECT: Student Portfolio & Performance Tracker

def calculate_average(marks_list):
    total = sum(marks_list)
    average = total / len(marks_list)
    return round(average, 2)

student_data = {
    'Dhruv': {
        'marks': [85, 92, 78],
        'skills': {'Python', 'C', 'CAED'},
        'college': 'SMVIT'
    },
    'Aryan': {
        'marks': [80, 88, 95],
        'skills': {'Java', 'DSA', 'Python'},
        'college': 'SMVIT'
    }
}
print("--- STUDENT PERFORMANCE REPORT ---")
for name, info in student_data.items():
    avg = calculate_average(info['marks'])
    print(f"Student: {name}")
    print(f"Average Grade: {avg}%")
    print(f"Skillset: {', '.join(info['skills'])}")
    print("-" * 30)