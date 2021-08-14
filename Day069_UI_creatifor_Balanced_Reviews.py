#Day069 - UI creation for Balanced Reviews

#Importing the libraries
import pickle
import pandas as pd
import webbrowser
import dash
import dash_html_components as html
import dash_core_components as dcc #https://dash.plotly.com/dash-core-components
import dash_bootstrap_components as dbc #https://dash-bootstrap-components.opensource.faculty.ai/docs/components/button/
from dash.dependencies import Input, Output, State
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer

#favicon - 16X16 image, also known as icon --> favicon.ico --> assets
#favicon.cc --> website to create icons


#Declaring Global variables - variables that can be declared outside the main function
project_name = None
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

#Defining My functions
def load_model():
    global ScrappedReviews #declaring df to global so that can be used in main function
    ScrappedReviews = pd.read_csv('ScrappedReviews.csv')
    
    global pickle_model
    pickle_file = open("pickle_lgr_model.pkl", 'rb')
    pickle_model = pickle.load(pickle_file)
    
    global vocab
    feature_file = open("features.pkl", 'rb')
    vocab = pickle.load(feature_file)

def check_review(reviewText):
    #reviewText has to be vectorised, that vectorizer is not saved yet
    #load the vectorize and call transform and then pass that to model predictor
    #load it later
    
    transformer = TfidfTransformer()
    loaded_vec = CountVectorizer(decode_error="replace",vocabulary=vocab)
    vectorised_review = transformer.fit_transform(loaded_vec.fit_transform([reviewText]))

    # Add code to test the sentiment of using both the model
    # 0 == negative   1 == positive

    return pickle_model.predict(vectorised_review)

def open_browser():
    webbrowser.open_new("http://127.0.0.1:8050/") #to automatically open the url
    
def create_app_ui():
    main_layout = html.Div(
       [
       html.H1(id='head_title', children = "Sentiment Analysis with Insights."), #children - argument/attribute of H1 tag    

    dcc.Textarea(
        id = 'textarea_review',
        placeholder = 'Enter your review here.....',
        style = {'width':'100%', 'height':100}
        ),
    
    dbc.Button(  
        children = 'Find Review',
        id = 'review_button',
        color = 'info',
        style= {'width':'100%', 'height':40},
        active=True,
        ), #*args - disabled=True,outline=True,n_clicks=0
    
    html.H1(children = None, id='result')
    
    ]    
    )
    
    return main_layout
    
"""
Event Handling - when someone clicks the button call my method update_app_ui
wiring concept

Object    Event   function
Button    Click   update_app_ui()

Decorators and callbacks mechanisms is a way to  implement wiring in python
Input == arguments to your callback
Output == return of your callback

"""

@app.callback(
    Output('result', 'children'),
    [
    Input('review_button', 'n_clicks')
    ],
    [
    State('textarea_review', 'value')]
    )

def update_app_ui(n_clicks, textarea_value):
    
    print("Data Type:", str(type(n_clicks)))
    print("Value:",str(n_clicks))
    
    print("Data Type = ", str(type(textarea_value)))
    print("Value = ", str(textarea_value))


    if (n_clicks > 0):

        response = check_review(textarea_value)
        if (response[0] == 0):
            result = 'This review is negative.'
        elif (response[0] == 1 ):
            result = 'This review is positive.'
        else:
            result = 'No test data is provided.'

        return result
        
    else:
        return ""
    
#Main function to control the flow of your project
def main():
    print('Start of my project')
    
    load_model()
    open_browser()
    
    global ScrappedReviews
    global project_name #not necessary since it's already a global variable by default
    global app
    
    project_name = "Sentiment Analysis with Insights"
    #print('My project name is:', project_name)   
    #print('My Scrapped data is:',ScrappedReviews.sample(5))
    
    app.title = project_name
    app.layout = create_app_ui() 
    app.run_server() #to make the application - blocking statement
    
    print('End of my project')
    
    project_name = None #At the end of the project set the global variable to null
    ScrappedReviews = None
    app = None

#Calling the Main function
if __name__ == '__main__':
    main()


