from flask import Flask, render_template, jsonify, request, send_file, redirect, url_for, session
from src.exception import CustomException
from src.logger import logging 
import sys
import os
import pandas as pd
import tempfile
from src.pipelines.prediction_pipeline import predictionpipeline

app = Flask(__name__)
app.secret_key = 'sensor_fault_detection_secret_key'  # Required for session

# Global variable to store the path of the last prediction file
LAST_PREDICTION_FILE = None

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST', 'GET'])
def upload():
    global LAST_PREDICTION_FILE
    
    try:
        if request.method == 'POST':
            # Instantiate prediction pipeline
            pipeline = predictionpipeline(request=request)

            # Run prediction pipeline
            prediction_file_detail = pipeline.run_pipeline()
            
            # Store the prediction file path for later use
            LAST_PREDICTION_FILE = prediction_file_detail.prediction_file_path
            
            # Process the prediction results
            df = pd.read_csv(LAST_PREDICTION_FILE)
            
            # Assume the prediction column is named 'Prediction' or similar
            # Adjust this based on your actual output format
            prediction_column = [col for col in df.columns if 'prediction' in col.lower() or 'status' in col.lower() or 'good/bad' in col.lower()]
            if not prediction_column:
                # If no obvious prediction column, use the last column
                prediction_column = df.columns[-1]
            else:
                prediction_column = prediction_column[0]
            
            # Convert predictions to 'Good' or 'Faulty' (adjust based on your model output)
            # This assumes 0 = Good, 1 = Faulty, but modify as needed
            sensors = []
            for index, row in df.iterrows():
                # This is a placeholder - you'll need to adjust based on your actual data structure
                status = 'Good' if row[prediction_column] == 0 else 'Faulty'
                
                # For demonstration, we're setting a random confidence value
                # In a real app, you'd use actual confidence scores from your model
                import random
                confidence = round(random.uniform(70, 99), 1)
                
                # Determine sensor name - adjust as needed based on your data
                sensor_name = f"Sensor-{index+1}"
                if 'sensor_id' in df.columns:
                    sensor_name = row['sensor_id']
                elif 'name' in df.columns:
                    sensor_name = row['name']
                
                sensors.append({
                    'name': sensor_name,
                    'status': status,
                    'confidence': confidence
                })
            
            # Count good and bad sensors
            good_count = sum(1 for sensor in sensors if sensor['status'] == 'Good')
            bad_count = len(sensors) - good_count
            
            return render_template('results.html', 
                                  sensors=sensors,
                                  good_count=good_count,
                                  bad_count=bad_count)
        else:
            return render_template('upload.html')  
    
    except Exception as e:
        logging.exception("An error occurred during prediction.")
        error_message = str(e)
        # Check if it's a feature names mismatch error
        if "Feature names unseen at fit time" in error_message:
            return render_template('error.html', 
                                  error_message="The CSV file format is incorrect. The column names don't match what our model expects.")
        else:
            return render_template('error.html', error_message=error_message)

@app.route('/download_results')
def download_results():
    global LAST_PREDICTION_FILE
    if LAST_PREDICTION_FILE and os.path.exists(LAST_PREDICTION_FILE):
        return send_file(LAST_PREDICTION_FILE,
                        download_name='sensor_prediction_results.csv',
                        as_attachment=True)
    else:
        return redirect(url_for('home'))

@app.route('/sample_format')
def sample_format():
    # This route should return a sample CSV file with the correct format
    # You'll need to create this file and place it in your static folder
    return send_file('static/sample_format.csv',
                     download_name='sample_format.csv',
                     as_attachment=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000, debug=True)