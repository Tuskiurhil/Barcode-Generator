# Barcode-Generator
A Python3 based Barcode Generator

## Table of contents
* [General info](#general-info)
* [Setup and Usage](#setup)
* [Planned Features](#updates)

## General info

![grafik](https://user-images.githubusercontent.com/79027579/157256767-d4dde2c8-5e74-48ad-aef7-254c14aa41ef.png)
![grafik](https://user-images.githubusercontent.com/79027579/152145930-2443db9a-d50a-429d-b6a7-aa542a3d6e96.png)


Barcode-Generator is a **PythonScript** that takes Values, formats them to a string and turns them into Barcodes

* Current Support:
  - Code128
  - Code39
  - European Article Number 8
  - European Article Number 13
  - European Article Number 14
  - Japan Article Number
  - International Standard Book Number 10
  - International Standard Book Number 13
  - International Standard Serial Number
  - Universal Product Code A
  - PZN (PharmaZentralNummer - Germanys Standardized Pharmaceutical Number)


* Requirements:
  - PySimpleGUI
  - python-barcode
  - opencv-python
  - numpy
	
## Setup and Usage

Download the above mentioned libraries with pip.

* Example "pip install PySimpleGUI" or "pip3 install PySimpleGUI" depending on your version of Python.

To run the script, simply put the "barcodegen.py" file in an accessible location and open it with your terminal.

* Example $BASH: *"python3 /home/"user"/Desktop/code128.py"*

Then just input your Value (eg. "12345", multiple Values can be seperated with a comma eg. "12345,23456,34567"), hit "Create Barcode(s)" and the Script will create a .png file of your barcodes.

The Barcode Images will be put in the same location as the .py file and they will be named according to the Value you gave them.

To change the resolution of the Output Image, adjust the Values in the fields Width and Height


## Planned Features

The planned features are in no particular order

* Add more Formats
* Ability to select filetype of output image (.jpg, .gif, etc.)
