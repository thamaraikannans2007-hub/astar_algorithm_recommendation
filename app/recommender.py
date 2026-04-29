import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

class MovieRecommender:
    def __init__(self, path):
        self.df = pd.read_csv(path)

        self.df['Genre'] = self.df['Genre'].fillna('')
        self.df['combined'] = self.df['Genre']

        self.vectorizer = CountVectorizer()
        self.matrix = self.vectorizer.fit_transform(self.df['combined'])

        self.similarity = cosine_similarity(self.matrix)

    def get_index(self, title):
        result = self.df[self.df['Series_Title'].str.lower() == title.lower()]
        return result.index[0] if not result.empty else None

    def recommend(self, title, top_n=10):
        idx = self.get_index(title)
        if idx is None:
            return []

        scores = list(enumerate(self.similarity[idx]))
        scores = sorted(scores, key=lambda x: x[1], reverse=True)[1:top_n+1]

        results = []
        for i, score in scores:
            results.append({
                "title": self.df.iloc[i]['Series_Title'],
                "rating": self.df.iloc[i]['IMDB_Rating'],
                "poster": self.df.iloc[i]['Poster_Link'],
                "score": float(score)
            })
        return results