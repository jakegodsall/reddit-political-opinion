import re
import emoji
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

nltk.download("stopwords")
nltk.download("wordnet")

class TextProcessor:
    url_pattern = re.compile(r"https?://\S+")
    hashtag_pattern = re.compile(r"#+")
    repetition_pattern = re.compile(r"([a-zA-Z])\1{2,}")
    punctuation_repetition_pattern = re.compile(r'([^\w\s])\1+')

    def __init__(self):
        """
        Initialize the TextProcessor with NLTK resources.
        """
        self.stopwords = set(stopwords.words("english"))
        self.lemmatizer = WordNetLemmatizer()

    def process(self, text):
        """
        Main method to process text. (To be implemented)

        Args:
            text (str): The text to be processed.

        Returns:
            str: The processed text.
        """
        return text
    
    def _to_lowercase(self, text):
        """
        Convert text to lowercase.

        Args:
            text (str): The text to be converted to lowercase.

        Returns:
            str: The lowercase version of the input text.
        """
        return text.lower()
    
    def _demojize(self, text):
        """
        Convert emojis in the text to their textual representation.

        Args:
            text (str): The text containing emojis to be converted.

        Returns:
            str: The text with emojis converted to their textual description.
        """
        return emoji.demojize(text)
    
    def _replace_url(self, text, default_replace=""):
        """
        Replace URLs in the text with a default string or an empty string.

        Args:
            text (str): The text containing URLs to be replaced.
            default_replace (str, optional): The string to replace URLs with. Defaults to an empty string.

        Returns:
            str: The text with URLs replaced.
        """
        return re.sub(TextProcessor.url_pattern, default_replace, text)
    
    def _replace_hashtag(self, text, default_replace=""):
        """
        Replace hashtags in the text with a default string or an empty string.

        Args:
            text (str): The text containing hashtags to be replaced.
            default_replace (str, optional): The string to replace hashtags with. Defaults to an empty string.

        Returns:
            str: The text with hashtags replaced.
        """
        return re.sub(TextProcessor.hashtag_pattern, default_replace, text)
    
    def _reduce_repetition(self, text, num_retained=2):
        """
        Reduce repetitions of characters in the text to a specified number.

        Args:
            text (str): The text containing character repetitions.
            num_retained (int, optional): Number of character occurrences to retain. Defaults to 2.

        Returns:
            str: The text with character repetitions reduced.
        """
        replace_pattern = ""

        if (num_retained > 0 and int(num_retained) == num_retained):
            replace_pattern += r"\1" * num_retained
        else:
            num_retained = 2


        return re.sub(TextProcessor.repetition_pattern, replace_pattern, text)
    
    def _reduce_punctuation_repetition(self, text, num_retained=1):
        """
        Reduce repetitions of punctuation in the text to a specified number.
        """
        replace_pattern = ""

        if (num_retained > 0 and int(num_retained) == num_retained):
            replace_pattern += r"\1" * num_retained
        else:
            num_retained = 1


        return re.sub(TextProcessor.punctuation_repetition_pattern, replace_pattern, text)