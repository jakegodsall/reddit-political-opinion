import pytest

from src.utils.text_process import TextProcessor

def test_basic_processing():
    processor = TextProcessor()
    input_text = "Hello"
    expected_output = "hello"
    assert processor._to_lowercase(input_text) == expected_output