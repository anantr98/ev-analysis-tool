import pandas as pd
import numpy as np

# reading EVByStates.csv into a dataframe
link = ('https://drive.google.com/file/d/1enkQ7eiccRdUJBlAtscsCMIKn3ZoGuVY/view?usp=sharing')
id = link.split("/")[-2]
downloaded = drive.CreateFile({'id':id})
downloaded.GetContentFile('EVByStates.csv')
EVByStates = pd.read_csv('EVByStates.csv')
EVByStates = EVByStates.rename(columns = {'Make':'Brand'})
EVByStates['Brand and Model'] = EVByStates['Brand'] + " " + EVByStates['Model']


# reading ElectricCarData.csv into a dataframe
link = ('https://drive.google.com/file/d/1puhH2VGibbts9nk9Maze2wnVbyCtmpRS/view?usp=sharing')
id = link.split("/")[-2]
downloaded = drive.CreateFile({'id':id})
downloaded.GetContentFile('ElectricCarData.csv')
ElectricCarData = pd.read_csv('ElectricCarData.csv')
ElectricCarData['Brand and Model'] = ElectricCarData['Brand']+ ElectricCarData['Model']

# Converting km to miles and Euros to Dollars
ElectricCarData['TopSpeed_mph'] = ElectricCarData['TopSpeed_KmH']*0.621371
ElectricCarData['Range_Mi'] = ElectricCarData['Range_Km']*0.621371
ElectricCarData['PriceUS'] = ElectricCarData['PriceEuro']*1.2

ElectricCarData['TopSpeed_mph'] = round(ElectricCarData['TopSpeed_mph'],0)
ElectricCarData['Range_Mi'] = round(ElectricCarData['Range_Mi'],0)
ElectricCarData['PriceUS'] = round(ElectricCarData['PriceUS'],0)

#Remove NAN values and unnecessary columns
drop_lst = list(missing_value_df[missing_value_df['percent_missing'] == 100.0]['column_name'])
ElectricCarData = ElectricCarData.drop(drop_lst, axis = 1)
ElectricCarData = ElectricCarData.drop(['TopSpeed_KmH','Range_Km','PriceEuro'],axis = 1)


# Creating a copy of ElectricCarData so we can modify it
df = ElectricCarData.copy()

# Custom Binary Encoding for RapidCharge Column
df["RapidCharge"] = np.where(df["RapidCharge"].str.contains('Yes'), 1, 0)

# Custom Encodings for driving range and budget range columns
def driving_range(num):
  if ((num >= 50 and num <=250) or num == '50-250'):
    return 0
  if (num >250 and num <=450 or num == '250-450'):
    return 1
  if (num > 450 and num <=650 or num == '450-650'):
    return 2

def budget_range(num):
  if (num >= 0 and num <=50000):
    return int(0)
  if (num >50000 and num <=100000):
    return int(1)
  if (num > 100000 and num <=150000):
    return int(2)
  if (num > 150000 and num <=200000):
    return int(3)
  if (num > 200000 and num <=250000):
    return int(4)
  if (num > 300000 and num <=350000):
    return int(5)

df['Range_Mi'] = df['Range_Mi'].apply(lambda x: driving_range(x))
df['PriceUS'] = df['PriceUS'].apply(lambda x: budget_range(x))

# Creating a Brand and Model categorical column to use for classification
# selecting the features that will be used in the model
data = df[['Seats','RapidCharge','Range_Mi','PriceUS','Brand and Model']]
data["Brand and Model Names"] = data["Brand and Model"]
data["Brand and Model"] = data["Brand and Model"].astype('category')
data["Brand and Model"] = data["Brand and Model"].cat.codes
mapping_car_types_to_cat = data[["Brand and Model Names","Brand and Model"]]
data = data.drop(51)
data = data[['Seats','RapidCharge','Range_Mi','PriceUS','Brand and Model']]


# Encodings- converting user input to categories
def new_dict_driving(user_string):
  if(user_string == '50-250'):
    return 0
  elif(user_string == '250-450'):
    return 1
  elif(user_string == '450-650'):
    return 2

def new_dict_budget(user_string):
  if(user_string == '0-50000'):
    return 0
  elif(user_string == '50000-100000'):
    return 1
  elif(user_string == '100000-150000'):
    return 2
  elif(user_string == '150000-200000'):
    return 3
  elif(user_string == '200000-250000'):
    return 4
  elif(user_string == '300000-350000'):
    return 5

def new_dict_rapidcharge(string):
  if string == 'Yes' or 'yes' or 'YES':
    return 1
  elif string == 'No' or 'no' or 'NO':
    return 0
