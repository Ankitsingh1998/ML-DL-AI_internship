#Day029 : Code challenge IGN Analysis
import pandas as pd
df = pd.read_csv('ign.csv')
df.columns

#Games with score more than 7 and released on xbox one platform
xbox_one_filtered = (df["score"] > 7) & (df["platform"] == "Xbox One")
filtered_reviews = df[xbox_one_filtered]
xbox_one_games = filtered_reviews['title']
print (xbox_one_games)

#xbox review ditribution
xbox_one = df[df['platform']=="Xbox One"]
xbox_reviews = xbox_one['score_phrase']
xbox_reviews.hist(bins=20, grid=False, xrot=90)

#playstation4 review distribution
ps4 = df[df['platform']=='PlayStation 4']
ps4_reviews = ps4['score_phrase']
ps4_reviews.hist(bins=20, grid=False, xrot=90, yrot=0)
#xrot and yrot for rotation of xlabels and ylabels
#grid=True will plot the graph with grids or vice-versa

