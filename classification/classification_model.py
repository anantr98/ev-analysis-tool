#KNN Model
import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neighbors import NearestNeighbors
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn import svm



def build_knn_model(user_results):
    #data = pd.read_csv('model_data.csv', index_col = False)
    data = pd.read_csv('data/model_data.csv', index_col = 0)
    #.drop(['unnamed 0'],axis=1)
    X = data.iloc[:, :-1].astype(str)
    y= data.iloc[:,-1:].astype(str).squeeze()
    knn = KNeighborsClassifier(n_neighbors = 10)
    knn.fit(X,y)
    #new point from user's input
    x_new = np.array([user_results])
    y_predict = knn.predict(x_new)
    return y_predict

#predicted_car = build_knn_model(user_results[1])


#Get the final reccomended EV
def recommended_EV(knn_car):
    brand_model = pd.read_csv('data/brand_model_df.csv')
    for i in knn_car:
        car = brand_model[brand_model['Brand and Model'] == int(i)]['Brand and Model Names'].tolist()
    return car[0]
    #return car[0]

#EV = recommended_EV(predicted_car)


def get_EV_stats(ev_string):
    ElectricCarData = pd.read_csv("data/EV_car_data.csv")
    stats = ElectricCarData[ElectricCarData['Brand and Model'] == ev_string ].squeeze().tolist()
    #.to_dict()
    return stats

#get_EV_stats(EV)
