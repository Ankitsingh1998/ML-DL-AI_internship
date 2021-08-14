#Day054 - pickle loading and prediction using TfidfVectorizer
#reload the model
import pickle

def check_review(textdata):
    file = open('pickle_lgr_model.pkl', 'rb')

    recreated_model = pickle.load(file)
    
    #load the vocabulary
    vocab_file = pickle.load(open('features.pkl', 'rb'))
    
    from sklearn.feature_extraction.text import TfidfVectorizer
    recreated_vec = TfidfVectorizer(min_df = 5, decode_error = 'replace', vocabulary = vocab_file, analyzer='word', stop_words='english')
    
    return recreated_model.predict(recreated_vec.fit_transform([textdata]))



review = check_review('I loved that product very much but disliked a bit too.')


if review == 1:
    print('The text is a positive review.')
else:
    print('The text is a negative review.')



