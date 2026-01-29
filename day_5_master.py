# QUESTION: Create a list with duplicates, convert to set, add an item, and test remove vs discard.

raw_guests = ["Dhruv", "Rahul", "Dhruv", "Sneha", "Rahul", "Amit"]
unique_guests = set(raw_guests)
print("Unique Guest List:", unique_guests)
unique_guests.add("Vihaan")
unique_guests.remove("Sneha") 
unique_guests.discard("Sneha") 
print("Final Guests after removals:", unique_guests)
print("Total Unique Guests:", len(unique_guests))