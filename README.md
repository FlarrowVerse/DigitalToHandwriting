# Digital To Handwriting

This project is targeted towards procastinators such as ourselves, who find it easier to type something than write something. 
This project is supposed to help them convert the digital copy of their code/assigment/or other things to their handwritten one(also digital).

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install

For windows/linux systems first make sure you have python 3 installed. To check if already installed or not you can use the folloeing command
```
python --version
```
it should show you something like:
```
Python 3.x.x
```
(x is for any version of 3)

After this make sure you have the following python 3rd party libraries installed:

```
cv2 (OpenCV version 2)

numpy(number python)
```


### Installing

A step by step series of examples that tell you how to get a development env running

Installing python might be different for different OS-s, please google :-)

After installing python and setting it up using the environment variables(google please) install the following packages from terminal

numpy installations:

For linux:
```
pip install numpy

pip3 install numpy
```
For windows

```
python -m pip install numpy

python3 -m pip install numpy
```

cv2 installation:

For linux:
```
pip install opencv-python

pip3 install opencv-python
```
For windows:

```
python -m pip install opencv-python

python3 -m pip install opencv-python
```

## Running the tests

To run the test:

1. Download the project

2. from the folder run the file "main.py" using python

3. From terminal:
	```python3 main.py```

4. You should provide the dimensions of your desired output in pixels e.g.: 20 20

5. Then provide the text you need converting

6. To end the input process provide ":q" as the last line

### Break down into end to end tests

The output image is both shown to you(press esc to close it) and stored in the directory called Output.
