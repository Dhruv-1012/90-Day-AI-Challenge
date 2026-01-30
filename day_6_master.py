# QUESTION: Create a nested dictionary representing a student profile, update an existing key, add a new key-value pair, and print all items using .items() ?

student_profile = {"name":"Dhruv","course":"B.E. CSE","skills":["python","C","Data Structures"],"details":{"collage":"SMVIT","year":"1st"}}
student_profile["name"]="Dhruv Aryan"
student_profile["status"]="Active"
print("Collage Name:",student_profile["details"]["collage"])
print("Keys:",list(student_profile.keys()))
print("All Data:",student_profile.items())
