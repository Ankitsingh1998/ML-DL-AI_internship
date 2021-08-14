#Day068 - UI creation

#Importing the libraries
import pandas as pd
import webbrowser
import dash
import dash_html_components as html
from dash.dependencies import Input, Output
#favicon - 16X16 image, also known as icon --> favicon.ico --> assets
#favicon.cc --> website to create icons


#Declaring Global variables - variables that can be declared outside the main function
project_name = None
app = dash.Dash()

#Defining My functions
def load_model():
    global ScrappedReviews #declaring df to global so that can be used in main function
    ScrappedReviews = pd.read_csv('ScrappedReviews.csv')

def open_browser():
    webbrowser.open_new("http://127.0.0.1:8050/") #to automatically open the url
    
def create_app_ui():
    main_layout = html.Div(
       [
       html.H1(id='head_title', children = "Sentiment Analysis with Insights."), #children - argument/attribute of H1 tag    
       html.Button(id='review_button', children = "Find Review", n_clicks=0)
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
    Output('review_button', 'children'),
    [
    Input('review_button', 'n_clicks')
    ]
    )

def update_app_ui(n_clicks):
    print("Data Type:", str(type(n_clicks)))
    print("Value:",str(n_clicks))
    
    if n_clicks > 0:
        return 'Someone has clicked the button '+ str(n_clicks)+' times.'
    else:
        return "Sentiment Analysis with Insights."
    
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

