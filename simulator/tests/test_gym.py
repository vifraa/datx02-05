import pytest
import math
from gym import apply_banister, generate_trimp, can_do, load_training


def test_apply_banister(training_list, bench_press):
    '''Give training with known parameters and assert that the resulting
    training adaptations are correct'''
    old_fitness = bench_press.fitness
    old_fatigue = bench_press.fatigue
    trimp = generate_trimp(training_list[0], bench_press.performance)

    apply_banister(training_list, bench_press)

    assert bench_press.fitness == old_fitness * math.exp(-1 / bench_press.fitness_decay) + trimp
    assert bench_press.fatigue == old_fatigue * math.exp(-1 / bench_press.fatigue_decay) + trimp
    assert bench_press.performance == bench_press.fitness * bench_press.fitness_gain \
           - bench_press.fatigue * bench_press.fatigue_gain


def test_generate_trimp(training_list, bench_press):
    '''Test if training load returned by function is correct for known input'''
    trimp = generate_trimp(training_list[0], bench_press.performance)
    ground_truth = training_list[0][0].reps * training_list[0][0].weight / bench_press.performance
    assert trimp == ground_truth


def test_can_do(training_list, bench_press):
    '''Test if training is possible by giving possible training'''
    for training_day in training_list:
        for training_set in training_day:
            assert training_set == can_do(training_set, bench_press)


def test_cant_do(impossible_training_list, bench_press):
    '''Test if training is impossible by giving impossible training'''
    for training_day in impossible_training_list:
        for training_set in training_day:
            assert not training_set == can_do(training_set, bench_press)


def test_load_training():
    '''Test that loading sample training program from csv works as expected'''
    program = load_training("sample_training_program.csv")
    assert program[0].reps == 4
    assert program[0].weight == 1337
