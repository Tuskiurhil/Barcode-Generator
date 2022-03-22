<img src="https://user-images.githubusercontent.com/79027579/157531034-474a6480-1168-44fc-a7b5-d66144a8103b.png" width=30% height=30%>


![image](https://img.shields.io/github/v/release/ColditzColligula/Barcode-Generator?color=green&label=Version&logo=Python&logoColor=yellow)
![image](https://img.shields.io/github/last-commit/ColditzColligula/Barcode-Generator?color=blue&label=Last%20Update)
![image](https://img.shields.io/github/languages/code-size/ColditzColligula/Barcode-Generator?color=yellow&label=Code%20Size)
![image](https://img.shields.io/github/license/ColditzColligula/Barcode-Generator?color=orange&label=License)
![image](https://img.shields.io/github/downloads/ColditzColligula/Barcode-Generator/total?color=cyan&label=Downloads)
***
# Barcode-Generator
A Python3 based **Barcode**, **QR-Code** and **DataMatrix** Generator
(Now with a Windows Executable too!)

## Table of contents
* [General info](#general-info)
* [Windows Executable](#windows-executable)
* [Setup and Usage](#setup-and-Usage)
* [Planned Features](#planned-features)
* [Known Bugs](#known-bugs)

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

## Windows Executable

There is now a Windows Executable (Test Build).
Just download and execute! (initial start up is slow)

[Barcodegen v05.exe](https://www.dropbox.com/s/3edxh5bm2qhpdta/barcodegen%20v05.exe?raw=1)
	
## Setup and Usage

**The Script was tested on Ubuntu, Debian, Arch and Microsoft Windows 10.**

1. Open a Terminal or CMD/PowerShell

2. Download the above mentioned libraries with pip.

* Example "pip install PySimpleGUI" or "pip3 install PySimpleGUI" depending on your version of Python.

3. Put the script (barcodegen.py) in a location of choice, open a Terminal or CMD/PowerShell in that location and execute it. (alternatively you can point to the file)

* Example $BASH: *"python3 /home/"user"/Desktop/barcodegen.py"*
* Example CMD/Powershell: *"python3 C:\Users\"user"\Desktop\Barcode\barcodegen.py"*

4. Create some Barcodes!


**Preview GIF**

<img src="https://user-images.githubusercontent.com/79027579/158082081-8406fdd6-ad65-4897-813a-c253572c77a0.gif" width="80%" height="80%" />


## Known Bugs
- ~~Using forbidden characters like \ / : * ? " < > | will crash the program~~ (fixed in v0.55)
- Some Barcode Formats will give a Traceback if an invalid Barcode has been entered in the Data field (Clarification required)

## Planned Features

The planned features are in no particular order

* Actual working Progress-Bar that automatically closes when creation of codes is done
* Adding more Image Formats 
* Adding additional Code Formats (Aztec, etc.)
* Ability to choose where the barcodes will be saved (including potential subfolders)
* Ability to colour Code (Foreground and Background)
* Ability to specify which character will split the input (e.g. ; , . , - , / , etc.) Default is ,
* Creating an executable/AppImage for easier use [(Windows Version is now Available! outdated)](https://www.dropbox.com/s/3edxh5bm2qhpdta/barcodegen%20v05.exe?raw=1)
