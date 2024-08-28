"""
Similarity Search : https://en.wikipedia.org/wiki/Similarity_search
Similarity search is a search algorithm for finding the nearest vector from
vectors, used in natural language processing.
In this algorithm, it calculates distance with euclidean distance and
returns a list containing two data for each vector:
    1. the nearest vector
    2. distance between the vector and the nearest vector (float)

This implementation also includes cosine similarity as an alternative measure.
"""

from __future__ import annotations

import math
from typing import Callable, List, Tuple, Union

import numpy as np
from numpy.linalg import norm

VectorType = Union[List[float], np.ndarray]
DistanceFunction = Callable[[np.ndarray, np.ndarray], float]


def euclidean(input_a: np.ndarray, input_b: np.ndarray) -> float:
    """
    Calculates euclidean distance between two data.
    :param input_a: ndarray of first vector.
    :param input_b: ndarray of second vector.
    :return: Euclidean distance of input_a and input_b. By using math.sqrt(),
             result will be float.

    >>> euclidean(np.array([0]), np.array([1]))
    1.0
    >>> euclidean(np.array([0, 1]), np.array([1, 1]))
    1.0
    >>> euclidean(np.array([0, 0, 0]), np.array([0, 0, 1]))
    1.0
    """
    return np.sqrt(np.sum((input_a - input_b) ** 2))


def similarity_search(
    dataset: np.ndarray,
    value_array: np.ndarray,
    distance_func: DistanceFunction = euclidean,
    k: int = 1,
) -> List[List[Union[List[float], float]]]:
    """
    :param dataset: Set containing the vectors. Should be ndarray.
    :param value_array: vector/vectors we want to know the nearest vector from dataset.
    :param distance_func: Distance function to use (default: euclidean).
    :param k: Number of nearest neighbors to return (default: 1).
    :return: Result will be a list containing
            1. the nearest vector(s)
            2. distance(s) from the vector(s)

    >>> dataset = np.array([[0], [1], [2]])
    >>> value_array = np.array([[0]])
    >>> similarity_search(dataset, value_array)
    [[[0], 0.0]]

    >>> dataset = np.array([[0, 0], [1, 1], [2, 2]])
    >>> value_array = np.array([[0, 1]])
    >>> similarity_search(dataset, value_array)
    [[[0, 0], 1.0]]

    >>> dataset = np.array([[0, 0, 0], [1, 1, 1], [2, 2, 2]])
    >>> value_array = np.array([[0, 0, 1]])
    >>> similarity_search(dataset, value_array)
    [[[0, 0, 0], 1.0]]

    >>> dataset = np.array([[0, 0, 0], [1, 1, 1], [2, 2, 2]])
    >>> value_array = np.array([[0, 0, 0], [0, 0, 1]])
    >>> similarity_search(dataset, value_array)
    [[[0, 0, 0], 0.0], [[0, 0, 0], 1.0]]

    >>> dataset = np.array([[0, 0], [1, 1], [2, 2]])
    >>> value_array = np.array([[0, 1]])
    >>> similarity_search(dataset, value_array, k=2)
    [[[0, 0], 1.0], [[1, 1], 1.0]]

    These are the errors that might occur:

    1. If dimensions are different.
    For example, dataset has 2d array and value_array has 1d array:
    >>> dataset = np.array([[1]])
    >>> value_array = np.array([1])
    >>> similarity_search(dataset, value_array)
    Traceback (most recent call last):
        ...
    ValueError: Wrong input data's dimensions... dataset : 2, value_array : 1

    2. If data's shapes are different.
    For example, dataset has shape of (3, 2) and value_array has (2, 3).
    We are expecting same shapes of two arrays, so it is wrong.
    >>> dataset = np.array([[0, 0], [1, 1], [2, 2]])
    >>> value_array = np.array([[0, 0, 0], [0, 0, 1]])
    >>> similarity_search(dataset, value_array)
    Traceback (most recent call last):
        ...
    ValueError: Wrong input data's shape... dataset : 2, value_array : 3

    3. If data types are different.
    When trying to compare, we are expecting same types so they should be same.
    If not, it'll come up with errors.
    >>> dataset = np.array([[0, 0], [1, 1], [2, 2]], dtype=np.float32)
    >>> value_array = np.array([[0, 0], [0, 1]], dtype=np.int32)
    >>> similarity_search(dataset, value_array)  # doctest: +NORMALIZE_WHITESPACE
    Traceback (most recent call last):
        ...
    TypeError: Input data have different datatype...
    dataset : float32, value_array : int32
    """

    if dataset.ndim != value_array.ndim:
        msg = (
            "Wrong input data's dimensions... "
            f"dataset : {dataset.ndim}, value_array : {value_array.ndim}"
        )
        raise ValueError(msg)

    try:
        if dataset.shape[1] != value_array.shape[1]:
            msg = (
                "Wrong input data's shape... "
                f"dataset : {dataset.shape[1]}, value_array : {value_array.shape[1]}"
            )
            raise ValueError(msg)
    except IndexError:
        if dataset.ndim != value_array.ndim:
            raise TypeError("Wrong shape")

    if dataset.dtype != value_array.dtype:
        msg = (
            "Input data have different datatype... "
            f"dataset : {dataset.dtype}, value_array : {value_array.dtype}"
        )
        raise TypeError(msg)

    answer = []

    for value in value_array:
        distances = [distance_func(value, data_point) for data_point in dataset]
        nearest_indices = np.argsort(distances)[:k]
        answer.append([[dataset[i].tolist(), distances[i]] for i in nearest_indices])

    return answer[0] if len(answer) == 1 else answer


def cosine_similarity(input_a: np.ndarray, input_b: np.ndarray) -> float:
    """
    Calculates cosine similarity between two data.
    :param input_a: ndarray of first vector.
    :param input_b: ndarray of second vector.
    :return: Cosine similarity of input_a and input_b. By using math.sqrt(),
             result will be float.

    >>> cosine_similarity(np.array([1]), np.array([1]))
    1.0
    >>> cosine_similarity(np.array([1, 2]), np.array([6, 32]))
    0.9615239476408232
    """
    return np.dot(input_a, input_b) / (norm(input_a) * norm(input_b))


def cosine_distance(input_a: np.ndarray, input_b: np.ndarray) -> float:
    """
    Calculates cosine distance between two data.
    :param input_a: ndarray of first vector.
    :param input_b: ndarray of second vector.
    :return: Cosine distance of input_a and input_b.

    >>> cosine_distance(np.array([1]), np.array([1]))
    0.0
    >>> round(cosine_distance(np.array([1, 2]), np.array([6, 32])), 7)
    0.0384761
    """
    return 1 - cosine_similarity(input_a, input_b)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
