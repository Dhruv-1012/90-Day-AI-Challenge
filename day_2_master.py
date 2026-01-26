name = input("What is the name of the Hacker :")
name[::-1]
name_list = list(name)
name_list[1] ='w'
name1="".join(name_list)
print("The Hacker name is :",name1)
print("Hacker preview :",name1[0:3])