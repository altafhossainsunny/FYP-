import joblib
import pandas as pd
from flask import Flask, request, jsonify, render_template
import os
import sys

# --- CONFIGURATION ---
# These are the files saved from your Kaggle notebook
MODEL_PATH = 'final_crop_decision_tree_model.joblib'
FEATURES_PATH = 'model_features.joblib'

app = Flask(__name__)

# --- MODEL LOADING (Crucial: Load only ONCE when server starts) ---
model = None
FEATURE_NAMES = None

def load_model():
    global model, FEATURE_NAMES
    try:
        print("Attempting to load model and feature list...")
        
        # Check if files exist
        if not os.path.exists(MODEL_PATH) or not os.path.exists(FEATURES_PATH):
             print(f"ERROR: Model file ('{MODEL_PATH}') or features file ('{FEATURES_PATH}') not found.")
             print("Ensure you have downloaded the latest files from Kaggle and placed them in the same directory as app.py.")
             return

        # Load the trained Decision Tree model (This requires scikit-learn 1.2.2)
        model = joblib.load(MODEL_PATH)
        
        # Load the feature names in the exact order the model expects
        FEATURE_NAMES = joblib.load(FEATURES_PATH)
        print(f"SUCCESS: Model loaded successfully. Expected features: {FEATURE_NAMES}")
        
    except ValueError as e:
        # This is the specific error we have been battling! It is now handled by the version lock.
        print(f"CRITICAL VERSION ERROR during model loading: {e}", file=sys.stderr)
        print("The loaded file's internal structure is incompatible with the currently installed scikit-learn version.", file=sys.stderr)
        print("Please ensure your local environment has 'scikit-learn==1.2.2' installed.", file=sys.stderr)
        model = None
    except Exception as e:
        print(f"ERROR: An unexpected error occurred during model loading: {e}", file=sys.stderr)
        model = None

# Execute the loading function immediately upon startup
load_model()


@app.route('/')
def index():
    """Serves the main HTML page for user input."""
    # Renders the index.html file which must be in a 'templates' folder
    try:
        return render_template('index.html')
    except Exception as e:
        return f"Template render failed. Ensure 'index.html' is in a 'templates' folder inside your project root: {e}", 500


@app.route('/predict', methods=['POST'])
def predict():
    """Handles the API call for crop prediction."""
    if model is None or FEATURE_NAMES is None:
        return jsonify({'error': 'Model is not available. Please check the server console for loading errors.'}), 500

    try:
        # 1. Get JSON data from the request
        data = request.json
        
        # 2. Extract features based on the saved order (FEATURE_NAMES)
        # Missing keys will trigger a KeyError, caught below
        input_values = [data[name] for name in FEATURE_NAMES]

        # 3. Convert input to a DataFrame
        # The model expects a DataFrame with columns matching the training features
        input_df = pd.DataFrame([input_values], columns=FEATURE_NAMES)
        
        # 4. Make the prediction
        prediction_array = model.predict(input_df)
        predicted_crop = prediction_array[0]
        
        # 5. Return the result as JSON
        return jsonify({'recommendation': predicted_crop.upper()})

    except KeyError as e:
        return jsonify({'error': f'Missing required feature: {e}. All inputs must be provided: {FEATURE_NAMES}'}), 400
    except Exception as e:
        # General error during prediction
        return jsonify({'error': f'Prediction failed due to an internal error: {e}'}), 500


if __name__ == '__main__':
    # Running on 0.0.0.0 is useful for development
    app.run(debug=True, host='0.0.0.0', port=5000)