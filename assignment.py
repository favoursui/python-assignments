
"""
Task: Hundred Student Records - Filtering with Loops and Conditionals

Scenario:
The Federal University of Jos wants to analyze the performance of its students 
after conducting a nationwide online assessment. 
They have exactly 100 student records in the system.

Each student record includes:
- student_id (integer)
- name (string)
- score (0 - 100)

A sample of the dataset looks like this:

students = [
    {"id": 1, "name": "Alice", "score": 78},
    {"id": 2, "name": "Bob", "score": 45},
    {"id": 3, "name": "Charlie", "score": 92},
    ...
]

The academic board wants to classify the students into 3 separate groups 
based on their scores:

1. High Performers: score >= 70
2. Average Performers: 50 <= score < 70
3. Low Performers: score < 50

Requirements:
1. Use a loop to iterate through all student records.
2. Use conditionals to filter and classify students into 3 separate groups.
3. Each group should be identified by its name (Group Name).
4. Each group should use `student_id` as the key and a tuple `(name, score)` as the value.
5. Print the number of students in each category as a summary report.
6. print each category(3)

Example Output:
High Performers: 300,245
Average Performers: 400,512
Low Performers: 299,243


e.g. 
All High Performers: [{1: ("student1", 100)}, {32: ("student32", 90)}, ..... continously]
All Average Performers: [{1: ("student1", 100)}, {32: ("student32", 90)}, ..... continously]
All Low Performers: [{1: ("student1", 100)}, {32: ("student32", 90)}, ..... continously]
"""

