# OCR Web App

This is a Flask application that includes Tesseract OCR for performing optical character recognition on images.

## Project Structure
my_flask_app/ ├── app/ │ ├── init.py │ ├── routes.py │ ├── templates/ │ │ └── index.html ├── tesseract/ │ ├── tesseract.exe │ └── tessdata/ # Tesseract data files ├── uploads/ ├── README.md ├── requirements.txt ├── setup.py └── run.py


## Prerequisites

- Python 3.x
- Virtual environment (`venv`)

## Installation

1. **Clone the repository**:
   git clone https://github.com/vinaykumarkv/ocr_web_app.git
   cd ocr_web_app
2. **Create a virtual environment**:

  python -m venv venv

# Activate the virtual environment:
**On Windows**:
  venv\Scripts\activate
**On macOS/Linux**:
  source venv/bin/activate
**Install the required dependencies**:
  pip install -r requirements.txt
# Setting Up Tesseract
**Download Tesseract**:
Download the Tesseract OCR executable for your operating system from the Tesseract GitHub repository.
**Place Tesseract in the Project Directory**:
Place the tesseract.exe file and the tessdata directory in the tesseract directory within your project.
# Building and Installing the Package
**Build the package**:
python setup.py sdist bdist_wheel
**Install the package**:
pip install .
**Running the Application**
Run the Flask application:
python run.py
**Access the application**:
Open your web browser and navigate to http://127.0.0.1:5000/.
# Usage
**Upload an Image**:
On the homepage, upload an image file for OCR processing.
**View Extracted Text**:
After uploading the image, the extracted text will be displayed on the page.
# Troubleshooting
**Tesseract Not Found**:
Ensure that the tesseract.exe file is located in the tesseract directory within your project.
Verify that the tessdata directory is also correctly placed in the tesseract directory.
**Python Dependencies**:
Ensure that all required Python packages are installed by running pip install -r requirements.txt.
License
This project is licensed under the MIT License. See the LICENSE file for more information.


# Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

# Contact
If you have any questions or issues, please contact Vinay Kumar K V - kvvk.win@gmail.com
