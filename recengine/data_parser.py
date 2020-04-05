"""
This module is responsible of having helper function revolving around parsing data.
"""
import csv
from collections import defaultdict
from datetime import datetime

def split_into_weeks(rows, time_format):
    """
    Splits the given two array containing sets into a dictionary
    containing keys of weeks with the values of the sets done in that
    week.

    :param rows: The given sets.
    :param time_format: The timeformat used for the timestamp in each set.
    """
    weeks = defaultdict(list)
    
    for row in rows:
        week = datetime.strptime(row[3], time_format).isocalendar()[1]
        weeks[str(week)].append(row)

    return weeks

def calculate_1rm(weight, reps):
    """
    Calculates the 1RM from given weight and repetitions.
    Calculations are made using the Epley formula.

    :param weight: The weight of the set.
    :param reps: The repetitions of the set.
    """
    if reps == 1:
        return weight

    return weight * (1 + (reps / 30.0))


def calculate_ttrdata_from_week_dict(weeks):
    """
    Calcualtes the ttr data from a given dictionary.

    :param weeks: Dictionary containing lists of sets done in a week.
    """
    ttr = []

    for week in sorted(weeks.keys()):
        rows = weeks.get(week)

        week_tonnage = 0
        week_1rm = 0
        for row in rows:
            weight = float(row[1])
            reps = int(row[2])

            one_rep_max = calculate_1rm(weight, reps)
            if one_rep_max > week_1rm:
                week_1rm = one_rep_max

            week_tonnage += (reps * weight)

        ttr.append(week_tonnage)
        ttr.append(week_1rm)

    return ttr

def ttr_data_from_reader(csv_reader, time_format, contains_header=True):
    """
    Creates the ttr data format based on the given csv reader.
    """
    if contains_header:
        _headers = next(csv_reader)

    rows = [row for row in csv_reader]

    weeks = split_into_weeks(rows, time_format)
    ttr = calculate_ttrdata_from_week_dict(weeks)
    return ttr


def ttrdata_from_csv(file_path, time_format, contains_header=True):
    """
    Creates the ttr data format based on the data found in the given file path.

    File has to be of type CSV and follow the structure of:
    Exercice | Weight | Reps | Timestamp

    :param file_path: The path to the CSV file.
    :param time_format: The string format of the Timestamp.
    :param contains_header: If the given CSV file contain a header row.
    """

    with open(file_path, newline='') as file:
        csv_reader = csv.reader(file, delimiter="|")
        return ttr_data_from_reader(csv_reader, time_format, contains_header=True)


def ttrdata_from_csv_bytes(f_bytes, time_format, contains_header=True):
    """
    Creates the ttr data format based on the data found in the given bytes.

    File has to be of type CSV and follow the structure of:
    Exercice | Weight | Reps | Timestamp

    :param f_bytes: The csv file in bytes.
    :param time_format: The string format of the Timestamp.
    :param contains_header: If the given CSV file contain a header row.
    """
    csv_reader = csv.reader(f_bytes, delimiter="|")
    return ttr_data_from_reader(csv_reader, time_format, contains_header=True)

