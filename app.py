from flask import Flask, request, jsonify
import pickle
import pandas as pd

# Load the saved pipeline
with open('vehicle_maintenance_pipeline.pkl', 'rb') as f:
    loaded_pipeline = pickle.load(f)

# Initialize Flask app
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the input JSON from the request
        input_data = request.get_json()
        
        # Convert JSON to DataFrame
        input_df = pd.DataFrame([input_data])  # Convert to a DataFrame
        
        # Predict using the pipeline
        predicted_class = loaded_pipeline.predict(input_df)
        predicted_probability = loaded_pipeline.predict_proba(input_df)[:, 1]
        
        # Prepare response
        response = {
            'Predicted_Class': int(predicted_class[0]),  # 0 or 1
            'Probability_of_Needing_Maintenance': float(predicted_probability[0])  # Probability
        }
        return jsonify(response)

    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Add health check route
@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy', 'message': 'The app is running successfully'}), 200

# Run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)