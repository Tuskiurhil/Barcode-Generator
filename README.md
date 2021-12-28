# Barcode-Generator
A Python3 based Barcode Generator

## Table of contents
* [General info](#general-info)
* [Setup and Usage](#setup)
* [Planned Features](#updates)

## General info
Barcode-Generator is a **PythonScript** that takes a Value, formats it to a string and turns it into a Barcode

* Current Support:
  -  Code128

* Requirements:
  - PySimpleGUI
  - python-barcode
  - opencv-python
  - numpy
	
## Setup and Usage

Download the above mentioned libraries with pip.

* Example "pip install PySimpleGUI" or "pip3 install PySimpleGUI" depending on your version of Python.

To run the script, simply put the "code128.py" file in an accessible location and open it with your terminal.

* Example $BASH: *"python3 /home/"user"/Desktop/code128.py"*

Then just input your Value (eg. "12345"), hit "Create Barcode" and the Script will create a .png file of your barcode.
If you require the Barcode to be a different size, feel free to edit the code.

Change the following lines:
{"module_width":0.35, "module_height":16, "font_size": 25, "text_distance": 0.85, "quiet_zone": 0})

and

dsize=(158,100) on line 34 where X, Y is the width and height of the final image.

## Planned Features

The planned features are in no particular order

* Ability to select which Barcode Format to use
* Ability to select desired resolution of output barcode
