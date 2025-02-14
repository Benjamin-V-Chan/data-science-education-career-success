# data-science-education-career-success

# Project Overview
This project analyzes the factors influencing education and career success. It processes data, explores relationships, engineers new features, builds predictive models, and visualizes key insights.

# Folder Structure
```
project-root/
├── data/                      # Contains the raw dataset
│   ├── education_career_success.csv
├── scripts/                   # Contains Python scripts for analysis
│   ├── 01_preprocessing.py
│   ├── 02_eda.py
│   ├── 03_feature_engineering.py
│   ├── 04_modeling.py
│   ├── 05_visualizations.py
├── outputs/                   # Stores results and generated outputs
│   ├── processed_data.csv
│   ├── eda_summary.txt
│   ├── model_performance.txt
│   ├── plots/
├── requirements.txt           # Required dependencies
├── README.md                  # Documentation
```

# Usage

### 1. Setup the Project:
Clone the repository.
Ensure you have Python installed.
Install required dependencies using the requirements.txt file:
```sh
pip install -r requirements.txt
```

### 2. Run Data Preprocessing:
```sh
python scripts/01_preprocessing.py
```
This script cleans and processes the dataset, converting categorical variables and handling missing values.

### 3. Perform Exploratory Data Analysis (EDA):
```sh
python scripts/02_eda.py
```
This script generates descriptive statistics and correlation insights, saving the results in `outputs/eda_summary.txt`.

### 4. Engineer Features:
```sh
python scripts/03_feature_engineering.py
```
This script creates new features, scales numerical values, and prepares the dataset for modeling.

### 5. Train and Evaluate Models:
```sh
python scripts/04_modeling.py
```
This script builds a regression model to predict career success metrics and saves evaluation results in `outputs/model_performance.txt`.

### 6. Generate Visualizations:
```sh
python scripts/05_visualizations.py
```
This script creates plots such as correlation heatmaps and salary distributions, saving them in `outputs/plots/`.

# Requirements
- Python 3.x
- pandas
- scikit-learn
- matplotlib
- seaborn

# Acknowledgments
**Dataset Name:** Education & Career Success.
**Dataset Author:** Adil Shamim
**Dataset Source:** [Kaggle](https://www.kaggle.com/datasets/adilshamim8/education-and-career-success)