from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from gensim.summarization import summarize
from gensim.parsing.preprocessing import remove_stopwords
from rake_nltk import Rake

def preprocessTokenizeText(text):
    summarizedText = summarize(text, ratio = 0.5)
    filteredSentence = remove_stopwords(summarizedText)
    r = Rake()
    r.extract_keywords_from_text(filteredSentence)
    phrases = r.get_ranked_phrases()
    tokenizedPhrases = ""
    for phrase in phrases:
        tokenizedPhrases += phrase + " "
    return tokenizedPhrases