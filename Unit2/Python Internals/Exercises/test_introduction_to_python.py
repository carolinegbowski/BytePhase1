import pytest
import introduction_to_python as answers

def test_question_1_lower():
    assert answers.range()[0] == -5

def test_question_1_upper():
    assert answers.range()[1] == 256
