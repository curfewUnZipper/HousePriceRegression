#required libraries; run command on cmd
#pip install numpy pandas matplotlib scikit-learn
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#from sklearn import preprocessing, svm
#from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression 

#mounting drive, used when in google colab
#from google.colab import drive
#drive.mount('/drive')

import csv

# Opeing csv and storing data
f = open('data.csv', 'r') #change the path
csvreader = csv.reader(f)
headings = [] 
rows = [] 
headings=next(csvreader)
for r in csvreader:
    rows.append(r)

#trial to see if loaded data is correct
pd.DataFrame(rows,columns=headings)[0:9] 


#Linear Regression

#x-axis - area (sq. ft.)
x = np.array(f[head[4]]).reshape(-1,1)
#print(x)

#y-axis
y= np.array(f[head[1]])
#print(y)


#model
model = LinearRegression().fit(x,y)
print(model.score(x,y))

a= int(input("Enter Area of house in sqft (Example: 3000) -> "))
print(f"The price would be around: ${round(float(model.predict(np.array(a).reshape(-1,1))),2):,}")
