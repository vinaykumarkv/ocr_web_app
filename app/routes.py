# app/routes.py
from flask import Flask, render_template, request, redirect, url_for
from PIL import Image
import pytesseract
import os

# Set the tesseract executable path
tesseract_path = os.path.join(os.path.dirname(__file__), '..', 'tesseract', 'tesseract.exe')
pytesseract.pytesseract.tesseract_cmd = tesseract_path

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.path.join(os.path.dirname(__file__), '..', 'uploads')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Check if a file is uploaded
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file:
            # Save the file to the upload folder
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)

            # Perform OCR on the uploaded image
            text = perform_ocr(file_path)

            # Remove the uploaded file after processing
            os.remove(file_path)

            return render_template('index.html', text=text)
    return render_template('index.html', text='')

def perform_ocr(image_path):
    try:
        # Load the image from file
        image = Image.open(image_path)

        # Perform OCR on the image
        text = pytesseract.image_to_string(image)

        # Return the extracted text
        return text
    except Exception as e:
        # Log the error (consider using a logging framework)
        return f"Error during OCR processing: {e}"

if __name__ == '__main__':
    app.run(debug=True)