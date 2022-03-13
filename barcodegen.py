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
import qrcode
import cv2
import numpy as np
import time
import requests
import webbrowser

IMGFORMAT = ""
EXTENSION = ""

def main():

    buttonname = ""

#   --- MAIN BARCODE FUNCTION ---
#   defining main function of creating and saving barcode image
    def createbarcode():
        WIDTH = values['-WIDTH-']
        HEIGHT = values['-HEIGHT-']
        global IMGFORMAT
        global EXTENSION
        target = values[0]
        print('\nCreating Barcode')
#   SKU equals our input from before
        SKU = str(values[0])
        SKUS = SKU.split(',')
#   this will take our input, create a barcode and save it as an image
        for code in SKUS:

            if values["-PNG-"] == True:
                IMGFORMAT = 'PNG'
                EXTENSION = '.png'
            elif values["-JPEG-"] == True:
                IMGFORMAT = 'JPEG'
                EXTENSION = '.jpeg'
            elif values["-BMP-"] == True:
                IMGFORMAT = 'BMP'
                EXTENSION = '.bmp'
#   "button" will be replaced by the radio selection done further below     
            barcode = button(code, writer=ImageWriter(IMGFORMAT))
            barcode.save(code+' - '+buttonname, {"module_width":0.35, "module_height":16, "font_size": 25, "text_distance": 0.85, "quiet_zone": 0})
#   resizing our image to fit within our product label document
            filename = (code+' - '+buttonname+EXTENSION)
            if values['-CHECKOUTPUT-'] == True:
                print(filename)
            img = cv2.imread(filename)
#   resizing the image according to the parameters given
            res = cv2.resize(img, dsize=(int(WIDTH), int(HEIGHT)), interpolation=cv2.INTER_CUBIC)
            cv2.imwrite(filename, res)


#   --- MAIN QR-CODE FUNCTION ---
    def createqrcode():
        QRVERSION = values['-QRSIZE-']
        QRBOX_SIZE = values['-QRBOXSIZE-']
        QRBORDER = values['-QRBORDER-']
        global IMGFORMAT
        global EXTENSION
        target = values[0]
        print('\nCreating QR-Code')
        SKU = str(values[0])
        SKUS = SKU.split(',')
        for code in SKUS:
            if values["-PNG-"] == True:
                IMGFORMAT = 'PNG'
                EXTENSION = '.png'
            elif values["-JPEG-"] == True:
                window.close()
                sg.popup_error('JPEG is not supported for QR-Codes!')
                start()
                #IMGFORMAT = 'JPEG'
                #EXTENSION = '.jpeg'
            elif values["-BMP-"] == True:
                IMGFORMAT = 'BMP'
                EXTENSION = '.bmp'

            if values['-CHECKOUTPUT-'] == True:
                print(code+EXTENSION)
#   QR Creation
            qr = qrcode.QRCode(
            version=QRVERSION,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=QRBOX_SIZE,
            border=QRBORDER,
            )
            qr.add_data(code)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")
#   Replacing the / with a dot to make sure that URL's will not break the program when saving
            code = code.replace("/",".")
            img.save(code+EXTENSION)
            

#   Content of the GUI, including Button Selection for which Barcode Format to use
#   Selection changes depending on wether or not the Version in use is up to date.

#   User has chosen to create a QR Code
    layoutQR = [  
        [sg.Text('QR-Code Generator')],
        [sg.Text('Enter Data'), sg.InputText()],
        [sg.Text('Size (1-40)'), sg.InputText('1', key='-QRSIZE-')],
        [sg.Text('Box Size'), sg.InputText('10', key='-QRBOXSIZE-')],
        [sg.Text('Border'), sg.InputText('1', key='-QRBORDER-')],

        [sg.Radio('PNG', "IMGFORMAT", default=True, key="-PNG-"),
        sg.Radio('JPEG', "IMGFORMAT", key="-JPEG-"),
        sg.Radio('BMP', "IMGFORMAT", key="-BMP-")],

        [sg.Radio('QR', "SELECTION", key="-BUTTON11-", default=True)],
        #sg.Radio('DATAMATRIX', "SELECTION", key="-BUTTON12-")],

        [sg.Checkbox('Print Output to Console', default=False, key='-CHECKOUTPUT-')],

        [sg.Button('Create Barcode(s)'), sg.Button('Close')] ]

#   User has chosen to create a Barcode
    layoutBARCODE = [  
        [sg.Text('Barcode Generator')],
        [sg.Text('Enter SKU'), sg.InputText()],
        [sg.Text('Width:'), sg.InputText('326', key='-WIDTH-')],
        [sg.Text('Height:'), sg.InputText('274', key='-HEIGHT-')],

        [sg.Radio('PNG', "IMGFORMAT", default=True, key="-PNG-"),
        sg.Radio('JPEG', "IMGFORMAT", key="-JPEG-"),
        sg.Radio('BMP', "IMGFORMAT", key="-BMP-")],
            
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
        
        [sg.Checkbox('Print Output to Console', default=False, key='-CHECKOUTPUT-')],

        [sg.Button('Create Barcode(s)'), sg.Button('Close')] ]
        
    if BARCODESELECTION == 1:
            window = sg.Window('Barcode Generator', layoutBARCODE)
            event, values = window.read()
    elif QRCODESELECTION == 1:
            window = sg.Window('Barcode Generator', layoutQR)
            event, values = window.read()

