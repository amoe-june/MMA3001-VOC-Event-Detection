"""Utility functions for the MMA3001 VOC Event Detection project.

This module contains reusable functions used in the analysis of
environmental sensor data and the evaluation of classification models.
"""

import json

from sklearn.metrics import (
    confusion_matrix,
    precision_score,
    recall_score,
    f1_score,
)


def extract_measurements(json_string):
    """Extract environmental measurements from a JSON sensor record.

    Parameters
    ----------
    json_string : str
        JSON-formatted sensor data containing measurement names and values.

    Returns
    -------
    dict
        Dictionary mapping each measurement name to its recorded value.
        Missing measurements are returned as None.
    """
    data = json.loads(json_string)

    measurements = {}

    for item in data:
        name = item["variable"]["name"]

        if item.get("values") and "value" in item["values"][0]:
            value = item["values"][0]["value"]
        else:
            value = None

        measurements[name] = value

    return measurements


def model_results(name, y_true, y_pred):
    """Calculate classification metrics for a VOC detection model.

    Parameters
    ----------
    name : str
        Name of the classification model.
    y_true : array-like
        Actual high-VOC classification labels.
    y_pred : array-like
        Predicted high-VOC classification labels.

    Returns
    -------
    dict
        Dictionary containing precision, recall, F1 score,
        true positives, false positives, and false negatives.
    """
    tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()

    return {
        "Model": name,
        "Precision": precision_score(y_true, y_pred, zero_division=0),
        "Recall": recall_score(y_true, y_pred, zero_division=0),
        "F1 Score": f1_score(y_true, y_pred, zero_division=0),
        "True Positives": tp,
        "False Positives": fp,
        "False Negatives": fn,
    }