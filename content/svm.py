# @Project:     LearnML
# @Filename:    svm.py
# @Author:      Daksh
# @Time:        23-02-2023 04:27 pm

content = """
# Support Vector Machines (SVM)
Support Vector Machines (SVM) is a popular supervised learning algorithm used for classification and regression analysis. It can be used for both linear and nonlinear data classification by finding an optimal hyperplane that separates the data into different classes.

### Linear SVM
A linear SVM tries to find the best hyperplane that separates the data points into different classes. The equation for a hyperplane in a p-dimensional space is given by:

$\\beta_0 + \\beta_1 x_1 + \\beta_2 x_2 + ... + \\beta_p x_p = 0$

where $x_1, x_2, ..., x_p$ are the independent variables and $\\beta_0, \\beta_1, \\beta_2, ..., \\beta_p$ are the coefficients that determine the orientation and position of the hyperplane.

The decision boundary of the SVM is defined as the hyperplane that maximizes the margin between the classes. The margin is defined as the distance between the hyperplane and the closest data points from each class.

The SVM optimization problem for a linearly separable dataset is formulated as:

$$\\text{Minimize } \\frac{1}{2} ||\\beta||^2$$

$$\\text{Subject to } y_i(\\beta_0 + \\beta_1 x_{i1} + \\beta_2 x_{i2} + ... + \\beta_p x_{ip}) \geq 1, \\text{ for all } i = 1,2,...,n$$

where $y_i$ is the class label of the i-th data point, $x_{ij}$ is the j-th feature of the i-th data point, and $n$ is the number of data points. The objective function minimizes the norm of the coefficient vector $\\beta$ subject to the constraint that all data points are classified correctly with a margin of at least 1.

### Nonlinear SVM
When the data is not linearly separable, the SVM can use a kernel function to map the data to a higher-dimensional space where it is linearly separable. The kernel function calculates the similarity between two data points and transforms the data to a higher-dimensional space based on that similarity.

The SVM optimization problem for a non-linearly separable dataset is formulated as:

$$\\text{Minimize } \\frac{1}{2} ||\\beta||^2 + C\sum_{i=1}^{n}\\xi_i$$

$$\\text{Subject to } y_i(\\beta_0 + \\beta_1 K(x_i,x_1) + \\beta_2 K(x_i,x_2) + ... + \\beta_p K(x_i,x_p)) \geq 1-\\xi_i, \\text{ for all } i = 1,2,...,n$$

where $\\xi_i$ is the slack variable that allows some data points to be misclassified, $C$ is the regularization parameter that controls the trade-off between maximizing the margin and minimizing the misclassification, and $K(x_i,x_j)$ is the kernel function that calculates the similarity between the i-th and j-th data points.

#### Popular kernel functions include:

Linear kernel: $K(x_i,x_j) = x_i^Tx_j$ <br>
Polynomial kernel: $K(x_i,x_j) = (x_i^Tx_j + c)^d$ <br>
Radial basis function (RBF) kernel: $K(x_i,x_j) = e^{-\\gamma ||x_i-x_j||^2}$ <br>
SVM is a powerful algorithm that can handle complex classification and regression problems. However, it requires careful selection of hyperparameters and can be sensitive to the choice

#### Code

The code is written just using numpy, although there are libraries like scikit-learn which can be used to perform svm. But when you are learning, it is better to write the code yourself, so that you can understand the inner workings of the algorithm.

```python
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
```
"""