<img src="https://user-images.githubusercontent.com/79027579/157531034-474a6480-1168-44fc-a7b5-d66144a8103b.png" width=30% height=30%>


# Barcode-Generator
A Python3 based Barcode Generator

## Table of contents
* [General info](#general-info)
* [Setup and Usage](#setup)
* [Planned Features](#updates)
* [Windows Executable](#windows)

## General info

![grafik](https://user-images.githubusercontent.com/79027579/157472974-50093cb0-41f5-48fe-bac9-367be0ded99c.png)
![grafik](https://user-images.githubusercontent.com/79027579/157473184-7a20c2bb-b78a-4171-a751-fbb0b2beb08b.png)
![image](https://user-images.githubusercontent.com/79027579/158069677-f8efcbfb-9cea-4fd6-b7fb-62d4231376f0.png)



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

  - Datamatrix

* Requirements:
  - PySimpleGUI
  - python-barcode
  - pylibdmtx
  - qrcode
  - opencv-python
  - numpy
  - requests
	
## Setup and Usage

Download the above mentioned libraries with pip.

* Example "pip install PySimpleGUI" or "pip3 install PySimpleGUI" depending on your version of Python.

To run the script, simply put the "barcodegen.py" file in an accessible location and open it with your terminal.

* Example $BASH: *"python3 /home/"user"/Desktop/barcodegen.py"*

<img src="https://user-images.githubusercontent.com/79027579/158082081-8406fdd6-ad65-4897-813a-c253572c77a0.gif" width="80%" height="80%" />

## Planned Features

The planned features are in no particular order

* Adding more Image Formats 
* Adding additional Code Formats (Aztec, etc.)
* Ability to choose where the barcodes will be saved (including potential subfolders)
* Ability to colour Code (Foreground and Background)
* Creating an executable/AppImage for easier use


## General info

There is now a Windows Executable (Test Build).
Just download and execute!

[Barcodegen v05.exe](https://www.dropbox.com/s/3edxh5bm2qhpdta/barcodegen%20v05.exe?raw=1)
