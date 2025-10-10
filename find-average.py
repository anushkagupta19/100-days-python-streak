# The provided code stub will read in a dictionary 
# containing key/value pairs of name:[marks] for a 
# list of students. Print the average of the marks array 
# for the student name provided, showing 2 places after the decimal.


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    # Find the marks for the student specified by query_name
    marks_to_average = student_marks.get(query_name)

    # Calculate the average of the marks
    if marks_to_average:
        average = sum(marks_to_average) / len(marks_to_average)
        # Print the average formatted to 2 decimal places
        print(f"{average:.2f}")

