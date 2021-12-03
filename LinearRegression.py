import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import datasets
import matplotlib.pyplot as plt


class LinearRegression():
    def __init__(self, lr=0.01, n_iters=1000):
        self.lr = lr
        self.n_iters = n_iters
        self.weights = None
        self.bias = None
    def fit(self, X, y):
        # Implement the gradinet descent
        # Init parameters
        n_sample, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0
        for _ in range(self.n_iters):
            y_predicted = np.dot(X, self.weights) + self.bias
            dw = (1/n_sample) * np.dot(X.T, (y_predicted - y))
            db = (1/n_sample) * np.sum(y_predicted - y)

            self.weights -= self.lr * dw
            self.bias -= self.lr * db


    def predict(self,x):
        y_predicted = np.dot(x, self.weights) + self.bias
        return y_predicted



X, y = datasets.make_regression(n_samples=100, n_features=1, noise=20, random_state=4)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1234)


regressor = LinearRegression()
regressor.fit(X_train,y_train)
y_predicted = regressor.predict(X_test)

# Cost Function = Mean Squared error --> Diff between actual Y and preducted Y
mse_values = np.mean( (y_test - y_predicted)**2)

print(mse_values)

y_pred_line = regressor.predict(X)
cmap = plt.get_cmap('viridis')
fig = plt.figure(figsize=(8,6))
m1 = plt.scatter(X_train, y_train, color=cmap(0.9), s=10 )
m2 = plt.scatter(X_test, y_test, color=cmap(0.5), s=10)
plt.plot(X, y_pred_line, color='black', linewidth=2, label="Prediction")
plt.show()

