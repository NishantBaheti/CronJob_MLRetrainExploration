

##########################################################
##### Importing Libraries
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import pickle
import os 
import time


#currWd = os.getcwd()
currWd = '/home/nishant/Desktop/CronJob_MLRetrainExploration'
##########################################################
###### Importing data
df = pd.read_csv("{}/iris.csv".format(currWd))

##########################################################
##### Creating Feature and Target matrix
feature_matrix = df.drop(['variety'],axis=1)
target_matrix = df['variety']

##########################################################
###### Training and Testing Segmentation
x_train,x_test,y_train,y_test = train_test_split(feature_matrix,target_matrix,random_state=42,test_size=0.33)

##### Initiating Model
model = DecisionTreeClassifier()

##### Model Fitting 
model.fit(x_train,y_train)

##### Saving model

pickle.dump(model,open("{}/iris_model".format(currWd),'wb'))

