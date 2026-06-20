# PlaceMux Task 1 – System Ingestion & Model Environment Setup

## Objective

Set up a reproducible machine learning environment and verify the complete machine learning workflow including data ingestion, validation, dataset splitting, baseline model training, evaluation, and experiment tracking.

---

## Technologies Used

* Python
* NumPy
* Pandas
* Scikit-Learn
* Jupyter Notebook
* Git

---

## Project Structure

```text
data/
logs/
│   └── metrics.csv
notebooks/
│   └── starter.ipynb
src/
│   └── train.py
requirements.txt
README.md
.gitignore
```

---

## Work Completed

### Environment Setup

* Created isolated Python environment
* Installed required libraries
* Generated requirements.txt
* Configured fixed random seed (42)

### Dataset Ingestion

* Loaded Iris dataset from Scikit-Learn
* Verified dataset shape and data types
* Checked class balance

### Dataset Splitting

* Performed stratified Train/Validation/Test split
* Preserved class distribution across datasets

### Baseline Model

* Trained a DummyClassifier baseline model
* Evaluated model on unseen test data
* Calculated accuracy metric

### Experiment Logging

* Created metrics.csv for experiment tracking
* Logged model information and evaluation results

### Verification

* Verified notebook execution
* Verified source module execution
* Verified dependency installation
* Verified end-to-end workflow

---

## Notes

No project-specific dataset was provided during onboarding. Therefore, the Iris dataset available in Scikit-Learn was used to validate the data ingestion pipeline, dataset splitting process, baseline model training workflow, and experiment tracking setup.

---

## Status

Task 1 completed successfully.

The project environment and machine learning workflow have been verified and are ready for future development tasks.
