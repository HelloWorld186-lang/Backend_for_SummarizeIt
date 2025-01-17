from setuptools import setup, find_packages

setup(
    name='summariesit',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'Flask==2.3.2',
        'Flask-CORS==3.0.10',
        'PyPDF2==3.0.1',
        'nltk==3.8.1',
        'sumy==0.11.0',
        'python-pptx==0.6.23',
        'pyttsx3==2.90',
        'moviepy==1.0.3',
        'Pillow==10.1.0',
        'gunicorn==20.1.0',
    ],
)