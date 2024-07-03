import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder 
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import GridSearchCV, KFold
import pickle

data = pd.read_csv('data/clean_data.csv') 
label_encoder = LabelEncoder()
data['sectorName'] = label_encoder.fit_transform(data['sectorName'])
data['stateDescription']= label_encoder.fit_transform(data['stateDescription'])
data.drop(['customers','revenue','sales'],axis=1,inplace= True)
filenamepre = r'C:\Users\shanu\Desktop\vertisystem\U.S.ElectricityPrices\artifacts\preprocessor.pkl'
pickle.dump(data, open(filenamepre, 'wb'))   
X = data.drop(['price'],axis=1)
y=data['price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
param_grid = {
    'n_estimators': [50, 100, 150, 200, 250]  # Adjust this range as needed
}
rf = RandomForestRegressor(random_state=42)
cv = KFold(n_splits=5, shuffle=True, random_state=42)  # 5-fold cross-validation
grid_search = GridSearchCV(estimator=rf, param_grid=param_grid, cv=cv, scoring='neg_mean_squared_error', n_jobs=-1)
grid_search.fit(X, y)

best_n_estimators = grid_search.best_params_['n_estimators']

best_rf = RandomForestRegressor(n_estimators=100, random_state=42)
best_rf.fit(X, y)
filename = r'C:\Users\shanu\Desktop\vertisystem\U.S.ElectricityPrices\artifacts\model.pkl'
pickle.dump(best_rf, open(filename, 'wb'))                     
y_pred = best_rf.predict(X)

mse = mean_squared_error(y, y_pred)
print("Best number of estimators:", best_n_estimators)
print("Mean Squared Error (MSE):", mse)