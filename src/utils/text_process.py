import re
import emoji
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

nltk.download("stopwords")
nltk.download("wordnet")

class TextProcessor:

    url_pattern = re.compile("(http|https):\/\/\S+")
    hashtag_pattern = re.compile("#+")

    def __init__(self):
        self.stopwords = set(stopwords.words("english"))
        self.lemmatizer = WordNetLemmatizer()

    def process(self, text):

        return text
    
    def _to_lowercase(self, text):
        return text.lower()
    
    def _demojize(self, text):
        return emoji.demojize(text)
    
    def _replace_url(self, text, default_replace=""):
        return re.sub(TextProcessor.url_pattern, default_replace, text)
    
    def _replace_hashtag(self, text, default_replace=""):
        return re.sub(TextProcessor.hashtag_pattern, default_replace, text)
    
    