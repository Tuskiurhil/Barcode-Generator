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

1.A window will pop-up allowing you to select which type of code you want to create.

![image](https://user-images.githubusercontent.com/79027579/158079492-96933cb2-1848-474f-a213-c638dca6c8fa.png)

2.Make the necessary selections in the following Window (Entering Data/SKU, Choosing Width/Height, Choosing Filetype, etc.).

![image](https://user-images.githubusercontent.com/79027579/158079576-5f279f92-8adb-4378-b661-3bb8d559d351.png)

3.Click on "Create Barcode(s)". 

![image](https://user-images.githubusercontent.com/79027579/158079587-f1ec82fc-412d-4e2c-9c21-9c7fdd4a67dd.png)

4.Your Barcodes will be created and saved in the same folder where the .py file is located.

![image](https://user-images.githubusercontent.com/79027579/158079600-c1c88672-7057-4c65-a724-a23a36fa03fa.png)




## Planned Features

The planned features are in no particular order

* Adding more Image Formats 
* Adding additional Code Formats (Aztec, etc.)
* Ability to choose where the barcodes will be saved (including potential subfolders)
* Ability to colour Code (Foreground and Background)
* Creating an executable/AppImage for easier use
