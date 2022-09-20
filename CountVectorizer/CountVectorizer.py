class CountVectorizer:
    """Convert a collection of text documents to a matrix of token counts."""

    def __init__(self, lowercase=True):
        """dict_for_features is dict with feature-keys and zero-values.
        It is a little memory-overhead, but since we are on Python, we don't care."""
        self.lowercase = lowercase
        self.dict_for_features = {}

    def fit_transform(self, corpus):
        """Transform a corpus of documents to a document-term matrix."""
        if self.lowercase:
            corpus = [doc.lower() for doc in corpus]

        self.dict_for_features = {keyword: 0 for keyword in ' '.join(corpus).split(' ')}
        matrix = []

        for doc in corpus:
            doc_feature_fq = self.dict_for_features.copy()
            for word in doc.split():
                doc_feature_fq[word] += 1
            matrix.append(list(doc_feature_fq.values()))

        return matrix

    def get_feature_names(self):
        """Function returns list of features."""
        return list(self.dict_for_features.keys())
