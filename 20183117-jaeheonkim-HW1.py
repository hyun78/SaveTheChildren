import sklearn
from sklearn.datasets import load_files
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfTransformer
import os
import nltk


def search(dirname):
    filenames = os.listdir(dirname)
    for filename in filenames:
        full_filename = os.path.join(dirname, filename)
        print (full_filename)

def train_nb(training_documents):
    #input : list of string.

    #output. classifier
    return MultinomialNB().fit(training_documents[0],training_documents[1])

    

def classify_nb(classifier_data, document):
    #input : classifier, list of string
    #output : prediction
    global m_vec
    d_counts = m_vec.transform(document)
    d_tfidf = tfidf_trans.transform(d_counts)

    prediction = classifier_data.predict(d_tfidf)
    
    return (document, prediction) 

def pretty_print(result):
    for text, posneg in result:
        print('%s => %s' %(str(text, 'utf-8'), m_train.target_names[posneg]))
    return

def result_print(result):
    res=[]
    for text, posneg in result:
        res.append(m_train.target_names[posneg])
    print(res)
    return

def main():
    train_dir = input("Enter your data directory name (default : txt_sentoken)\n>>")
    m_dir = r'data_final'
    if(train_dir == ""):
        train_dir = m_dir
    global m_train, m_vec, tfidf_trans
    m_train = load_files(train_dir)
    X,x,Y,y = train_test_split(m_train.data,m_train.target,test_size = 0.1)
    #X,Y ==> train
    #x,y ==> test

    m_vec = CountVectorizer(min_df = 1, tokenizer=nltk.word_tokenize)
    train_counts = m_vec.fit_transform(X)
    test_counts = m_vec.transform(x)
    tfidf_trans = TfidfTransformer()
    x_train = tfidf_trans.fit_transform(train_counts)
    x_test = tfidf_trans.transform(test_counts)
    y_train = Y
    y_test = y

    classifier = train_nb((x_train, y_train))

    doc, y_pred = classify_nb(classifier, x)
    result = zip(doc, y_pred)
    #pretty_print(result)
    target_names = m_train.target_names

    report = sklearn.metrics.classification_report(y_test, y_pred, labels=None, target_names=target_names, sample_weight=None, digits=2)
    print(report)
    return

main()
