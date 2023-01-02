# @Project:     LearnML
# @Filename:    knn.py
# @Author:      Daksh
# @Time:        02-01-2023 09:02 pm

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