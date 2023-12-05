import pytest

from src.utils.text_process import TextProcessor

def test_basic_processing():
    processor = TextProcessor()
    input_text = "Hello"
    expected_output = "Hello"
    assert processor.process(input_text) == expected_output