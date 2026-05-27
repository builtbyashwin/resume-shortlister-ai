from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


def rank_resumes(job_description, resumes):
    docs = [job_description] + resumes

    vectorizer = TfidfVectorizer(stop_words="english")
    matrix = vectorizer.fit_transform(docs)

    job_vec = matrix[0]
    resume_vecs = matrix[1:]

    scores = cosine_similarity(job_vec, resume_vecs)[0]

    ranked = sorted(
        list(enumerate(scores)),
        key=lambda x: x[1],
        reverse=True
    )

    return ranked
