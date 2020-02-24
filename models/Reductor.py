
# Fake Data to test the reduction
# -------------------------------

# id,   age, gender, weight-kg, timestamp   (gender = man = 1, woman = 2)
mock_person_1 = [123, 27, 1, 70, "2019-01-24"]

# id, exercise, reps, weight-kg, timestamp, performance  (exercise = bench press = 1, squats = 2, mark lifting = 3)
mock_log_1 = [123, 1, 5, 60, "2019-01-25", 6]

# ----------------------------------


# transform mock_person_1 and mock_log_1 to S1 vector of the important variables of both
# [age, gender, personWeigth, exercise, reps, liftedWeight, performance]
def transform():
    transfored_array = [mock_person_1[1], mock_person_1[2], mock_person_1[3],
                         mock_log_1[1], mock_log_1[2], mock_log_1[3], mock_log_1[5]]



# reduct S1 vector to s1 value using pca
def reduct():
    transformed_array = []