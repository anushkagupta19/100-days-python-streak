# Given the names and grades for each student in a class of  students,
#  store them in a nested list and print the name(s) of any student(s) 
# having the second lowest grade.

if __name__ == '__main__':
    # Create a nested list to store student names and their grades.
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    # Find the second lowest grade.
    # 1. Create a set of all the scores to get unique values.
    # 2. Convert the set to a list and sort it.
    # 3. The second element (at index 1) is the second lowest grade.
    second_lowest_grade = sorted(list(set([score for name, score in students])))[1]

    # Find all students who have the second lowest grade, sort their names, and print them.
    for name in sorted([name for name, score in students if score == second_lowest_grade]):
        print(name)

