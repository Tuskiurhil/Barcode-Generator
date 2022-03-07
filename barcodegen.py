# Barcode Generator v0.2 for public release
#   import main functionality
#from multiprocessing.sharedctypes import Value
import PySimpleGUI as sg
from barcode import Code128 as Code128, Code39 as Code39 
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
            barcode = button(code, writer=ImageWriter())
            barcode.save(code, {"module_width":0.35, "module_height":16, "font_size": 25, "text_distance": 0.85, "quiet_zone": 0})
            #   resizing our .png to fit within our product label document
            filename = (code +'.png')
            img = cv2.imread(filename)
            res = cv2.resize(img, dsize=(int(WIDTH), int(HEIGHT)), interpolation=cv2.INTER_CUBIC)
            cv2.imwrite(filename, res)


    #   defining window colour
    sg.theme('BrownBlue')



    #   Content of the GUI
    layout = [  [sg.Text('Code128')],
                [sg.Text('Enter SKU'), sg.InputText()],
                [sg.Text('Width:'), sg.InputText('158', key='-WIDTH-')],
                [sg.Text('Height:'), sg.InputText('100', key='-HEIGHT-')],
                [sg.Radio('Code128', "SELECTION", default=True, key="-BUTTON-"), sg.Radio('Code39', "SELECTION", key="-BUTTON1-")],
                [sg.Button('Create Barcode(s)'), sg.Button('Close')] ]


    #   Creating GUI Window
    window = sg.Window('Code128', layout)
    event, values = window.read()
    WIDTH = values['-WIDTH-']
    HEIGHT = values['-HEIGHT-']


    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Close':
            break
        if event == 'Create Barcode(s)':
            if values["-BUTTON-"] == True:
                button = Code128
            elif values["-BUTTON1-"] == True:
                button = Code39
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