students = [{'id': 1, 'name': 'Student1', 'score': 68}, {'id': 2, 'name': 'Student2', 'score': 86}, {'id': 3, 'name': 'Student3', 'score': 44}, {'id': 4, 'name': 'Student4', 'score': 60}, {'id': 5, 'name': 'Student5', 'score': 1}, {'id': 6, 'name': 'Student6', 'score': 25}, {'id': 7, 'name': 'Student7', 'score': 31}, {'id': 8, 'name': 'Student8', 'score': 85}, {'id': 9, 'name': 'Student9', 'score': 53}, {'id': 10, 'name': 'Student10', 'score': 33}, {'id': 11, 'name': 'Student11', 'score': 75}, {'id': 12, 'name': 'Student12', 'score': 2}, {'id': 13, 'name': 'Student13', 'score': 95}, {'id': 14, 'name': 'Student14', 'score': 36}, {'id': 15, 'name': 'Student15', 'score': 55}, {'id': 16, 'name': 'Student16', 'score': 57}, {'id': 17, 'name': 'Student17', 'score': 97}, {'id': 18, 'name': 'Student18', 'score': 44}, {'id': 19, 'name': 'Student19', 'score': 81}, {'id': 20, 'name': 'Student20', 'score': 20}, {'id': 21, 'name': 'Student21', 'score': 65}, {'id': 22, 'name': 'Student22', 'score': 68}, {'id': 23, 'name': 'Student23', 'score': 41}, {'id': 24, 'name': 'Student24', 'score': 16}, {'id': 25, 'name': 'Student25', 'score': 18}, {'id': 26, 'name': 'Student26', 'score': 88}, {'id': 27, 'name': 'Student27', 'score': 59}, {'id': 28, 'name': 'Student28', 'score': 89}, {'id': 29, 'name': 'Student29', 'score': 12}, {'id': 30, 'name': 'Student30', 'score': 13}, {'id': 31, 'name': 'Student31', 'score': 87}, {'id': 32, 'name': 'Student32', 'score': 20}, {'id': 33, 'name': 'Student33', 'score': 43}, {'id': 34, 'name': 'Student34', 'score': 36}, {'id': 35, 'name': 'Student35', 'score': 47}, {'id': 36, 'name': 'Student36', 'score': 14}, {'id': 37, 'name': 'Student37', 'score': 14}, {'id': 38, 'name': 'Student38', 'score': 61}, {'id': 39, 'name': 'Student39', 'score': 86}, {'id': 40, 'name': 'Student40', 'score': 87}, {'id': 41, 'name': 'Student41', 'score': 24}, {'id': 42, 'name': 'Student42', 'score': 61}, {'id': 43, 'name': 'Student43', 'score': 69}, {'id': 44, 'name': 'Student44', 'score': 56}, {'id': 45, 'name': 'Student45', 'score': 47}, {'id': 46, 'name': 'Student46', 'score': 27}, {'id': 47, 'name': 'Student47', 'score': 84}, {'id': 48, 'name': 'Student48', 'score': 71}, {'id': 49, 'name': 'Student49', 'score': 4}, {'id': 50, 'name': 'Student50', 'score': 43}, {'id': 51, 'name': 'Student51', 'score': 81}, {'id': 52, 'name': 'Student52', 'score': 99}, {'id': 53, 'name': 'Student53', 'score': 57}, {'id': 54, 'name': 'Student54', 'score': 94}, {'id': 55, 'name': 'Student55', 'score': 99}, {'id': 56, 'name': 'Student56', 'score': 67}, {'id': 57, 'name': 'Student57', 'score': 54}, {'id': 58, 'name': 'Student58', 'score': 17}, {'id': 59, 'name': 'Student59', 'score': 77}, {'id': 60, 'name': 'Student60', 'score': 35}, {'id': 61, 'name': 'Student61', 'score': 40}, {'id': 62, 'name': 'Student62', 'score': 22}, {'id': 63, 'name': 'Student63', 'score': 7}, {'id': 64, 'name': 'Student64', 'score': 19}, {'id': 65, 'name': 'Student65', 'score': 1}, {'id': 66, 'name': 'Student66', 'score': 24}, {'id': 67, 'name': 'Student67', 'score': 74}, {'id': 68, 'name': 'Student68', 'score': 34}, {'id': 69, 'name': 'Student69', 'score': 42}, {'id': 70, 'name': 'Student70', 'score': 42}, {'id': 71, 'name': 'Student71', 'score': 35}, {'id': 72, 'name': 'Student72', 'score': 22}, {'id': 73, 'name': 'Student73', 'score': 32}, {'id': 74, 'name': 'Student74', 'score': 88}, {'id': 75, 'name': 'Student75', 'score': 28}, {'id': 76, 'name': 'Student76', 'score': 5}, {'id': 77, 'name': 'Student77', 'score': 73}, {'id': 78, 'name': 'Student78', 'score': 55}, {'id': 79, 'name': 'Student79', 'score': 62}, {'id': 80, 'name': 'Student80', 'score': 87}, {'id': 81, 'name': 'Student81', 'score': 21}, {'id': 82, 'name': 'Student82', 'score': 88}, {'id': 83, 'name': 'Student83', 'score': 62}, {'id': 84, 'name': 'Student84', 'score': 19}, {'id': 85, 'name': 'Student85', 'score': 60}, {'id': 86, 'name': 'Student86', 'score': 23}, {'id': 87, 'name': 'Student87', 'score': 46}, {'id': 88, 'name': 'Student88', 'score': 25}, {'id': 89, 'name': 'Student89', 'score': 17}, {'id': 90, 'name': 'Student90', 'score': 49}, {'id': 91, 'name': 'Student91', 'score': 34}, {'id': 92, 'name': 'Student92', 'score': 11}, {'id': 93, 'name': 'Student93', 'score': 87}, {'id': 94, 'name': 'Student94', 'score': 56}, {'id': 95, 'name': 'Student95', 'score': 91}, {'id': 96, 'name': 'Student96', 'score': 30}, {'id': 97, 'name': 'Student97', 'score': 92}, {'id': 98, 'name': 'Student98', 'score': 77}, {'id': 99, 'name': 'Student99', 'score': 22}, {'id': 100, 'name': 'Student100', 'score': 39}]


#Create empty lists for each category
high_performers = []
average_performers = []
low_performers = []

#Loop and classify
for student in students:
    student_entry = {student["id"]: (student["name"], student["score"])}
    score = student["score"]

    if score >= 70:
        high_performers.append(student_entry)
    elif score >= 50 and score < 70:
        average_performers.append(student_entry)
    else:
        low_performers.append(student_entry)

#Summary Report
print("Summary Report:")
print("High Performers: {}" .format ({len(high_performers)}))
print("Average Performers: {}" .format ({len(average_performers)}))
print("Low Performers: {}" .format ({len(low_performers)}))

#Print each category
print("High Performers:", high_performers)
print("Average Performers:", average_performers)
print("Low Performers:", low_performers)



































