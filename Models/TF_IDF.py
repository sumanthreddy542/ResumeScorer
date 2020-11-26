from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords as stp
from TextPreProcessing import tf_idf_lemmetizer as tf_idf_lemma

def get_tf_idf_cosine_similarity(compare_doc, doc_corpus):
    tf_idf_vect = TfidfVectorizer(analyzer='word', ngram_range=(1, 1))
    
    tf_idf_req_vector = tf_idf_vect.fit_transform([compare_doc]).todense()
    tf_idf_resume_vector = tf_idf_vect.transform(doc_corpus).todense()

    cosine_similarity_list = []
    for i in range(len(tf_idf_resume_vector)):
        cosine_similarity_list.append(cosine_similarity(tf_idf_req_vector, tf_idf_resume_vector[i])[0][0])
    return cosine_similarity_list

def get_tf_cosine_similarity(compare_doc, doc_corpus):
    tf_idf_vect = TfidfVectorizer(use_idf=False, analyzer='word', ngram_range=(1, 1))
    
    tf_idf_req_vector = tf_idf_vect.fit_transform([compare_doc]).todense()
    tf_idf_resume_vector = tf_idf_vect.transform(doc_corpus).todense()

    cosine_similarity_list = []
    for i in range(len(tf_idf_resume_vector)):
        cosine_similarity_list.append(cosine_similarity(tf_idf_req_vector, tf_idf_resume_vector[i])[0][0])
    return cosine_similarity_list


