#KNN Model
def build_knn_model(user_results):
  X = data.iloc[:, :-1].astype(str)
  y= data.iloc[:,-1:].astype(str)
  knn = KNeighborsClassifier(n_neighbors = 10)
  knn.fit(X,y)
  #new point from user's input
  x_new = np.array([user_results])
  y_predict = knn.predict(x_new)
  return y_predict

predicted_car = build_knn_model(user_results[1])


#Get the final reccomended EV
def recommended_EV(knn_car):
  lst = []
  for i in knn_car:
    car = mapping_car_types_to_cat[mapping_car_types_to_cat['Brand and Model'] == int(i)]['Brand and Model Names'].tolist()

  return car[0]

EV = recommended_EV(predicted_car)


def get_EV_stats(ev_string):
  stats = ElectricCarData[ElectricCarData['Brand and Model'] == ev_string ].squeeze().to_dict()
  return stats

get_EV_stats(EV)
