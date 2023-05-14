'''
Complete the test_score function. It should calculate a report that describes the percentage of multiple-choice answers a student got right on their test.

Inputs
answer_sheet: A list of the correct multiple-choice answers
student_answers: A list where the first index is the name of the student, but the rest of the list consists of the student's multiple-choice answers.
Output
The function should return 2 values:

name: a string
percentage: a float
'''

def test_score(answer_sheet, student_answers):
    name = student_answers[0]
    total = len(answer_sheet)
    obtained = 0
    for i in range(0, len(answer_sheet)):
        if answer_sheet[i] == student_answers[i + 1]:
            obtained += 1
    return name, (obtained / total) * 100
            


# Don't touch below this line


def test(answer_sheet, student_1_answers):
    name, percentage = test_score(answer_sheet, student_1_answers)
    print(f"{name}: {percentage:.1f}%")


def main():
    answer_sheet = [
        "A",
        "A",
        "C",
        "D",
        "D",
        "B",
        "C",
        "A",
        "C",
        "B",
        "A",
        "D",
        "C",
        "B",
        "D",
        "C",
        "B",
        "A",
        "D",
        "A",
    ]
    student_1_answers = [
        "Allan",
        "A",
        "C",
        "C",
        "B",
        "D",
        "B",
        "C",
        "A",
        "C",
        "B",
        "A",
        "A",
        "C",
        "B",
        "D",
        "C",
        "B",
        "A",
        "D",
        "A",
    ]
    student_2_answers = [
        "John",
        "A",
        "D",
        "A",
        "A",
        "D",
        "A",
        "C",
        "B",
        "D",
        "A",
        "F",
        "A",
        "C",
        "B",
        "D",
        "C",
        "D",
        "C",
        "D",
        "A",
    ]
    student_3_answers = [
        "Jeremy",
        "A",
        "B",
        "D",
        "C",
        "D",
        "B",
        "D",
        "A",
        "C",
        "C",
        "D",
        "A",
        "C",
        "B",
        "D",
        "C",
        "B",
        "A",
        "F",
        "A",
    ]
    student_4_answers = [
        "Sally",
        "A",
        "A",
        "D",
        "A",
        "A",
        "B",
        "C",
        "A",
        "C",
        "B",
        "A",
        "A",
        "C",
        "B",
        "D",
        "C",
        "F",
        "A",
        "D",
        "A",
    ]
    student_5_answers = [
        "Tim",
        "A",
        "A",
        "C",
        "D",
        "D",
        "B",
        "C",
        "A",
        "C",
        "B",
        "A",
        "D",
        "C",
        "B",
        "D",
        "C",
        "B",
        "A",
        "D",
        "A",
    ]

    test(answer_sheet, student_1_answers)
    test(answer_sheet, student_2_answers)
    test(answer_sheet, student_3_answers)
    test(answer_sheet, student_4_answers)
    test(answer_sheet, student_5_answers)


main()
