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
"""