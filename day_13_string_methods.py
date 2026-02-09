# DAY 13: String Manipulation & Formatting
# Useful for cleaning up data or study notes
raw_topics = "  pointers, structures, file handling, linked lists  "
# Cleaning the string (Removing extra spaces)
cleaned_topics = raw_topics.strip()
# Converting to a List
topics_list = cleaned_topics.split(", ")

print("--- FORMATTED STUDY TOPICS ---")
# Capitalizing each topic and printing
for topic in topics_list:
    print(f"- {topic.title()}")
# Counting total topics
print(f"\nTotal topics to cover: {len(topics_list)}")