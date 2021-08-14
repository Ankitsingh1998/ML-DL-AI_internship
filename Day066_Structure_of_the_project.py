#Day066 - Structure of the project

#Importing the libraries
import pandas as pd

#Declaring Global variables - variables that can be declared outside the main function
project_name = None

#Defining My functions
def load_model():
    global ScrappedReviews #declaring df to global so that can be used in main function
    ScrappedReviews = pd.read_csv('ScrappedReviews.csv')

#Main function to control the flow of your project
def main():
    print('Start of my project')
    
    load_model()
    global ScrappedReviews
    global project_name #not necessary since it's already a global variable by default
    
    project_name = "Sentiment Analysis with Insights"
    print('My project name is:', project_name)
    
    print('My Scrapped data is:',ScrappedReviews.sample(5))
    
    print('End of my project')
    
    project_name = None #At the end of the project set the global variable to null
    ScrappedReviews = None

#Calling the Main function
if __name__ == '__main__':
    main()

