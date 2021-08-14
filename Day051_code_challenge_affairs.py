#Day051 - code challenge affairs
import numpy as np
import pandas as pd

df = pd.read_csv('affairs.csv')
df.columns

percentage_women_having_affairs = df['affair'].value_counts(normalize=True)
print('percentage of women having affairs is: '+str((percentage_women_having_affairs[1].round(4))*100)+'%')

features = df.iloc[:,:-1].values
labels = df.iloc[:,-1].values

def my_model(features, labels):
    from sklearn.preprocessing import OneHotEncoder
    from sklearn.compose import ColumnTransformer
    ct = ColumnTransformer([('encoder', OneHotEncoder(), [6,7])], remainder='passthrough')
    features = ct.fit_transform(features)
    
    col_to_ohe =[6,7]
    tot_col, indexes = 0, []
    for col in col_to_ohe:
        unique_val_count = len(df.iloc[:,col].value_counts())
        tot_col += unique_val_count
        indexes.append(tot_col - unique_val_count)   
        
    features = np.delete(features, indexes, axis=1)
    
    from sklearn.model_selection import train_test_split
    features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.3, random_state=0)
    
    from sklearn.linear_model import LogisticRegression
    lg_rg = LogisticRegression(random_state=0, max_iter=1000)
    lg_rg.fit(features_train, labels_train)
    
    prediction = lg_rg.predict(features_test)
    
    from sklearn.metrics import confusion_matrix
    con_mat = confusion_matrix(labels_test, prediction)
    
    lg_rg_score = lg_rg.score(features_test, labels_test)
    
    # Preprocessing the new individual's data
    """
     She's a 25-year-old teacher who graduated college, 
     has been married for 3 years, 
     has 1 child, 
     rates herself as strongly religious, 
     rates her marriage as fair, 
     and her husband is a farmer.        
    """
    data = np.array([3, 25, 3, 1, 4, 16, 4, 2]).reshape(1, -1)
    data = ct.transform(data)
    data = np.delete(data, indexes, axis=1)
    data_prediction = lg_rg.predict_proba(data)
    
    return prediction, con_mat, lg_rg_score, data_prediction

pred, cm, score, val_pred = my_model(features,labels)

print ("model accuracy by using the confusion matrix : "+str(cm))
print ("model accuracy using .score() function : "+str(round(score*100,2)))
print ("percentage of total women actually had an affair : "+str(round(df["affair"].mean()*100,2))+"%")
print ("probability of an affair for a random woman is : "+str(val_pred))

