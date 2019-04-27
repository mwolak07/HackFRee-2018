2018 HackFRee district-wide hackathon project

Description:
	- OCR app for converting hand writing to text using a camera
	- Custom OCR model trained on modified versions of MNIST and EMNIST --> abandoned, accuracy on real-world images too low
	- Tessaract OCR module --> pre-trained OCR model (part of openCV). Allowed for better accuracy
	- OpenCV noise filtering used because openCV requires relatively clean images
	- Firebase was used to send image to computer for processing, and send response back to phone

Environment:
	- Python 3.6
	- numpy       --> pip install numpy
	- scipy       --> pip install scipy
	- matplotlib  --> pip install matplotlib
	- keras       --> pip install keras
	- tensorflow  --> pip install tensorflow
	- opencv      --> pip install opencv-python
	- pillow      --> pip install pillow
	- pytesseract --> pip install pytesseract

*pip might default to python 2, in that case, use pip3
*install tensorflow-gpu for processing on the gpu
*Cuda and cuDNN need to be installed for processing on an Nvidia GPU

Tesseract install for windows:
    - https://github.com/UB-Mannheim/tesseract/wiki
    - The Tesseract-OCR folder must then be added to the system path (usually installed in local appdata)

Team:
Mateusz Wolak, Jon Riklan, Peter Wilmot, Nicholas Procaccio