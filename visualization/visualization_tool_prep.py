import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly
import chart_studio.plotly as cs
import plotly.figure_factory as ff


link = ('https://drive.google.com/file/d/1k-RlY4G2gEMlMk0n5hMQi5lepM9K_cau/view?usp=sharing')
id = link.split("/")[-2]
downloaded = drive.CreateFile({'id':id})
downloaded.GetContentFile('StationsByState.csv')
data = pd.read_csv('StationsByState.csv')
data.head()

data['Electric Total'] = data['Electric stations'] + data['Electric Charging Outlets']

data['code'] = ['State','AL','AK','AZ','AR','CA','CO','CT','DC','DE','FL','GA','HI','ID','IL','IN','IA','KS','KY',
'LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT',
'VT','VA','WA','WV','WI','WY']

data['Total'] = data['Propane Total'] + data['Hydrogen Total'] + data['Electric Total']

totalRow = data.iloc[0]
data = data.iloc[1:]
