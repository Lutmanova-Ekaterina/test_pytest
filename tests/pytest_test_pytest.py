from pytest_code.pytest_test import get_val
import pytest

def test_get_val():
    assert get_val({"hello": "world"}, "hello", "python") == "python"
    assert get_val({"hello": "world"}, "hello") == "world"

def test2_get_val():
    assert get_val({}, "hello", "python") == "python"
    assert get_val({}, "", "python") == "python"
    assert get_val({}, "", "") == ""

def test3_get_val():
    assert get_val({False: "world"}, False) == "python"
    assert get_val({"hello": "world"}, "hello", False) == False