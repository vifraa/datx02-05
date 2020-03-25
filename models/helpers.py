from datetime import date, datetime

def print_mean_squared_error(value):
    print('Mean squared error: %.2f' % value)

def print_coefficient_of_determination(value):
    """The coefficient of determination: 1 is perfect prediction"""
    print('Coefficient of determination: %.2f' % value)

def calculate_age(date_string):
    """
    Calcululates the age of someone with the birtday of the inputted
    date string.

    Date string should be formatted 'yyyy-mm-dd' i.e '2020-02-30'

    :param date_string: Birthday in string representation.
    """
    birth_date = datetime.strptime(date_string, "%Y-%m-%d")
    today = datetime.now()

    age = today.year - birth_date.year - ((today.month, today.day) <
                                          (birth_date.month, birth_date.day))
    return age
