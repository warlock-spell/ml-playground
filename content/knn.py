# @Project:     LearnML
# @Filename:    knn.py
# @Author:      Daksh
# @Time:        23-02-2023 04:35 pm

content= """
# K-Nearest Neighbors (KNN)
K-Nearest Neighbors (KNN) is a supervised learning algorithm used for classification and regression analysis. The goal of KNN is to classify an unlabeled data point based on the class of its K nearest neighbors in the training data.

### Algorithm
The KNN algorithm can be summarized in the following steps:

1. Determine the value of K.
2. Calculate the distance between the new data point and each data point in the training set.
3. Select the K-nearest data points based on their distance to the new data point.
4. Assign the new data point to the class that is most common among the K-nearest neighbors.

### Mathematical formulation
Let's consider a set of $n$ data points $X = {x_1, x_2, ..., x_n}$ where each data point has $p$ features $x_{i} = (x_{i1}, x_{i2}, ..., x_{ip})$. Also, let's consider a target variable $Y$ which can take one of the $K$ classes.

In KNN, the prediction of the target variable $Y$ for a new observation $x_{new}$ is given by:

$\\hat{Y}{new} = mode(Y{k1}, Y_{k2}, ..., Y_{kK})$

where $Y_{k1}, Y_{k2}, ..., Y_{kK}$ are the target variables of the $K$ nearest neighbors of $x_{new}$.

To calculate the distance between two data points, several distance metrics can be used. Euclidean distance is the most common distance metric and is given by:

$D(x_i, x_j) = \\sqrt{(x_{i1}-x_{j1})^2 + (x_{i2}-x_{j2})^2 + ... + (x_{ip}-x_{jp})^2}$

Alternatively, Manhattan distance can also be used and is given by:

$D(x_i, x_j) = |x_{i1}-x_{j1}| + |x_{i2}-x_{j2}| + ... + |x_{ip}-x_{jp}|$

#### Hyperparameters
The value of K is a hyperparameter in KNN. A small value of K can lead to overfitting, while a large value of K can lead to underfitting. Therefore, the value of K should be chosen carefully based on the problem and the data.

#### Advantages and disadvantages
KNN is a simple and intuitive algorithm that does not require any assumptions about the underlying data distribution. However, the algorithm can be computationally expensive, especially when the size of the training data is large. Additionally, the performance of the algorithm can be sensitive to the value of K and the distance metric used.

#### Code

The code is written just using numpy, although there are libraries like scikit-learn which can be used to perform linear regression. But when you are learning, it is better to write the code yourself, so that you can understand the inner workings of the algorithm.

```python
import numpy as np
from collections import Counter


def euclidean_distance(x1, x2):
    return np.sqrt(np.sum((x1 - x2) ** 2))


class KNN:
    def __init__(self, k=3):
        self.k = k

    def fit(self, train, train_labels):
        self.X_train = train
        self.y_train = train_labels

    def predict(self, test):
        predicted_labels = [self._predict(x) for x in test]
        # convert predicted_labels to numpy array
        return np.array(predicted_labels)

    # helper function for predict function
    def _predict(self, x):
        # compute the distances
        distances = [euclidean_distance(x, x_train) for x_train in self.X_train]

        # get k nearest samples, labels
        k_indices = np.argsort(distances)[: self.k]
        k_nearest_labels = [self.y_train[i] for i in k_indices]

        # majority vote, most common class label
        # Counter(any_list).most_common(k) returns a list of a k tuples
        # where each tuple is of the form (k_most_common, frequency_of_k_most_common)
        most_common = Counter(k_nearest_labels).most_common(1)
        # get the first element of first tuple from most_common
        return most_common[0][0]
```

"""