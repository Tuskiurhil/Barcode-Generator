# Barcode Generator v0.25 for public release

#   import main functionality
import PySimpleGUI as sg
from barcode import (
    Code128 as code128, 
    Code39 as code39, 
    EAN8 as ean8, 
    EAN13 as ean13, 
    EAN14 as ean14, 
    JAN as jan,
    ISBN13 as isbn13,
    ISBN10 as isbn10,
    ISSN as issn,
    UPCA as upca,
    PZN as pzn,
    )
from barcode.writer import ImageWriter
import cv2
import numpy as np

def main():

        #   defining main function of creating and saving barcode image
    def createbarcode():
        target = values[0]
        print('\nCreating Barcode')
        #   SKU equals our input from before
        SKU = str(values[0])
        SKUS = SKU.split(',')
        #   this will take our input, create a barcode and save it as a .png
        for code in SKUS:
            #   "button" will be replaced by the radio selection done further below
            barcode = button(code, writer=ImageWriter())
            barcode.save(code, {"module_width":0.35, "module_height":16, "font_size": 25, "text_distance": 0.85, "quiet_zone": 0})
            #   resizing our .png to fit within our product label document
            filename = (code+'.png')
            img = cv2.imread(filename)
            #   resizing the image according to the parameters given
            res = cv2.resize(img, dsize=(int(WIDTH), int(HEIGHT)), interpolation=cv2.INTER_CUBIC)
            cv2.imwrite(filename, res)


    #   defining window colour
    sg.theme('BrownBlue')



    #   Content of the GUI, including Button Selection for which Barcode Format to use
    layout = [  [sg.Text('Barcode Generator')],
                [sg.Text('Enter SKU'), sg.InputText()],
                [sg.Text('Width:'), sg.InputText('158', key='-WIDTH-')],
                [sg.Text('Height:'), sg.InputText('100', key='-HEIGHT-')],
                
                [sg.Radio('Code128', "SELECTION", default=True, key="-BUTTON-"), 
                sg.Radio('Code39', "SELECTION", key="-BUTTON1-"),
                sg.Radio('EAN-8', "SELECTION", key="-BUTTON2-"),
                sg.Radio('EAN-13', "SELECTION", key="-BUTTON3-"),
                sg.Radio('EAN-14', "SELECTION", key="-BUTTON4-")],
                
                [sg.Radio('UPC-A', "SELECTION", key="-BUTTON5-"),
                sg.Radio('JAN', "SELECTION", key="-BUTTON6-"),
                sg.Radio('ISSN', "SELECTION", key="-BUTTON7-"),
                sg.Radio('PZN', "SELECTION", key="-BUTTON8-")],

                [sg.Radio('ISBN10', "SELECTION", key="-BUTTON9-"),
                sg.Radio('ISBN13', "SELECTION", key="-BUTTON10-")],

                [sg.Button('Create Barcode(s)'), sg.Button('Close')] ]


    #   Creating GUI Window
    window = sg.Window('Barcode Generator', layout)
    event, values = window.read()
    WIDTH = values['-WIDTH-']
    HEIGHT = values['-HEIGHT-']


    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Close':
            break
        #   if loop to check which Radio Button is active (e.g. which Barcode Format to use)
        if event == 'Create Barcode(s)':
            try:
                if values["-BUTTON-"] == True:
                    button = code128
                elif values["-BUTTON1-"] == True:
                    button = code39
                elif values["-BUTTON2-"] == True:
                    button = ean8
                elif values["-BUTTON3-"] == True:
                    button = ean13
                elif values["-BUTTON4-"] == True:
                    button = ean14
                elif values["-BUTTON5-"] == True:
                    button = upca
                elif values["-BUTTON6-"] == True:
                    button = jan
                elif values["-BUTTON7-"] == True:
                    button = issn
                elif values["-BUTTON8-"] == True:
                    button = pzn
                elif values["-BUTTON9-"] == True:
                    button = isbn10
                elif values["-BUTTON10-"] == True:
                    button = isbn13
            except ValueError as err:
                err.args = ("Invalid Image Size or Input")
            

            createbarcode()
        window.close()

        layout = [  [sg.Text('Please wait for your Barcode(s) to finish before you close this window!')],
                    [sg.Text('creating barcode(s) for...')],
                    [sg.Text(str(values[0]))],
                    [sg.Button('New Barcode(s)'), sg.Button('Close')] ]

        window = sg.Window('Code128', layout)

        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Close': 
                window.close()
                break
            if event == 'New Barcode(s)':
                window.close()
                main()



main()