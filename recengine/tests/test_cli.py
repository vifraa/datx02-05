import pytest
import os
import click
from click.testing import CliRunner
from cli import pbar, ttr
from hypothesis import given
from hypothesis.strategies import floats, integers, sampled_from, booleans

def test_pbar_works_isolated():
    """
    Test to ensure that the pbar cli command works in
    isolated filesystems.
    """
    runner = CliRunner()
    with runner.isolated_filesystem():
        res = runner.invoke(pbar, ["--age", 18, "--weight", 80,
                                   "--performance", 60, "--sex", "MAN", "-h"])
        res = runner.invoke(pbar, ["--age", 18, "--weight", 80,
                                   "--performance", 60, "--sex", "MAN"])

        assert res.exit_code == 0


@pytest.mark.parametrize("cli_input, expected", [
    (["--age", "18", "--weight", "80.5", "--performance", "60.5", "--sex", "MAN", "-h"], 0),
    (["--age", "18", "--weight", "80.5", "--performance", "60.5", "--sex", "MAN"], 0),
    (["--age", "18", "--weight", "80.5", "--performance", "60.5", "--sex", "WOMAN", "-h"], 0),
    (["--age", "18", "--weight", "80.5", "--performance", "60.5", "--sex", "OTHER", "-h"], 0),
    (["--age", "18", "--weight", "80.5", "--performance", "60.5", "--sex", "WILLNOTWORK"], 2),
    (["--age", "18", "--weight", "80.5", "--performance", "60.5", "--sex", "WILLNOTWORK", "-h"], 2),
    (["--age", "18.2", "--weight", "80.5", "--performance", "60.5", "--sex", "MAN", "-h"], 2),
    (["--age", "18", "--weight", "80", "--performance", "60", "--sex", "MAN", "-h"], 0)
])
def test_pbar_ensures_correct_types(cli_input, expected):
    """
    Tests to ensure that the input to the pbar cli command forces
    correct types.
    """
    runner = CliRunner()

    res = runner.invoke(pbar, cli_input)
    assert res.exit_code == expected


@given(integers(min_value=0), floats(min_value=0, allow_infinity=False),
       floats(min_value=0, allow_infinity=False),
       sampled_from(["MAN", "WOMAN", "OTHER"]), booleans())
def test_pbar(age, weight, performance, sex, hide):
    """
    Tests the pbar cli command with different generated values to ensure stability
    in large range of inputs.
    """
    runner = CliRunner()

    if hide:
        res = runner.invoke(pbar, ["--age", age, "--weight",
                                   weight, "--performance", performance, "--sex", sex, "-h"])
    else:
        res = runner.invoke(pbar, ["--age", age, "--weight",
                                   weight, "--performance", performance, "--sex", sex])


    assert res.exit_code == 0

@given(integers(min_value=0, max_value=7), booleans())
def test_ttr(weeks, hide):
    """
    Tests that the ttr command finishes with expected input.
    """
    logs_path = os.path.join(os.path.dirname(__file__), "training_logs", "test.csv")

    runner = CliRunner()

    cli_input = ["--file", logs_path, "--weeks", weeks,
                                  "--timeformat", "%m/%d/%Y %H:%M", "-h"]
    if hide:
        cli_input.append("-h")

    res = runner.invoke(ttr, cli_input)

    assert res.exit_code == 0
