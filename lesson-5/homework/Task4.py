universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

def enrollment_stats(univ_data):
    return [uni[1] for uni in univ_data], [uni[2] for uni in univ_data]

def mean(student):
    return sum(student) / len(student)

def median(students):
    students.sort()
    return (students[len(students)//2] if len(students) % 2 != 0 else (students[len(students)//2 - 1] + students[len(students)//2]) / 2)

student_counts, tuition_fees = enrollment_stats(universities)

print("*" * 30)
print(f"Total students: {sum(student_counts):,}")
print(f"Total tuition: $ {sum(tuition_fees):,}")
print("")
print(f"Student mean: {mean(student_counts):,.2f}")
print(f"Student median: {median(student_counts):,}")
print("")
print(f"Tuition mean: $ {mean(tuition_fees):,.2f}")
print(f"Tuition median: $ {median(tuition_fees):,}")
print("*" * 30)
