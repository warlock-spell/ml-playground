# @Project:     LearnML
# @Filename:    linear_regression.py.py
# @Author:      Daksh
# @Time:        09-12-2022 04:05 pm

import numpy as np


class LinearRegression:
    """
        A class to create a linear regression model.

        ...

        Attributes
        ----------
        lr : float
            learning rate for algorithm
        n_iters : int
            number of iterations

        Methods
        -------
        fit(train, train_labels):
            fits the training data to the model.

        predict(test):
            predicts output on test data.
        """
    def __init__(self, lr: float = 0.001, n_iters: int = 1000) -> None:
        self.lr = lr
        self.n_iters = n_iters
        self.weights = None
        self.bias = None

    def fit(self, train, train_labels):
        # initialize parameters
        n_samples, n_features = train.shape
        self.weights = np.zeros(n_features)
        self.bias = 0

        for _ in range(self.n_iters):
            y_predicted = np.dot(train, self.weights) + self.bias

            dw = (1 / n_samples) * np.dot(train.T, (y_predicted - train_labels))
            db = (1 / n_samples) * np.sum(y_predicted - train_labels)

            self.weights -= self.lr * dw
            self.bias -= self.lr * db

    def predict(self, test):
        y_predicted = np.dot(test, self.weights) + self.bias
        return y_predicted
