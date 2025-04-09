## Wise Analytics Sales Forecasting - README
## Project Overview
This project focuses on building a robust time series sales forecasting model using historical sales data along with external factors like oil prices, holidays, transactions, and store metadata. The goal is to predict future sales to support business decisions in inventory management and marketing.

## Data Preprocessing Steps
Data Merging
Merged multiple CSVs:

train.csv — sales history

stores.csv — store-level details

transactions.csv — customer traffic

holidays_events.csv — national/local holidays and events

oil.csv — daily oil prices (economic indicator)

Missing Value Handling

Interpolated and forward-filled oil prices

Filled missing transactions and promotions with 0

Removed outliers using Z-score method per store/family

Feature Engineering
Extracted new features to improve model accuracy:

Time features: day, month, weekday, payday, weekend

Event flags: national/regional/local holidays, earthquake

Lag/rolling features: past 7/30-day sales, moving averages

Store-level: type, cluster, top-performing families

Label encoding: applied to family, city, state, type

Train/Test Split
Used a time-based split (last 60 days as test set) to simulate real forecasting conditions.

## Models Built
Naïve Forecasting
Predicts next day's sales as same as previous day. Used as baseline.

LSTM Neural Network
Sequential model trained on time-windowed input. Captures patterns and seasonality effectively.

## Evaluation Metric
Used Root Mean Squared Log Error (RMSLE):

Penalizes under-prediction more than over-prediction

Reduces the effect of large outliers

Ideal for skewed sales data

 Results Summary
Model	RMSLE (Lower = Better)
Naïve	~1.02
LSTM	0.40 ✅
## Business Insights & Recommendations 
Best Model: LSTM

LSTM gave the most accurate results. It understood seasonality, trends, and promotional spikes better than the other models.

## External Factors That Impacted Sales
Promotions: Big sales boost. Weekly spikes during promo periods were detected.

Holidays: National holidays decreased sales due to closures. Local holidays had varying impact.

Oil Prices: Slight negative effect—higher prices led to lower sales in some periods.
## Business Strategy Suggestions
Use LSTM for Weekly Inventory Forecasting
Especially for top-selling stores and families.

Plan Inventory Around Holidays/Promotions
Avoid overstocking on holidays. Stock up before promo periods.

Use Transactions for Daily Demand
Transaction counts can help adjust short-term forecasts.

Track Economic Indicators
Add inflation, oil price, and more macro indicators to adjust long-term strategy.