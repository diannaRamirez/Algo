"""
Mean Squared Error (MSE) Loss Function

This script defines the Mean Squared Error (MSE) loss function, which is commonly used for regression problems.

Description:
The Mean Squared Error (MSE) measures the average squared difference between the true values (ground truth) and the predicted values produced by a model. It is widely used in regression tasks and serves as a measure of the model's accuracy.

Formula:
MSE = (1/n) * Σ(y_true - y_pred)^2

Source:
- [Wikipedia - Mean squared error](https://en.wikipedia.org/wiki/Mean_squared_error)
"""

import numpy as np


def mean_squared_error(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """
    Calculate the Mean Squared Error (MSE) between two arrays.

    Parameters:
    - y_true: The true values (ground truth).
    - y_pred: The predicted values.

    Returns:
    - mse: The Mean Squared Error between y_true and y_pred.

    Example usage:
    >>> true_values = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
    >>> predicted_values = np.array([0.8, 2.1, 2.9, 4.2, 5.2])
    >>> mean_squared_error(true_values, predicted_values)
    0.028000000000000032
    """
    if len(y_true) != len(y_pred):
        raise ValueError("Input arrays must have the same length.")

    squared_errors = (y_true - y_pred) ** 2
    return np.mean(squared_errors)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
