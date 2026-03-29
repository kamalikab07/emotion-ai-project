from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC

def create_pipeline() -> Pipeline:
    return Pipeline([
        ("tfidf", TfidfVectorizer(
            max_features=10000,
            ngram_range=(1, 2),     # unigrams + bigrams = better accuracy
            stop_words="english"
        )),
        ("clf", LinearSVC(max_iter=1000))
    ])