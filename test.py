import pytest
from main import add

def test_empty_string_returns_zero():
    assert add("") == 0
def test_single_number_returns_value():
    assert add("1") == 1

def test_two_numbers_comma_separated():
    assert add("1,5") == 6

def test_multiple_numbers_comma_separated():
    assert add("1,2,3,4,5") == 15

def test_numbers_separated_by_newlines():
    assert add("1\n2,3") == 6

def test_custom_delimiter():
    assert add("//;\n1;2") == 3