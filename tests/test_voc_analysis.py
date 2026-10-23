import json

from voc_analysis import extract_measurements, model_results


def test_extract_measurements_with_values():
    sample = json.dumps([
        {
            "variable": {"name": "Temperature"},
            "values": [{"value": 22.5}],
        },
        {
            "variable": {"name": "Humidity"},
            "values": [{"value": 55}],
        },
    ])

    result = extract_measurements(sample)

    assert result["Temperature"] == 22.5
    assert result["Humidity"] == 55


def test_extract_measurements_with_missing_value():
    sample = json.dumps([
        {
            "variable": {"name": "Temperature"},
            "values": [],
        }
    ])

    result = extract_measurements(sample)

    assert result["Temperature"] is None


def test_model_results():
    y_true = [0, 0, 1, 1]
    y_pred = [0, 1, 1, 0]

    result = model_results("Test Model", y_true, y_pred)

    assert result["Model"] == "Test Model"
    assert result["True Positives"] == 1
    assert result["False Positives"] == 1
    assert result["False Negatives"] == 1
    assert result["Precision"] == 0.5
    assert result["Recall"] == 0.5
    assert result["F1 Score"] == 0.5