# 🚗 Car Market Analysis: Vehicle Pricing & Feature Trends

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![pandas](https://img.shields.io/badge/pandas-2.0%2B-green.svg)](https://pandas.pydata.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 📊 Project Overview

This project performs a comprehensive exploratory analysis of the automotive market using a dataset of 10,000+ vehicles spanning 27 years (1990-2017). The analysis reveals key insights into pricing trends, brand positioning, and feature relationships that help consumers make informed decisions and provide market intelligence for industry stakeholders.

**Key Questions Addressed:**
- How has the car market evolved over time?
- What factors influence vehicle pricing?
- Which brands dominate different market segments?
- How do technical features correlate with price and efficiency?

## 📈 Key Findings

| Finding | Insight |
|---------|---------|
| **Market Growth** | 200% increase in models available (1990-2017) |
| **Price Distribution** | 75% of vehicles priced under $45K (median: $30K) |
| **Brand Leadership** | BMW, Chevrolet, Mercedes-Benz top by volume |
| **Price-Feature Correlation** | Engine HP and price: r = 0.67 |
| **Performance Trade-off** | Engine HP and MPG: r = -0.57 |

## 🛠️ Tools & Technologies

- **Python 3.9+** - Core programming language
- **pandas** - Data manipulation and analysis
- **matplotlib** - Static visualizations
- **seaborn** - Statistical visualizations
- **Jupyter Notebook** - Interactive analysis environment

## 📁 Dataset Information

**Source:** Kaggle - Car Features and MSRP Dataset  
**Size:** 10,177 vehicles, 18 features  
**Features:** Make, Model, Year, Engine HP, Engine Cylinders, Transmission Type, MPG (city/highway), MSRP, Popularity

## 🧹 Data Cleaning Process

1. **Missing Values:** Numeric → median imputation, Categorical → 'Unknown'
2. **Duplicates:** 715 duplicate records removed
3. **Outliers:** IQR method applied to MSRP and Engine HP
4. **Feature Engineering:** Created Avg MPG and Price Category features

## 📊 Visualizations

### Figure 1: Market Overview Dashboard
![Dashboard](figures/dashboard.png)
*Four-panel overview of market trends, price distribution, top brands, and feature relationships*

### Figure 2: Price Distribution
![Price Distribution](figures/price_distribution.png)
*Histogram with mean/median lines showing right-skewed distribution*

### Figure 3: Brand Analysis
![Brand Analysis](figures/brand_analysis.png)
*Top 10 brands with average price comparison*

### Figure 4: Feature Correlations
![Correlation Heatmap](figures/correlation_heatmap.png)
*Heatmap revealing key relationships between numerical features*

## 🚀 How to Run This Project

### Prerequisites
```bash
pip install -r requirements.txt
