import filecmp
from generator import generate_individuals, gender_to_string, save_individuals


def gender_ratio_calc(individuals):
    """
    Helper function to get gender_ratio from a list of individuals
    """
    __tracebackhide__ = True
    n_male = 0
    for i in individuals:
        if i.gender == 0:
            n_male += 1
    return n_male/len(individuals)


def test_gender_to_string():
    """Tests the gender_to_string() method of generator"""
    assert gender_to_string(1) == "female"
    assert gender_to_string(0) == "male"


def test_generate_individuals():
    """Tests if generated individuals are of the same length and gender_ratio, have not yet figured
    out how to test the variance and mean"""
    num = 10
    age_mean = 25
    age_variance = 2
    bench_press_fitness_mean = 100
    bench_press_fitness_variance = 5
    gender_ratio = 0.5
    weight_mean = 70
    weight_variance = 5
    generated_individuals = generate_individuals(num, age_mean, age_variance, 
                                                 weight_mean, weight_variance,
                                                 bench_press_fitness_mean, bench_press_fitness_variance,
                                                 gender_ratio)

    assert len(generated_individuals) == num
    assert gender_ratio == gender_ratio_calc(generated_individuals)


def test_save_individuals(tmpdir, individual):
    """
    Tests the save_individuals method of generator module. Saves a file and compares it to a
    manually created file to check if they are the same.
    """
    path = tmpdir.mkdir("sub").join("test_individuals.csv")
    individuals = [individual, individual]  # use two individuals
    save_individuals(individuals, path)
    assert filecmp.cmp(path, "tests/sample_individuals.csv")
