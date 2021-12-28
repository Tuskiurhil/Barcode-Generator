#   import main functionality
import PySimpleGUI as sg
from barcode import Code128
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
            barcode = Code128(code, writer=ImageWriter())
            barcode.save(code, {"module_width":0.35, "module_height":16, "font_size": 25, "text_distance": 0.85, "quiet_zone": 0})
            #   resizing our .png to fit within our product label document
            filename = (code +'.png')
            img = cv2.imread(filename)
            res = cv2.resize(img, dsize=(158, 100), interpolation=cv2.INTER_CUBIC)
            cv2.imwrite(filename, res)
    #   defining window colour
    sg.theme('BrownBlue')
    #   Content of the GUI
    layout = [  [sg.Text('Code128')],
                [sg.Text('Enter SKU'), sg.InputText()],
                [sg.Button('Create Barcode(s)'), sg.Button('Close')] ]


    #   Creating GUI Window
    window = sg.Window('Code128', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Close':
            break
        if event == 'Create Barcode(s)':
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