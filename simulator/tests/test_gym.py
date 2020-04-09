"""Unit tests for the gym module"""

import math
from gym import apply_banister, generate_trimp, can_do, load_training


def test_apply_banister(training_dataframe, bench_press):
    """Give training with known parameters and assert that the resulting
    training adaptations are correct"""
    old_fitness = bench_press.fitness
    old_fatigue = bench_press.fatigue
    trimp = generate_trimp(
        training_dataframe.iloc[0, :], bench_press.get_current_performance())

    apply_banister(training_dataframe, bench_press)

    assert bench_press.fitness == old_fitness * \
        math.exp(-1 / bench_press.fitness_decay) + trimp
    assert bench_press.fatigue == old_fatigue * \
        math.exp(-1 / bench_press.fatigue_decay) + trimp
    assert bench_press.get_current_performance() == bench_press.basic_performance + \
           bench_press.fitness * bench_press.fitness_gain \
           - bench_press.fatigue * bench_press.fatigue_gain


def test_generate_trimp(training_dataframe, bench_press):
    """Test if training load returned by function is correct for known input"""
    training_set = training_dataframe.iloc[0, :]
    trimp = generate_trimp(training_set, bench_press.get_current_performance())
    ground_truth = training_set["Reps"] * \
        training_set["Weight"] / bench_press.get_current_performance()
    assert trimp == ground_truth


def test_can_do(training_dataframe, bench_press):
    """Test if training is possible by giving possible training"""
    for _, training_set in training_dataframe.iterrows():
        assert training_set["Reps"] == can_do(
            training_set, bench_press)["Reps"]


def test_cant_do(impossible_training_dataframe, bench_press):
    """Test if training is impossible by giving impossible training"""
    for _, training_set in impossible_training_dataframe.iterrows():
        assert not training_set["Reps"] == can_do(
            training_set, bench_press)["Reps"]


def test_load_training(individual):
    """Test that loading sample training program from csv works as expected"""
    program_dataframe = load_training("tests/sample_training_program.csv", individual.bench_press_movement)
    assert program_dataframe.iloc[0, :]["Reps"] == 4
    assert program_dataframe.iloc[0, :]["Weight"] == 300*0.75


