# PROJECT:
# A simple student search system 
# Combining Dictionaries, Lists and Sets

students = { '101':{'Name':'Dhruv','Subjects':{'Python','C','Math'},'Marks':[85,90,84]},
            '102':{'Name': 'Aryan','Subject':{'Python','Java','DSA'},'Marks':[88,94,79]}}
students['103'] = {'Name':'Shubham','Subject':{'Python','C++','AIML'},'Marks':[90,85,98]}


search_id = '101'
if search_id in students:
    print(f"\nStudent Found:{students[search_id]['Name']}")
else:
    print("Student Not Found.")
print("Display all students IDs")
print("Current Database IDs:\n",list(students.keys()))
