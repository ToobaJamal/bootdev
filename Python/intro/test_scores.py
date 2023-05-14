'''
Loop over the answer_sheet and student_answers lists. Calculate the student's score as a percentage and store it in a variable called percentage.

For example, if these were the lists:

answer_sheet = ["A", "A", "C", "D"]
student_answers = ["A", "B", "C", "D"]
Then the percentage would be 75.0. The percentage should be a float, not an integer.
'''

answer_sheet = ["A", "A", "C", "D", "D", "B", "C", "A", "C", "B", "A", "D", "C", "B", "D", "C", "B", "A", "D", "A"]
student_answers = ["A", "B", "C", "A", "D", "B", "C", "A", "C", "B", "A", "A", "C", "B", "D", "C", "B", "A", "D", "A"]

# Don't touch above this line
total = len(answer_sheet)
obtained = 0
for i in range(0, len(answer_sheet)):
    if answer_sheet[i] == student_answers[i]:
        obtained += 1

percentage = obtained/total * 100

# Don't touch below this line

print(f"The student answered correctly on {percentage}% of the questions")
