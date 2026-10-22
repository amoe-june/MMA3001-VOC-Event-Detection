# MMA3001 – Detection of Unusual VOC Events

This project investigates whether environmental sensor measurements can be used to identify unusually high volatile organic compound (VOC) events.

The analysis was completed as part of **MMA3001 Numerical Methods and Machine Learning** at Monash University.

## Project Objective

The aim of this project is to:

- explore environmental sensor data and assess data quality;
- select a suitable sensor and continuous analysis period;
- define unusual VOC events using a data-driven threshold;
- investigate temporal and environmental patterns associated with high-VOC observations;
- compare classification approaches for detecting rare high-VOC events; and
- evaluate the trade-off between event detection and false alarms.

## Data

The project uses the Monash Smart Infrastructure environmental sensor dataset.

The main analysis uses measurements including:

- temperature;
- humidity;
- carbon dioxide;
- pressure;
- particulate matter (PM1, PM2.5, PM4 and PM10);
- light volatile organic compounds; and
- timestamps and sensor identifiers.

The raw data files are not included in this repository because of their size. The notebook expects the required dataset files to be available locally before execution.

## Analysis Workflow

The notebook follows five main stages:

1. **Data Loading and Sensor Identification**  
   Sensor measurements and sensor metadata are loaded and inspected.

2. **Data Preprocessing**  
   JSON-formatted sensor measurements are extracted into numerical columns and timestamps are converted to UTC-aware datetime values.

3. **Sensor Data Exploration and Selection**  
   Sensor coverage, sampling behaviour, missing values and time gaps are examined. Sensor `6012002000326` is selected for further analysis, and a continuous post-gap period is used for the main analysis.

4. **VOC Event Definition and Analysis**  
   High-VOC events are defined using the 95th percentile of non-zero VOC readings. Temporal patterns and relationships with other environmental variables are explored.

5. **Classification Model Development**  
   Three classification approaches are compared:
   - dummy baseline classifier;
   - decision tree classifier; and
   - logistic regression.

Because high-VOC events are rare, model performance is assessed using precision, recall, F1 score, true positives, false positives and false negatives rather than overall accuracy alone.

## Key Findings

The dataset is highly imbalanced, making unusual VOC events difficult to classify reliably.

The decision tree and logistic regression both detected some high-VOC observations, while the dummy classifier detected none. Logistic regression achieved higher recall but produced substantially more false-positive predictions. The decision tree therefore provided a more balanced preliminary trade-off between detection and false alarms.

Within the fitted decision tree, time of day and carbon dioxide were the most influential predictors. These relationships are specific to the fitted model and should not be interpreted as causal.

## Limitations

Important limitations include:

- only one environmental sensor was used for the final analysis;
- very few high-VOC observations were present in the test set;
- the VOC threshold is data-driven rather than an established indoor-air-quality limit;
- a random train-test split does not explicitly account for temporal dependence between nearby observations; and
- further validation using additional sensors, longer time periods and time-based testing would be required before operational use.

## Repository Contents

- `MMA3001_VOC_Event_Detection.ipynb` — complete data analysis and classification notebook
- `README.md` — project overview and execution information

Additional project documentation, testing files and licensing information will be included as required for the final submission.

## Software

The project was developed in Python using:

- pandas
- NumPy
- Matplotlib
- scikit-learn
- Jupyter / Google Colab

## Running the Notebook

1. Download or clone this repository.
2. Make the required raw sensor dataset files available in the working environment.
3. Update the file paths in the data-loading section if necessary.
4. Open `MMA3001_VOC_Event_Detection.ipynb`.
5. Run all cells from top to bottom.

The final notebook has been tested by running the complete workflow from a fresh session.
