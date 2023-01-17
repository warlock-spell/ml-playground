# @Project:     LearnML
# @Filename:    svm.py
# @Author:      Daksh
# @Time:        03-01-2023 08:48 pm

import numpy as np


class SVM:

    def __init__(self, lr: float = 0.001, n_iters: int = 1000, lambda_parameter: float = 0.01) -> None:
        self.w = None
        self.b = None
        self.lr = lr
        self.n_iters = n_iters
        self.lambda_parameter = lambda_parameter

    def fit(self, train, train_labels):
        # Make sure that the labels are -1 & +1 instead of 0 and +1
        # To do this we will use np.where and replace all the value less than equal to 0 to -1
        train_labels_updated = np.where(train_labels <= 0, -1, 1)
        # train is a nd array, where
        # number of rows = number of samples
        # number of cols = number of features
        n_samples, n_features = train.shape
        # initialize weights and bias
        self.w = np.zeros(n_features)
        self.b = 0

        # Gradient Descent
        for _ in range(self.n_iters):
            for index, x_i in enumerate(train):
                condition = train_labels_updated[index] * (np.dot(x_i, self.w) - self.b) >= 1
                if condition:
                    self.w -= self.lr * (2 * self.lambda_parameter * self.w)
                else:
                    self.w -= self.lr * (2 * self.lambda_parameter * self.w - np.dot(x_i, train_labels_updated[index]))
                    self.b -= self.lr * train_labels_updated[index]

    def predict(self, test):
        linear_output = np.dot(test, self.w) - self.b
        return np.sign(linear_output)
