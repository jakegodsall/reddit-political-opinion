from gensim.test.utils import common_texts
from gensim.models import Word2Vec

class TextVectorizer:
    def __init__(self):
        ...

    def word2vec_text(self, text, size=100, window=5, min_count=1, workers=4):
        model = Word2Vec(
            common_texts,
            vector_size=size, 
            window=window, 
            min_count=min_count, 
            workers=workers
            )
        
        return model.train(text, total_examples=1, epochs=1)

    def glove_text(self, text):
        ...

    def fasttext_text(self, text):
        ...

    def elmo_text(self, text):
        ...


    def train_word2vec(self, text, vector_size=100, window=5, min_count=1, workers=4):
        model = Word2Vec(
            vector_size=vector_size,
            window=window,
            min_count=min_count,
            workers=workers
        )


        model.build_vocab(text, progress_per=1000)

    

    
if __name__ == "__main__":
    vectorizer = TextVectorizer()
    trained = vectorizer.word2vec_text(["hello", "world"])
    print(trained)