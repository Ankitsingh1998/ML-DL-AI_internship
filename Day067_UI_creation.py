#Day067 - UI creation

#Importing the libraries
import pandas as pd
import webbrowser
import dash
import dash_html_components as html

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
       html.H1(children = "Sentiment Analysis with Insights."), #children - argument/attribute of H1 tag    
       html.H2(children = "Data Analysis on ScrappedReviews.")   ,
       html.H3(children = "Statistical Analysis on the data."),
       html.H4(children = "NLP performed on our data."),
       html.H5(children = "Predictions made on reviews."),
       html.H2(children = "Another similar text size."),
       html.H6(children = "All rights are reserved."),
        ] #H1 to H6 --> text size decreases
        )
    return main_layout

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

