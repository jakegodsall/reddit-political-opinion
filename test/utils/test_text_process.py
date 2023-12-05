import pytest

from src.utils.text_process import TextProcessor


@pytest.mark.parametrize("input_text, expected_text", [
    ("Hello", "hello"),
    ("This is A STRING", "this is a string"),
    ("Test324", "test324")
])
def test_lowercasing(input_text, expected_text):
    processor = TextProcessor()
    result = processor._to_lowercase(input_text) == expected_text
    assert result

@pytest.mark.parametrize("input_text, expected_text", [
    ("😀", ":grinning_face:"),
    ("Had a great time at the beach today! 🌊🏖️", "Had a great time at the beach today! :water_wave::beach_with_umbrella:"),
    ("I need to work out more 🏋️‍♂️💪", "I need to work out more :man_lifting_weights::flexed_biceps:")
])  
def test_demojize(input_text, expected_text):
    processor = TextProcessor()
    result = processor._demojize(input_text) == expected_text
    assert result

@pytest.mark.parametrize("input_text, expected_text", [
    ("Check out the latest news on our website: https://www.example.com/news", "Check out the latest news on our website: "),
    ("Learn programming at https://www.code-academy.com", "Learn programming at "),
    ("For support, visit https://support.example.net/help", "For support, visit ")
])
def test_replace_url(input_text, expected_text):
    processor = TextProcessor()
    result = processor._replace_url(input_text, "") == expected_text
    assert result