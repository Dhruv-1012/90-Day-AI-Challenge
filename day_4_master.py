# QUESTION: Create a tuple, access its 3rd element, use .count() and .index() methods, and demonstrate immutability using min/max/len.

t = (2,4,4,6,8,9,'dhruv',True,5+6j)
print("3rd Element:",t[2])
print("Count of 4:",t.count(4))
print("Index of 'dhruv':",t.index("dhruv"))
# t[5]= 'hello' #This would cause an Error: 'tuple' object does not support item assignment
t_nums = (3,4,5,6,2,4,5,3,4,56,4353,2,2,3,3,53)
print("Min:", min(t_nums))
print("Max:", max(t_nums))
print("Len:", len(t_nums))