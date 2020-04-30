import pandas as pd,numpy as np
ann=pd.read_csv("C:\\Users\\memon\\Documents\\python\\DeepLearning\\ann\\Churn_Modelling.csv")
X=ann.iloc[:,3:13].values
y=ann.iloc[:,[13]].values
from sklearn.preprocessing import LabelEncoder,OneHotEncoder,StandardScaler
labelencode_X2=LabelEncoder()
X[:,2]=labelencode_X1.fit_transform(X[:,2])
from sklearn.compose import ColumnTransformer
ct=ColumnTransformer([('encoder',OneHotEncoder(),[1])],remainder='passthrough')
X=ct.fit_transform(X)
X=X[:,1:]
sc_X=StandardScaler()
X=sc_X.fit_transform(X)

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=0)
from keras.models import Sequential
from keras.layers import Dense
classifier=Sequential()