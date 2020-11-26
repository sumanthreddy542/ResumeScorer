from sklearn.metrics.pairwise import cosine_similarity
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords as stp
from sklearn.feature_extraction.text import CountVectorizer
from TextPreProcessing import cv_lemmetizer as cv_lemma


def get_binay_cosine_similarity(compare_doc,doc_corpus):
    count_vect = CountVectorizer(binary=True,analyzer=cv_lemma.stemmed_words)
    cv_req_vector = count_vect.fit_transform([compare_doc]).todense()
    cv_resume_vector = count_vect.transform(doc_corpus).todense()

    cosine_similarity_list = []
    for i in range(len(cv_resume_vector)):
        cosine_similarity_list.append(cosine_similarity(cv_req_vector,cv_resume_vector[i])[0][0])
    return cosine_similarity_list

def get_cosine_similarity(compare_doc,doc_corpus):
    count_vect = CountVectorizer( analyzer=cv_lemma.stemmed_words)
    cv_req_vector = count_vect.fit_transform([compare_doc]).todense()
    cv_resume_vector = count_vect.transform(doc_corpus).todense()

    cosine_similarity_list = []
    for i in range(len(cv_resume_vector)):
        cosine_similarity_list.append(cosine_similarity(cv_req_vector,cv_resume_vector[i])[0][0])
    return cosine_similarity_list


