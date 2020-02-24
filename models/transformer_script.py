
# This script transforms the data of the generated people and
# the logs to a shape that can be used by the regression-models
# ------------------------------------------------------------------------------------

# loads people data from individuals.csv and logs data from training.csv
# and offer several utility methods.
class data_loader:

    people = []
    logs = []


    def __init__(self, people_csv, log_csv):
        return 0

    def load_people_data(self):
        return 0

    def get_90_log_data_for_person(self, id):
        return 0

    def get_all_log_data_for_person(self, id):
        return 0

    def get_all_log_data_for_all(self):
        return 0








# ---------------------------------------------------------------------------------------

# transform the data of the people, the logs and the final performance to one array in the following form
# [reps1, weight1, reps2, weight2, ..... , reps90, weight90, age, gender, person's_weight, performance]
# for 90 logs, its size is 2 * 90 + 3 + 1 = 184
class concatenated_data:
    def concatenate(self):
        return 0







# ---------------------------------------------------------------------------------------

# transform the data of the people and the logs to one array where each log data is squashed
# with the same personal data, using PCA and dimensional reduction so per1 (R) log1 = s1
# [s1, s2, s3, ..... , s90, performance] (the array is concatenated with performance)
# for 90 logs, its size is 90 + 1 = 91
class squashed_data:

    # Fake Data to test the reduction
    # id, age, gender, weight-kg, timestamp   (gender = man = 1, woman = 2)
    mock_person_1 = [123, 27, 1, 70, "2019-01-24"]

    # id, exercise, reps, weight-kg, timestamp, performance  (exercise = bench press = 1, squats = 2, mark lifting = 3)
    mock_log_1 = [123, 1, 5, 60, "2019-01-25", 6]

    def squash(self):
        return 0

    # transform mock_person_1 and mock_log_1 to S1 vector of the important variables of both
    def transform(self):
        transfored_array = [self.mock_person_1[0], self.mock_person_1[1], self.mock_person_1[2], self.mock_person_1[3],
                            self.mock_log_1[1], self.mock_log_1[2], self.mock_log_1[3], self.mock_log_1[5]]

    # reduct S1 vector to s1 value using pca
    def reduct(self):
        return 0







# ---------------------------------------------------------------------------------------

# transform the data of the people and the logs to one array where regarding to the order of the log
# everything is concatenated in the following form
# [5*3, 5*5, 5*8, 5*12, 5*15, ...... , 300*3, 300*5, 300*8, 300*12, 300*15   ,age, gender, person's_weight, performance]
# where 5 is the first possible lifted-weight that a person can have lifted, and 3,5,8,12,15 is the possible reps
# the values of this array will be the count of times that a person in his/her log have done this training
# for example [0, 1, 0, 0, 4, ...... , 0, 0, 0, 0, 0,  32, 1, 73, 56.9]
# Its size is fixed to 290 * 5 + 3 + 1 = 1454
class detailed_data:
    def detail(self):
        return 0