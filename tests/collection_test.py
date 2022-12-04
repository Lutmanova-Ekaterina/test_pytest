from pytest_code.collection import set_
import pytest

def test_set_():
    assert set_({"a": {"b": {"c": 3}}}, ["a", "b", "c"], 4) == {"a": {"b": {"c": 3}}}
    assert set_({"a": {"b": {"c": 3}}}, [], 1000) == {"a": {"b": {"c": 3}}}

def test2_set_():
    assert set_({}, [1, 2, 3, 4, 5], 1000) == {1: {2: {3: {4: {5: 1000}}}}}
    assert set_({"a": {"b": {"c": 3}}}, ["a", "b", "C", "d"], "") == {"a": {"b": {"c": {"d": ""}}}}