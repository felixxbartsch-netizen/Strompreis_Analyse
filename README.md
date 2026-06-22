
# German Electricity Price Analysis (2021–2025)

## Overview

This project analyzes German wholesale electricity prices between 2021 and 2025 using Python. The goal was to practice the complete data analytics workflow, from data acquisition and cleaning to statistical analysis and visualization.

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib

## Project Workflow

### 1. Data Preparation

* Imported raw electricity price data
* Selected relevant columns
* Renamed columns for easier handling
* Converted date columns to datetime format
* Removed unnecessary data and duplicates

### 2. Exploratory Data Analysis

* Descriptive statistics
* Identification of negative electricity prices
* Detection of maximum and minimum price events
* Daily and hourly aggregations
* Correlation analysis

### 3. Feature Engineering

* 20-hour and 50-hour moving averages
* Previous-day price comparison using `shift()`
* Percentage price change calculation

### 4. Visualization

* Weekly electricity price trend
* Annual average price comparison
* Year-by-year price development
* Analysis of extreme price events
* Hourly price profile

## Key Findings

* Significant price volatility occurred during the analyzed period.
* Multiple instances of negative electricity prices were identified.
* Electricity prices showed clear seasonal and hourly patterns.
* The energy crisis period was reflected by unusually high price levels and extreme price spikes.

## Skills Demonstrated

* Data cleaning and preprocessing
* Working with time series data
* Datetime handling in Pandas
* Statistical analysis
* Feature engineering
* Data visualization
* Project structuring and modular Python code

## Data Source

German wholesale electricity price data obtained from publicly available market data sources.

## Future Improvements

* Integration of weather data (wind, solar, temperature)
* Inclusion of energy production and demand data
* Advanced correlation analysis
* Predictive modeling and machine learning
* Interactive dashboards using Plotly or Power BI


