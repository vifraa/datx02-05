
# This script transforms the data of the generated people and
# the logs to a shape that can be used by the regression-models
# ------------------------------------------------------------------------------------
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
class concatenated_data:
    def concatenate(self):
        return 0







# ---------------------------------------------------------------------------------------
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
class detailed_data:
    def detail(self):
        return 0