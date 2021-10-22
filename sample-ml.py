import numpy as np
from sklearn.linear_model import LinearRegression

X = np.asarray([[1.1,1.23], [2.2,1.34], [5.6,3.2], [1.6,4.3], [1.9,3.2], [3.4,2.1]])
y = [2.1, 1.4, 1.2, 1.5, 1.7, 2.3]

reg = LinearRegression()
reg = reg.fit(X, y)

X_new = [[1, 1.2]]
y_new = reg.predict(X_new)
print(f"Predicted value for {X_new} is {y_new}")