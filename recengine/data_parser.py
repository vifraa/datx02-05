"""
This module is responsible of having helper function revolving around parsing data.
"""
import csv
from collections import defaultdict
from datetime import datetime
from io import StringIO
import pandas as pd

def split_into_weeks(sets, time_format):
    """
    Splits the given array containing sets into a dictionary
    containing keys of weeks with the values of the sets done in that
    week.

    The sets should be a dict with keys:
    {
        'exercise',
        'weight',
        'repetitions',
        'timestamp'
    }

    :param sets: The given sets.
    :param time_format: The timeformat used for the timestamp in each set.
    """
    weeks = defaultdict(list)

    for t_set in sets:
        week = datetime.strptime(t_set.get('timestamp'), time_format).isocalendar()[1]
        weeks[str(week)].append(t_set)

    return weeks

def calculate_1rm(weight, reps):
    """
    Calculates the 1RM from given weight and repetitions.
    Calculations are made using the Epley formula.

    :param weight: The weight of the set.
    :param reps: The repetitions of the set.
    """
    return weight * (1 + (reps / 30.0))


def calculate_ttrdata_from_week_dict(weeks):
    """
    Calcualtes the ttr data from a given dictionary.

    :param weeks: Dictionary containing lists of sets done in a week.
    """
    ttr = []

    for week in sorted(weeks.keys()):
        sets = weeks.get(week)

        week_tonnage = 0
        week_1rm = 0
        for t_set in sets:
            weight = float(t_set.get('weight'))
            reps = int(t_set.get('repetitions'))

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

    rows = [
        {
            'exercise': row[0],
            'weight': row[1],
            'repetitions': row[2],
            'timestamp': row[3]
        }
        for row in csv_reader]

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


def ttrdata_from_csv_population_4_weeks(logs_path):
    """
    Wrapper function for ttrdata_from_csv meant for files directly outputted from the simulator.

    File has to be of type CSV and follow the structure of:
    ID | Exercise | Weight | Reps | Timestamp | Performance

    :param logs_path: The path to the CSV file from the simulator containing the training logs.

    :returns: Dataframe consisting of the TTR data during the last 4 weeks with the associated
    individual's ID
    """
    logs = pd.read_csv(logs_path, sep="|")

    # Calculate TTR_DATA based on pre-logs.
    ttr_data = {}
    for p_id, group in logs.groupby('ID'):
        group = group.drop(columns=['ID'])

        # Saving to buffer to be able to use with data parsers directly.
        buffer = StringIO()  # creating an empty buffer
        group.to_csv(buffer, index=False)  # filling that buffer
        buffer.seek(0)  # set to the start of the stream

        data = ttr_data_from_reader(csv.reader(buffer), '%Y-%m-%d %H:%M:%S')
        ttr_data[str(p_id)] = data

    headers = ["load_week1", "max_week1", "load_week2", "max_week2", "load_week3", "max_week3",
               "load_week4", "max_week4"]

    data = pd.DataFrame(columns=headers)

    # Transform data
    for p_id, ttr in ttr_data.items():

        # Take last 4 weeks.
        entry = ttr[-8:]

        data = data.append(pd.Series(entry, index=data.columns), ignore_index=True)

    return data


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

