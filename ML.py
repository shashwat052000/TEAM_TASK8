def run_ml_code():
    import numpy as np
    import matplotlib.pyplot as plt
    import pandas as pd

	# Importing the dataset
    dataset = pd.read_csv('Salary_Data.csv')
    X = dataset.iloc[:, :-1].values
    X = X.reshape(-1,1)
    Y = dataset.iloc[:, 1].values # Dependent Variable/Target Values
    Y = Y.reshape (-1,1)

	# Splitting the Dataset into Training Set and Test Set
    from sklearn.model_selection import train_test_split
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 1/3, random_state = 0)
    
    from sklearn.linear_model import LinearRegression
    regressor = LinearRegression()
    regressor.fit(X_train, Y_train)

	# Predicting the Test Set Results
    y_pred = regressor.predict(X_test)
    print("Enter Years Experience")
    rr = regressor.predict([[int(input())]])
    print (rr)
