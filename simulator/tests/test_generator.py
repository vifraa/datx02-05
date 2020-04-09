"""Unit tests for the generator module"""
import datetime
import filecmp
from generator import generate_individuals, gender_to_string, save_individuals


def gender_ratio_calc(individuals):
    """
    Helper function to get gender_ratio from a list of individuals
    """
    n_male = 0
    for i in individuals:
        if i.gender == 0:
            n_male += 1
    return n_male/len(individuals)


def test_gender_to_string():
    """Tests the gender_to_string() method of generator"""
    assert gender_to_string(1) == "female"
    assert gender_to_string(0) == "male"
    assert gender_ratio == gender_ratio_calc(generated_individuals)


def test_save_individuals(tmpdir, individual):
    """
    Tests the save_individuals method of generator module. Saves a file and compares it to a
    manually created file to check if they are the same.
    """
    path = tmpdir.mkdir("sub").join("test_individuals.csv")
    individuals = [individual, individual]  # use two individuals
    save_individuals(individuals, path, None)

    with open(path) as file, open("tests/sample_individuals.csv") as file2:
        while True:
            a = file.read(1)
            b = file2.read(1)
            print(a, b)
            if a is not b:
                print("FAIL:", a, b)
            if not a or not b:
                break
    assert filecmp.cmp(path, "tests/sample_individuals.csv")
