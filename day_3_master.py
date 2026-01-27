# THE EXAM ORGANIZER
# QUESTION: 
# 1. Create a list of 3 subjects.
# 2. Add a new subject using .append().
# 3. Sort the list alphabetically.
# 4. Create a nested list [Subject, Hours] and access the 
#    second element of the second list.



subjects = ['Maths','C programing','Physics']
new_subject = input("Enter your next exterenal exam :")
subjects.append(new_subject)
subjects.sort()
print("My study list :",subjects)
study_plan = [['Maths',6],['C programing', 3],['Physics', 2]]
print(f"I will study {study_plan[1][0]} for {study_plan[1][1]} hours")