# Smart Crop Predictor

## Overview
This is a Flask-based web application that uses machine learning to recommend crops based on soil and environmental parameters. The application uses a Decision Tree model trained on agricultural data to predict the most suitable crop for given conditions.

## Project Structure
- `app.py` - Main Flask application with prediction API
- `templates/index.html` - Frontend UI with Tailwind CSS
- `final_crop_decision_tree_model.joblib` - Trained ML model
- `model_features.joblib` - Feature names for the model
- `Crop_recommendation.csv` - Training dataset
- `requirements.txt` - Python dependencies

## Technology Stack
- **Backend**: Python 3.11, Flask 3.0+
- **ML**: scikit-learn 1.2.2, pandas, joblib
- **Frontend**: HTML, JavaScript, Tailwind CSS
- **Server**: Running on port 5000

## Features
The model predicts crops based on:
- Nitrogen (N) content - kg/ha
- Phosphorus (P) content - kg/ha
- Potassium (K) content - kg/ha
- Temperature - °C
- Humidity - %
- pH Level

## Recent Changes
- 2025-11-10: Initial setup in Replit environment
- Configured to run on port 5000 with host 0.0.0.0
- Dependencies installed via Python package manager

## Architecture Notes
- Flask serves both the frontend (HTML template) and backend API
- Model is loaded once on server startup for efficiency
- Uses specific scikit-learn version (1.2.2) for model compatibility
- Single-page application with async fetch API for predictions
