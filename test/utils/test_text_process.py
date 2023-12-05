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

@pytest.mark.parametrize("input_text, expected_text", [
    ("This is a tweet! #HASHTAG #tweet", "This is a tweet! HASHTAG tweet"),
    ("I just love #coffee in the morning. Best start to the day!", "I just love coffee in the morning. Best start to the day!"),
    ("Stunning sunset at the beach #Nature #Beautiful", "Stunning sunset at the beach Nature Beautiful")
])
def test_replace_hashtag(input_text, expected_text):
    processor = TextProcessor()
    result = processor._replace_hashtag(input_text) == expected_text
    assert result


@pytest.mark.parametrize("input_text, expected_text", [
    ("Testingggggggg", "Testing"),
    ("Helloooooo", "Hello"),
    ("Yessssss!!!", "Yes!!!"),
    ("Whaaaaaat???", "What???")
])
def test_reduce_repetition_1(input_text, expected_text):
    processor = TextProcessor()
    result = processor._reduce_repetition(input_text, 1) == expected_text
    assert result, f"Result of the test {processor._reduce_repetition(input_text, 1)}"

@pytest.mark.parametrize("input_text, expected_text", [
    ("Testingggggggg", "Testingg"),
    ("Helloooooo", "Helloo"),
    ("Yessssss!!!", "Yess!!!"),
    ("Whaaaaaat???", "Whaat???")
])
def test_reduce_repetition_2(input_text, expected_text):
    processor = TextProcessor()
    result = processor._reduce_repetition(input_text, 2) == expected_text
    assert result, f"Result of the test {processor._reduce_repetition(input_text, 1)}"

@pytest.mark.parametrize("input_text, expected_text", [
    ("Testingggggggg", "Testinggg"),
    ("Helloooooo", "Hellooo"),
    ("Yessssss!!!", "Yesss!!!"),
    ("Whaaaaaat???", "Whaaat???")
])
def test_reduce_repetition_3(input_text, expected_text):
    processor = TextProcessor()
    result = processor._reduce_repetition(input_text, 3) == expected_text
    assert result, f"Result of the test {processor._reduce_repetition(input_text, 1)}"