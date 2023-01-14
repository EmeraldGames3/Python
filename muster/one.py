import csv
from statistics import mean


def one(subject: str) -> float:
    with open('text.txt') as csvfile:
        # Using csv.reader to handle csv file
        reader = csv.reader(csvfile, delimiter=',')

        # Using filter function to get the rows with matching subject
        subject_rows = filter(lambda row: row[2].lower() == subject.lower(), reader)

        # Using list comprehension to get grades from subject_rows
        subject_grades = [float(row[-1]) for row in subject_rows]

        # using statistics.mean function to get the mean of the grades
        return mean(subject_grades) if subject_grades else None


def test_one():
    assert one("Acting 101") == 10

    try:
        assert one("Advanced programming") == 9.0
    except AssertionError:
        print("There has been a violation")
