import os
import cv2
import numpy as np
import torch
from pathlib import Path
from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

dataset_folder = "dataset"
output_folder = "static/output"  
os.makedirs(output_folder, exist_ok=True)

model_path = Path("model/best.pt")
model = torch.hub.load('ultralytics/yolov5', 'custom', path=model_path, force_reload=True)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = model.to(device)

total_yellow_plate_count = 0
total_plate_count = 0

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    global total_yellow_plate_count  
    global total_plate_count  

    uploaded_files = request.files.getlist('file') 
    total_yellow_plate_count = 0  
    for uploaded_file in uploaded_files:
        if uploaded_file.filename != '':
            image = cv2.imdecode(np.fromstring(uploaded_file.read(), np.uint8), cv2.IMREAD_COLOR)
            results = model(image)
            yellow_plate_count = 0
            detected_plate_count = len(results.xyxy[0])

            for result in results.xyxy[0]:
                x1, y1, x2, y2 = map(int, result[0:4])
                cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 255), 3)
                plate_roi = image[y1:y2, x1:x2]
                lower_yellow = np.array([20, 100, 100])
                upper_yellow = np.array([30, 255, 255])
                mask = cv2.inRange(plate_roi, lower_yellow, upper_yellow)
                if cv2.countNonZero(mask) > 0:
                    yellow_plate_count += 1

            total_yellow_plate_count += yellow_plate_count
            total_plate_count += detected_plate_count

            processed_image_path = os.path.join(output_folder, uploaded_file.filename)
            cv2.imwrite(processed_image_path, image)

    return render_template('result.html', filenames=[uploaded_file.filename for uploaded_file in uploaded_files],  yellow_plate_count=total_yellow_plate_count)

@app.route('/stats')
def stats():
    return f"Total detected plates in dataset: {total_plate_count}<br>Total yellow plate count: {total_yellow_plate_count}"

if __name__ == '__main__':
    app.run(debug=True)
