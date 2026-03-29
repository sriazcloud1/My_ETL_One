#!/usr/bin/env python
# coding: utf-8

get_ipython().system('pip install requests')


import requests
import os
import pandas as pd
from datetime import datetime



#loading data
url = "https://api.open-meteo.com/v1/forecast?latitude=40.71&longitude=-74.00&current_weather=true"
response =  requests.get(url)


# In[22]:


data = response.json()
print (data)



#finding the usage data
working_df=data['current_weather']
working_df


# 2.clening data
time_stamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
temp_fahrenheit = (working_df['temperature'] * 9/5 ) + 32
temp_fahrenheit
#time_stamp
final_df=pd.DataFrame([{ 'time stamp' : time_stamp, 'temp_fahrenheit': temp_fahrenheit,
                         'windspeed': working_df['windspeed'], 'weathercode' : working_df['weathercode']
                       }])
final_df




# 3. LOAD: Save to a CSV file
## = 'data/weather_history.csv'
file_path='C:\\Users\\srisr\\Data_Science_Practice\\My_ETL_One\\data\\weather_history.csv'


#if file exist append or create new file.
#print (dir(os.path.isfile))
if os.path.isfile(file_path):
   final_df.to_csv(file_path,mode='a',index=False,header=False)
else:
   final_df.to_csv(file_path, index=False)

print (f"***********ETL completed for recroding of temperature: {working_df['temperature']}  ************")




