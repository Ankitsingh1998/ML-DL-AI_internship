#Day054 - pickle loading and prediction using CountVectorizer
#reload the model
import pickle

def check_review(textdata):
    file = open('pickle_lgr_model.pkl', 'rb')

    recreated_model = pickle.load(file)
    
    #load the vocabulary
    vocab_file = pickle.load(open('features.pkl', 'rb'))
    
    from sklearn.feature_extraction.text import CountVectorizer
    recreated_vec = CountVectorizer(decode_error = 'replace', vocabulary = vocab_file)
    
    from sklearn.feature_extraction.text import TfidfTransformer
    tf_trans = TfidfTransformer()
    
    return recreated_model.predict(tf_trans.fit_transform(recreated_vec.fit_transform([textdata])))



review = check_review('I loved that product very much but disliked a bit too.')

if review == 1:
    print('The text is a positive review.')
else:
    print('The text is a negative review.')