#   Creating GUI Window
    while True:
        event, values = window.read()
        if event == 'Update Available!':
            latestrelease = 'https://github.com/ColditzColligula/Barcode-Generator/releases'
            webbrowser.open(latestrelease)
            break
        if event == sg.WIN_CLOSED or event == 'Close':
            break
#   if loop to check which Radio Button is active (e.g. which Barcode Format to use)
#   Making sure to only activate the necessary buttons. Having unused buttons active will crash the program!
        if event == 'Create Barcode(s)':
            try:
                if BARCODESELECTION == 1:
                    if values["-BUTTON-"] == True:
                        button = code128
                        buttonname = 'code128'
                        createbarcode()
                    elif values["-BUTTON1-"] == True:
                        button = code39
                        buttonname = 'code39'
                        createbarcode()
                    elif values["-BUTTON2-"] == True:
                        button = ean8
                        buttonname = 'ean8'
                        createbarcode()
                    elif values["-BUTTON3-"] == True:
                        button = ean13
                        buttonname = 'ean13'
                        createbarcode()
                    elif values["-BUTTON4-"] == True:
                        button = ean14
                        buttonname = 'ean14'
                        createbarcode()
                    elif values["-BUTTON5-"] == True:
                        button = upca
                        buttonname = 'upca'
                        createbarcode()
                    elif values["-BUTTON6-"] == True:
                        button = jan
                        buttonname = 'jan'
                        createbarcode()
                    elif values["-BUTTON7-"] == True:
                        button = issn
                        buttonname = 'issn'
                        createbarcode()
                    elif values["-BUTTON8-"] == True:
                        button = pzn
                        buttonname = 'pzn'
                        createbarcode()
                    elif values["-BUTTON9-"] == True:
                        button = isbn10
                        buttonname = 'isbn10'
                        createbarcode()
                    elif values["-BUTTON10-"] == True:
                        button = isbn13
                        buttonname = 'isbn13'
                        createbarcode()
                elif QRCODESELECTION == 1:
                        if values["-BUTTON11-"] == True:
                            createqrcode()
            except ValueError as err:
                err.args = ("Invalid Image Size or Input")
            
        window.close()

        layout = [  [sg.Text('Please wait for your Barcode(s) to finish before you close this window!')],
                    [sg.Text('creating barcode(s) for...')],
                    [sg.Text(str(values[0]))],
                    [sg.Button('New Barcode(s)'), sg.Button('Close')] ]

        window = sg.Window(buttonname, layout)

        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Close': 
                window.close()
                break
            if event == 'New Barcode(s)':
                window.close()
                start()



response = requests.get("https://api.github.com/repos/ColditzColligula/Barcode-Generator/releases/latest")

def checkforupdate():
    global updating
    global versionnr
    if versionnr != response.json()["name"]:
        updating = 1

#   ******** IMPORTANT ********
#   Version Number of current script, don't forget to change after updating, otherwise Script Update functionality might not work
updating = 0
versionnr = 'v0.4'
#   ******** IMPORTANT ********

def start():
    global updating
#   LAYOUT LISTS
#   An Update for the Script was found
    layout1 = [  
        [sg.Text('- Choose your desired Code Type -'),
        [sg.Button('Update Available!')],
        [sg.Radio('BAR - CODE', "SELECTION", default=True, key="-BARCODES-"),
        sg.Radio('QR - CODE', "SELECTION", key="-QRCODES-")],
        [sg.Button('Continue'), sg.Button('Close')] ]]

#   No Update or no Internet Connection
    layout2 = [  
        [sg.Text('- Choose your desired Code Type -'),
        [sg.Radio('BAR - CODE', "SELECTION", default=True, key="-BARCODES-"),
        sg.Radio('QR - CODE', "SELECTION", key="-QRCODES-")],
        [sg.Button('Continue'), sg.Button('Close')] ]]



#   defining window colour
    sg.theme('BrownBlue')

#   Grabbing latest version number from the github repo

#   Check if connection to internet is active (For update checking only!)
    timeout = 1
    



    global BARCODESELECTION
    global QRCODESELECTION
#   This will grab the Name of the current release from the github repo (eg. v0.3) and compare it to the version number defined further above
#   ... if the version numbers don't match the Main Menu Screen will show an "Update Available!" Button that when pressed will bring the
#   ... user to the latest release page on Github using their default Webbrowser.
    try:
        global response
        requests.head("http://github.com/", timeout=timeout)
        #print('Internet Connection Active: Checking for Updates...')
        response = requests.get("https://api.github.com/repos/ColditzColligula/Barcode-Generator/releases/latest")
        # print(response.json()["name"])
        # print(versionnr)
        checkforupdate()
    except:
        #print("No Internet Connection: Can't check for Updates...")
        updating = 0


    if updating == 1:
        window = sg.Window('Barcode Generator', layout1)
        event, values = window.read()
    elif updating == 0:
        window = sg.Window('Barcode Generator', layout2)
        event, values = window.read()

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Close':
            break
        if event == 'Continue':
            if values["-BARCODES-"] == True:
                BARCODESELECTION = 1
                QRCODESELECTION = 0
                window.close()
                main()
            elif values['-QRCODES-'] == True:
                QRCODESELECTION = 1
                BARCODESELECTION = 0
                window.close()
                main()
        if event == 'Update Available!':
            latestrelease = 'https://github.com/ColditzColligula/Barcode-Generator/releases'
            webbrowser.open(latestrelease)
            break

start()