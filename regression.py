#required libraries; run command on cmd
#pip install numpy pandas scikit-learn
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

f = pd.read_csv("https://raw.githubusercontent.com/curfewUnZipper/HousePriceRegression/main/data.csv")
head = list(f.columns)

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
