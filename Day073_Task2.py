#Day073 - UI creation

#Importing the libraries
import pickle #to load pickle models
import pandas as pd #to raed stored data
import webbrowser
import dash #python web framework
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer

app = dash.Dash(external_stylesheets=[dbc.themes.CYBORG]) #BOOTSTRAP/CYBORG
project_name = "Sentiment Analysis with Insights"

def open_browser():
    webbrowser.open_new("http://127.0.0.1:8050/") #to directly open the url after the code executed

def load_model(): #loading the saved model and passing the scrappedReviews
    global pickle_model
    global vocab
    global scrappedReviews

    scrappedReviews = pd.read_csv('ScrappedReviews.csv')

    file = open("pickle_lgr_model.pkl", 'rb') #to looad the saved model
    pickle_model = pickle.load(file)

    file2 = open("features.pkl", 'rb')  #features - to load vocabs
    vocab = pickle.load(file2)
        
def check_review(reviewText):
    transformer = TfidfTransformer()
    loaded_vec = CountVectorizer(decode_error="replace", vocabulary=vocab)
    reviewText = transformer.fit_transform(loaded_vec.fit_transform([reviewText])) #fitting the review in Tfidfvectorizer in 1D array format
    return pickle_model.predict(reviewText) #review prediction

def create_app_ui():
    global project_name
    main_layout = dbc.Container(
        dbc.Jumbotron(
                [
                    html.H1(id = 'heading', children = project_name, className = 'display-3 mb-4'),
                    dbc.Textarea(id = 'textarea', className="mb-3", placeholder="Search your Review here:", value = 'I loved these shoes but the quality is not as expected.', style = {'height': '100px'}), #https://dash-bootstrap-components.opensource.faculty.ai/docs/components/input/
                    dbc.Container([ #https://dash-bootstrap-components.opensource.faculty.ai/docs/components/layout/
                        dcc.Dropdown( #https://dash.plotly.com/dash-core-components
                    id='dropdown',
                    placeholder = 'Select a Review',
                    options=[{'label': i[:500] + "...", 'value': i} for i in scrappedReviews.reviews],
                    value = scrappedReviews.reviews[0],
                    style = {'margin-bottom': '20px'}
                    
                )
                       ],
                        style = {'padding-left': '40px', 'padding-right': '40px'}
                        ),
                    dbc.Button("Submit", color="info", className="mt-2 mb-3", id = 'button', style = {'width': '80px'}),
                    html.Div(id = 'result'),
                    html.Div(id = 'result1')
                    ],
                className = 'text-center'
                ),
        className = 'mt-4'
        )
    
    return main_layout

@app.callback(
    Output('result', 'children'),
    [
    Input('button', 'n_clicks')
    ],
    [
    State('textarea', 'value')
    ]
    )    
def update_app_ui(n_clicks, textarea):
    result_list = check_review(textarea)
    
    if (result_list[0] == 0 ):
        return dbc.Alert("Negative review", color="danger")
    elif (result_list[0] == 1 ):
        return dbc.Alert("Positive review", color="success")
    else:
        return dbc.Alert("Unknown", color="dark")

@app.callback(
    Output('result1', 'children'),
    [
    Input('button', 'n_clicks')
    ],
    [
     State('dropdown', 'value')
     ]
    )
def update_dropdown(n_clicks, value):
    result_list = check_review(value)
    
    if (result_list[0] == 0 ):
        return dbc.Alert("Negative review", color="danger")
    elif (result_list[0] == 1 ):
        return dbc.Alert("Positive review", color="success")
    else:
        return dbc.Alert("Unknown", color="dark")
    
def main():
    global app
    global project_name
    load_model()
    open_browser()
    
    app.layout = create_app_ui()
    app.title = project_name
    app.run_server()
    
    app = None
    project_name = None
if __name__ == '__main__':
    main()
