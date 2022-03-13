<img src="https://user-images.githubusercontent.com/79027579/157531034-474a6480-1168-44fc-a7b5-d66144a8103b.png" width=30% height=30%>


# Barcode-Generator
A Python3 based Barcode Generator

## Table of contents
* [General info](#general-info)
* [Setup and Usage](#setup)
* [Planned Features](#updates)

## General info

![grafik](https://user-images.githubusercontent.com/79027579/157472974-50093cb0-41f5-48fe-bac9-367be0ded99c.png)
![grafik](https://user-images.githubusercontent.com/79027579/157473184-7a20c2bb-b78a-4171-a751-fbb0b2beb08b.png)


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

  - QR Code

* Requirements:
  - PySimpleGUI
  - python-barcode
  - opencv-python
  - numpy
  - qrcode
  - requests
	
## Setup and Usage

Download the above mentioned libraries with pip.

* Example "pip install PySimpleGUI" or "pip3 install PySimpleGUI" depending on your version of Python.

To run the script, simply put the "barcodegen.py" file in an accessible location and open it with your terminal.

* Example $BASH: *"python3 /home/"user"/Desktop/code128.py"*

Then just input your Value (eg. "12345", multiple Values can be seperated with a comma eg. "12345,23456,34567"), select which Filetype and Barcode Format you want, hit "Create Barcode(s)" and the Script will turn your input into barcode images.

The Barcode Images will be put in the same location as the .py file and they will be named according to the Value and Barcode Format you gave them.

To change the resolution of the Output Image, adjust the Values in the fields Width and Height.


## Planned Features

The planned features are in no particular order

* Adding more Image Formats 
* Adding additional Code Formats (Datamatrix, Aztec, etc.)
* Ability to choose where the barcodes will be saved (including potential subfolders)
* Creating an executable/AppImage for easier use
