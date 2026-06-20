# Task 1 - System Ingestion & Model Environment Setup

## Objective

To set up a reproducible machine learning environment and prepare the project structure for future model training and evaluation tasks.

## Environment Setup

* Created an isolated Python virtual environment.
* Installed required libraries:

  * NumPy
  * Pandas
  * Scikit-learn
  * Jupyter Notebook
* Generated requirements.txt to ensure reproducibility.

## Reproducibility

* Fixed random seed value (42) for deterministic execution.
* Version-controlled dependencies using pip freeze.

## Project Structure

* data/ : Dataset storage directory
* notebooks/ : Jupyter notebooks
* src/ : Python source files
* logs/ : Experiment logs and metrics
* requirements.txt : Dependency versions
* README.md : Documentation

## Experiment Tracking

A metrics.csv file was created to record future model evaluation results.

## Current Status

Environment setup completed successfully. The project is ready for dataset ingestion, train/validation/test splitting, model training, and evaluation once the project dataset is provided.

## Verification

* Environment activated successfully.
* Required libraries installed.
* Seed configuration verified.
* Starter notebook executed successfully.
