# setup.py
from setuptools import setup, find_packages
import os

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="my_flask_tesseract_app",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A Flask app with Tesseract OCR included",
    long_description=read('README.md'),
    long_description_content_type="text/markdown",
    url="https://github.com/vinaykumarkv/my_flask_tesseract_app",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "Flask",
        "pytesseract",
        "Pillow"
    ],
    package_data={
        '': ['tesseract/*', 'app/templates/*'],
    },
    entry_points={
        'console_scripts': [
            'run_my_flask_app=run:app.run',
        ],
    },
)