# Stock Price Forecasting Using Hybrid Deep Learning Models

This capstone project explores stock price prediction using hybrid models such as **CNN-LSTM**, **Transformer-LSTM**, and **XGBoost-LSTM**. It builds on the paper [Predicting Stock Market Time-Series Data using CNN-LSTM Neural Network Model](https://arxiv.org/abs/2305.14378) and aims to improve prediction accuracy across multiple datasets.

## Demo Video

[Watch the demo video on YouTube](https://youtu.be/kpocSXYlyy8)

> Click the link above to watch a short demo of the project.

---

## Project Goals
- Compare hybrid deep learning models for time-series forecasting
- Evaluate performance on 5 public stock datasets
- Use feature importance (e.g., SHAP) to interpret results

---

## Models Implemented
- CNN-LSTM
- XGBoost-LSTM
- Transformer-LSTM

---

## Repository Structure
- CNN-LSTM/ # CNN-LSTM initial and improvment models, and metrics
- GRU-LSTM/ # GRU-LSTM model and evaluation metrics
- XGBoost/ # XGBoost model files, SHAP plots, and metrics
- Datasets/ # Stock data (TSLA, META, NVDA, BATS)
- Visualizations/ # All plots and evaluation visuals (SHAP, predictions, etc.)

---

## Technologies Used
- Python 3.x
- TensorFlow / Keras
- XGBoost
- Scikit-learn
- SHAP
- Matplotlib / Seaborn

---

## Evaluation Metrics
- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R² Score
- Visual comparison of actual vs predicted prices

---

