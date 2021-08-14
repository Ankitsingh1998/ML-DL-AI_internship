#Day025 - Code challenge bitly
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
json_df = pd.read_json('bitly.json', lines=True)
#json - javascript object notation

#replacing nan with missing and ' ' with Unknown
json_df.isnull().any(axis=0)
json_df = json_df.replace([np.nan,'Missing'],[' ','Unknown'])

#Top 10 most frequent time zones
json_df_tz = json_df['tz'].value_counts().head(10)

#Number of occurence of each time zone
json_count_tz = json_df['tz'].value_counts()

#Bar plot to show frequency distribution for different time zones
json_df_tz.plot(kind='bar')
plt.xlabel('time zones')
plt.ylabel('counts')
plt.suptitle('frequency for top 10 time zones')

#Seperating browser capability
tokens_df = json_df['a'].str.split(n=1, expand=True).add_prefix('Token_')

#Browser capability count
tokens_frequency = tokens_df['Token_0'].value_counts()

#Bar plot to show frequency distribution for different browsers
tokens_frequency.head(10).plot.bar()
plt.xlabel('operating system')
plt.ylabel('frequency')
plt.suptitle('frequency distriubution of different os')

#Seperating windows and non-windows OS's
tokens_df = tokens_df.replace(np.nan,'Missing')

tokens_df['os'] = 'Windows'
tokens_df["os"][tokens_df["Token_1"].str.find("Windows") != 1] = "Not Windows"
