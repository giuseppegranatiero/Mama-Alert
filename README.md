# Mama-Alert

Simple program which is able to recognize given faces and alert you about who is found by speech synthesis (text-to-speech), powered by Google's machine learning technology.

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
This project is simple Lorem ipsum dolor generator.
	
## Technologies
Project is created with the following Python libraries (no worries, they're all listed in requirements.txt):
* face_recognition: 1.3.0
* gTTS: 2.2.4
* numpy: 1.21.0
* opencv_python: 4.6.0.66
* playsound: 1.2.2
	
## Setup
To run this project, install the required libraries:

```
$ pip install -r requirements.txt
```

First run the server

```
$ python server.py
```

Run the static client (speaker)

```
$ python client_static.py
```

Run the dynamic client (camera)

```
$ python client_dynamic_face_recognition.py
```



