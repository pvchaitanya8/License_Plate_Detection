# License Plate Detection [V1]

Welcome to the License Plate Detection project! This brief documentation will guide you through the process of setting up and running the project for license plate detection using YOLOv5.

## Overview

This project utilizes machine learning to detect license plates with the help of YOLOv5, a pretrained model for object detection. It identifies yellow number plates by analyzing the average pixel values present in the detected number plate regions.

## Getting Started

Follow these steps to set up and run the project:

### Step 0: Download and Open the Project

- Download the project folder and unzip it.
- Open the project folder in Visual Studio Code (VS Code) or your preferred code editor.

### Step 1: Install Dependencies

- Ensure you have a stable internet connection.
- Install the required dependencies by running the following commands in your terminal or command prompt:

```bash
virtualenv venv
```
```bash
pip install -r requirements.txt
```

### Step 2: Run the Project

- To run the project, execute the following command in your terminal or command prompt:

```bash
python app.py
```

### Step 3: Upload Images

- In your web browser.
![image](https://github.com/pvchaitanya8/License_Plate_Detection/assets/93573686/33e45ba1-d347-41e7-a4ff-5721d89c1aa5)
![image](https://github.com/pvchaitanya8/License_Plate_Detection/assets/93573686/6297405c-0f42-47e6-a621-12d78ff7efec)

- Press `CTRL` and click on the link.

### Step 4: Upload and Process Images

- Upload or drag and drop image files into the web interface.
- Click on the "Process" button as shown in the screenshot.

### Step 5: View Output

- After processing, you will receive the following information:
  - Total number of detected yellow license plates.
  - List of images with detected license plates.
  - Output images saved in the directory: `static\output`

### Step 6: Deactivate Virtual Environment

- To deactivate the virtual environment and stop the project execution, use the following command in your terminal or command prompt:

```bash
CTRL + C
```
```bash
deactivate.bat
```

## Execution Video Explanation

For a visual guide on how to run the project, you can watch the [Execution Video Explanation](https://youtu.be/RZSDA3f23SY).

Enjoy using the License Plate Detection project! If you encounter any issues or have questions, please refer to the video or reach out for assistance.
