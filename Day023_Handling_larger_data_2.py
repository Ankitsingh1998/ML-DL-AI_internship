#Day023 - Handling larger data
import pandas as pd
df_reader = pd.read_json('Clothing_Shoes_and_Jewelry.json', lines=True, chunksize=1000000 )

"""
counter = 1
for chunks in df_reader:
    new_df = pd.DataFrame(chunks[['overall','reviewText','summary']])
    
    new_df1 = new_df[new_df['overall'] == 1].sample(4000)
    new_df2 = new_df[new_df['overall'] == 2].sample(4000)
    new_df3 = new_df[new_df['overall'] == 3].sample(8000)
    new_df4 = new_df[new_df['overall'] == 4].sample(4000)
    new_df5 = new_df[new_df['overall'] == 5].sample(4000)
    
    new_df6 = pd.concat([new_df1, new_df2, new_df3, new_df4, new_df5], axis=0, ignore_index=True)
    new_df6.to_csv(str(counter)+'.csv',index=False) #To skip index column in my dataframe
    counter += 1
"""
#to_csv method used to convert the merged data into csv file

from glob import glob
#glob module is used to retrieve the files or pathnames matching a specified pattern
filenames = glob('*.csv')
#glob('*file_extension') - it will give every file present with that extension in the directory
"""
glob('*.csv') will give:
['1.csv', '10.csv', '11.csv', '12.csv', '13.csv', '14.csv', '15.csv', '16.csv', '17.csv',
 '18.csv', '19.csv', '2.csv', '20.csv', '21.csv', '22.csv', '23.csv', '24.csv', '25.csv',
 '26.csv', '27.csv', '28.csv', '29.csv', '3.csv', '30.csv', '31.csv', '32.csv', '33.csv',
 '4.csv', '5.csv', '6.csv', '7.csv', '8.csv', '9.csv', 'Automobile.csv', 'Baltimore.csv',
 'Salaries.csv', 'titanic.csv']
"""
dataframes = []
i=1
while i<=33:
    dataframes.append(pd.read_csv(str(i)+'.csv'))
    i += 1

final_df = pd.concat(dataframes, axis=0, ignore_index=True)
"""
To finally convert into csv:
final_df.to_csv('Balanced_reviews.csv',index=False)
"""

df = pd.read_csv('Balanced_reviews.csv')
df.shape
df.ndim
df.size
df['reviewText'].head()
df['overall'].value_counts()
df['overall'].min()
df['overall'].max()
df['overall'].mean()
df['overall'].std()
df.isnull()
df.isnull().any(axis=0)
df.fillna('null')

