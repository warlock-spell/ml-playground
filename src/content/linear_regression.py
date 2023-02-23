# @Project:     LearnML
# @Filename:    linear_regression.py.py
# @Author:      Daksh
# @Time:        23-02-2023 03:58 pm

content= """

# Linear Regression

Linear regression is a supervised learning algorithm used to predict a continuous output variable based on one or more input variables. The goal of linear regression is to find the best linear relationship between the input variables (also known as independent variables, predictors or features) and the output variable (also known as dependent variable or target). The linear relationship is modeled using a straight line with equation:

$y = \\beta_0 + \\beta_1 x_1 + \\beta_2 x_2 + \\dots + \\beta_p x_p + \\epsilon$


where:

$y$ is the predicted output variable <br>
$\\beta_0$ is the intercept or bias term, representing the predicted output when all input variables are zero <br>
$\\beta_1, \\beta_2, ..., \\beta_p$ are the coefficients or weights, representing the change in the predicted output for a unit change in the corresponding input variable <br>
$x_1, x_2, ..., x_p$ are the input variables <br>
$\\epsilon$ is the error term or noise, representing the difference between the predicted output and the actual output
The coefficients $\\beta_0, \\beta_1, ..., \\beta_p$ are estimated from the training data using a technique called Ordinary Least Squares (OLS) which minimizes the sum of squared errors between the predicted output and the actual output. Once the coefficients are estimated, the model can be used to predict the output for new input variables.

### Mathematical Formulation
In linear regression, we assume that the relationship between the dependent variable Y and the independent variables X1, X2, ..., Xp is linear. Mathematically, we can express this relationship as:

$Y = \\beta_0 + \\beta_1X_1 + \\beta_2X_2 + \\cdots + \\beta_pX_p + \\epsilon$

where Y is the dependent variable, X1, X2, ..., Xp are the independent variables, $\\beta_0, \\beta_1, \\beta_2, \\cdots, \\beta_p$ are the coefficients that represent the intercept and slopes of the linear relationship, and $\epsilon$ is the error term that represents the random variation in Y that is not explained by the linear relationship with X1, X2, ..., Xp.



### Objective Function
The objective of linear regression is to estimate the values of the coefficients $\\beta_0, \\beta_1, \\beta_2, \\cdots, \\beta_p$ that minimize the sum of squared errors between the predicted values and the actual values of the dependent variable Y. Mathematically, this can be expressed as:

$\min_{\\beta_0, \\beta_1, \\beta_2, \\cdots, \\beta_p} \\sum_{i=1}^{n} (Y_i - (\\beta_0 + \\beta_1X_{i1} + \\beta_2X_{i2} + \\cdots + \\beta_pX_{ip}))^2$\

where n is the number of data points in the training set.

Linear regression can be applied in different settings, including simple linear regression (when there is only one input variable), multiple linear regression (when there are multiple input variables), and polynomial regression (when the relationship between the input variables and the output variable is not linear and can be approximated using a polynomial function).

Overall, linear regression is a powerful and widely used algorithm in the field of machine learning and data science for predictive modeling and inference.

#### Code

The code is written just using numpy, although there are libraries like scikit-learn which can be used to perform linear regression. But when you are learning, it is better to write the code yourself, so that you can understand the inner workings of the algorithm.

```python

import numpy as np


class LinearRegression:
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
```

"""