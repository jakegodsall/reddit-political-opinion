import string
import re
import emoji
import nltk
import contractions
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, LancasterStemmer, SnowballStemmer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

nltk.download("stopwords")
nltk.download("wordnet")


class TextProcessor:
    retweet_pattern = re.compile(r"RT\s+")
    url_pattern = re.compile(r"https?://\S+")
    hashtag_pattern = re.compile(r"#+")
    repetition_pattern = re.compile(r"([a-zA-Z])\1{2,}")
    punctuation_repetition_pattern = re.compile(r'([^\w\s])\1+')

    def __init__(self):
        ...

    def process(self, text):
        """
        Main method to process text. Applies a series of text normalization
        and tokenization methods sequentially to the input text.

        Args:
            text (str): The text to be processed.

        Returns:
            str: The processed text.
        """
        # Convert text to lowercase
        text = self._to_lowercase(text)

        # Convert emojis to text
        text = self._demojize(text)

        # Replace retweets, URLs, and hashtags
        text = self._replace_retweet(text)
        text = self._replace_url(text)
        text = self._replace_hashtag(text)

        # Reduce character and punctuation repetition
        text = self._reduce_repetition(text)
        text = self._reduce_punctuation_repetition(text)

        # Fix contractions
        text = self._fix_contractions(text)

        # Tokenize the text
        tokens = self._tokenize(text)

        # Remove punctuation from tokens
        tokens = self._remove_punct(tokens)

        # Retain only alphanumeric tokens
        tokens = self._retain_alnum(tokens)

        # Remove stopwords
        tokens = self._remove_stopwords(tokens)

        # Stemming (optional, based on use case)
        # tokens = self._stem(tokens)

        # Reconstruct the processed text from tokens
        return tokens

    def _to_lowercase(self, text):
        """
        Convert text to lowercase.

        Args:
            text (str): The text to be converted to lowercase.

        Returns:
            str: The lowercase version of the input text.
        """
        return str(text).lower()

    def _demojize(self, text):
        """
        Convert emojis in the text to their textual representation.

        Args:
            text (str): The text containing emojis to be converted.

        Returns:
            str: The text with emojis converted to their textual description.
        """
        return emoji.demojize(text)

    def _replace_retweet(self, text, default_replace=""):
        """
        Replace all instances of "RT" with a default value.

        Args:
            text (str): The text containing "RT" to be converted.
            default_replace (str, optional): The string to replace URLs with. Defaults to an empty string.

        Returns:
            str: The text with "RT" replaced.
        """
        return re.sub(TextProcessor.retweet_pattern, default_replace, text)

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

        Args:
            text (str): The text containing punctuation repetitions.
            num_retained (int, optional): Number of punctuation occurrences to retain. Defaults to 1.

        Returns:
            str: The text with punctuation repetitions reduced.

        """
        replace_pattern = ""

        if (num_retained > 0 and int(num_retained) == num_retained):
            replace_pattern += r"\1" * num_retained
        else:
            num_retained = 1

        return re.sub(
            TextProcessor.punctuation_repetition_pattern,
            replace_pattern,
            text)

    def _fix_contractions(self, text):
        """
        Expands contractions found in the input text.
        For example, "don't" is expanded to "do not".

        Args:
            text (str): A string containing English text with contractions.

        Returns:
            str: The input text with contractions expanded.
        """
        return contractions.fix(text)

    def _tokenize(self, text):
        """
        Tokenizes the input text into individual words.

        Args:
            text (str): A string representing a sentence or sentences.

        Returns:
            list[str]: A list of tokens (words) extracted from the input text.
        """
        return word_tokenize(text)

    def _remove_punct(self, token_list):
        """
        Removes punctuation from a list of tokens.

        Args:
            token_list (list[str]): A list of tokens from which punctuation is to be removed.

        Returns:
            list[str]: The token list with punctuation removed.
        """
        return [token for token in token_list if token not in string.punctuation]

    def _retain_alpha(self, token_list):
        """
        Filters the token list to retain only alphabetic tokens.

        Args:
            token_list (list[str]): A list of tokens.

        Returns:
            list[str]: A list containing only tokens that are purely alphabetic.
        """
        return [token for token in token_list if token.isalpha()]

    def _remove_stopwords(self, token_list):
        """
        Removes stopwords from a list of tokens. The method specifically retains the word 'not'
        as it can be significant in sentiment analysis.

        Args:
            token_list (list[str]): A list of tokens from which stopwords are to be removed.

        Returns:
            list[str]: The token list with stopwords removed.
        """
        stops = set(stopwords.words("english"))
        stops.discard("not")
        return [token for token in token_list if token not in stops]

    def _stem(self, tokens, stemmer_type="porter"):
        """
        Stems the tokens in the list using the specified stemming algorithm.

        Args:
            tokens (list[str]): A list of tokens to be stemmed.
            stemmer_type (str, optional): The type of stemmer to use. Options include 'porter', 'lancaster', and 'snowball'. Defaults to 'porter'.

        Returns:
            list[str]: The list of stemmed tokens.

        Raises:
            ValueError: If an invalid 'stemmer_type' is provided.
        """
        if stemmer_type == "porter":
            stemmer = PorterStemmer()
        elif stemmer_type == "lancaster":
            stemmer = LancasterStemmer()
        elif stemmer_type == "snowball":
            stemmer = SnowballStemmer("english")
        else:
            raise ValueError("Invalid 'stemmer_type' provided")

        token_list = []

        for token in tokens:
            token_list.append(stemmer.stem(token))

        return token_list
