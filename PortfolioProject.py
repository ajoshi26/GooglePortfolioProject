import numpy as np
import pandas as pd 
import seaborn as sb
import datetime as dt



data = pd.read_csv(r'C:\Users\Adity\OneDrive\Documents\Data_Analyst_Project\Fitabase Data\dailyActivity_merged.csv',encoding='utf-8')

print(data)

#Looking into the data types and general overview of the dataframe
data.info()
print(data.head(10))

#Checking for any null values 
print(data.isnull())

#Removing some of the unnecessary columns
data = data.drop('TrackerDistance',axis=1)
print(data.head(10))


#Reformatting the header columns
new_columns = []
def cleaning(string):
    
    string = string.replace("ActivityDate", "date_of_activity")
    string = string.replace("TotalSteps", "num_of_steps")
    string = string.replace("TotalDistance", "total_distance_in_miles")
   
    string = ''.join(['_'+i.lower() if i.isupper() 
                      else i for i in string]).lstrip('_') 

    return string

for columns in data:
    clean_columns = cleaning(columns)
    new_columns.append(clean_columns) 
    
data.columns = new_columns

#Creating a new column for the total amount of active minutes
data['total_active_minutes'] = data['very_active_minutes'] + data['fairly_active_minutes'] + data['lightly_active_minutes']


#Converting the date_of_activity column into a date type
data['date_of_activity'] = pd.to_datetime(data['date_of_activity'])
#data.info()

#Converting id column into a string
data['id'] = data['id'].astype(str)
data.info()

#Summary Stats of the dataset
print(data.describe())
print(data['logged_activities_distance'].describe())


#Correlation between active minutes and calories burned
sb.scatterplot(data=data, x="total_active_minutes", y="calories")







