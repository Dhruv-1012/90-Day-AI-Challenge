# DAY 15: Mastering Functions and Logic
# Using only what I have studied so far
#1 Defining the function
def evaluate_performance(score):
    if score >= 90:
        return "Excellent"
    elif score >= 75:
        return "Good"
    elif score >= 40:
        return "Pass"
    else:
        return "Need Improvement"
#2 Data (Dictionary)
my_results = {
    "C-Programming": 82,
    "Mathematics": 91,
    "Physics": 78
}
print("--- EXAM PERFORMANCE REPORT ---")
#3 Using a Loop to call the Function
for subject, marks in my_results.items():
    rating = evaluate_performance(marks)
    print(f"{subject}: {marks} -> {rating}")
