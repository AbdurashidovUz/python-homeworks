import csv

def read_grades(filename):
    grades = []
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['Grade'] = int(row['Grade'])
            grades.append(row)
    return grades

def calculate_average(grades):
    subject_totals = {}
    subject_counts = {}

    for record in grades:
        subject = record['Subject']
        grade = record['Grade']

        if subject not in subject_totals:
            subject_totals[subject] = 0
            subject_counts[subject] = 0

        subject_totals[subject] += grade
        subject_counts[subject] += 1

    averages = {subject: subject_totals[subject] / subject_counts[subject] for subject in subject_totals}
    return averages


def write_averages(filename, averages):
    with open(filename, mode='w', newline='') as file:
        fieldnames = ['Subject', 'Average Grade']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for subject, avg in averages.items():
            writer.writerow({'Subject': subject, 'Average Grade': round(avg, 1)})

grades = read_grades('grades.csv')
averages = calculate_average(grades)
write_averages('average_grades.csv', averages)
print("Average grades have been written to average_grades.csv")
