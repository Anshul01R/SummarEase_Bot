# app.py
from flask import Flask, render_template, request, jsonify
import os
from src.TextSummarizer.pipeline.prediction import PredictionPipeline

app = Flask(__name__, static_folder="static", template_folder="static")

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/train', methods=['GET'])
def train():
    try:
        # Replace with actual training script call
        os.system("python main.py")
        return "Training successful !!"
    except Exception as e:
        return f"Error Occurred: {e}"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract the text from the request
        data = request.json
        text = data.get('text', '')

        # Initialize the Prediction Pipeline and perform prediction
        obj = PredictionPipeline()
        summary = obj.predict(text)

        # Return summary as JSON response
        return jsonify({'summary': summary})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
