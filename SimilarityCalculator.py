import ExtractTextFromFiles
from Models import TF_IDF
from Models import Doc2Vec
from Models import CountVectorizer
import os

def process_doc2_vec_process(req_document, resume_docs):
    req_doc_text = ExtractTextFromFiles.getTxtContentAsString(req_document)
    resumesText = []
    for doc in resume_docs:
        resumesText.append(ExtractTextFromFiles.getPDFContentAsString(doc))
    return Doc2Vec.get_doc2vec_similarity(req_doc_text,resumesText)

def process_doc2vec_textract(req_document, resume_docs):
    req_doc_text = ExtractTextFromFiles.getTxtContentAsString(req_document)
    resumesText = []
    for doc in resume_docs:
        resumesText.append(ExtractTextFromFiles.getPDFContentAsString(doc))
    return Doc2Vec.get_doc2vec_similarity(req_doc_text, resumesText)


def getSimilarityScore(req_document, resume_docs):
    jDText = ExtractTextFromFiles.getTxtContentAsString(req_document)
    resumesText = []
    for doc in resume_docs:
        resumesText.append(ExtractTextFromFiles.getPDFContentAsString(doc))

    cos_sim_list = CountVectorizer.get_cosine_similarity(jDText, resumesText)
    final_doc_rating_list = []
    zipped_docs = zip(cos_sim_list,resume_docs)
    sorted_doc_list = sorted(zipped_docs, key = lambda x: x[0], reverse=True)
    for element in sorted_doc_list:
        doc_rating_list = []
        doc_rating_list.append(os.path.basename(element[1]))
        doc_rating_list.append("{:.0%}".format(element[0]))
        final_doc_rating_list.append(doc_rating_list)
    return final_doc_rating_list
    

