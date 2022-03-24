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
import PIL
from pylibdmtx.pylibdmtx import encode
import cv2
import numpy as np
import time
import requests
import webbrowser
import os

IMGFORMAT = ""
EXTENSION = ""
SELTHEME = ""
code = ""

def main():

    buttonname = ""

# ____________________________________________________________________
#   --- MAIN BARCODE FUNCTION ---
#   defining main function of creating and saving barcode image
    def createbarcode():
        global code
        WIDTH = values['-WIDTH-']
        HEIGHT = values['-HEIGHT-']
        BGCOLOUR = values['-BGCOLOUR-']
        FGCOLOUR = values['-FGCOLOUR-']
        global IMGFORMAT, EXTENSION
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
            barcode.save(code+' - '+buttonname, {"module_width":0.35, "module_height":16, "font_size": 25, "text_distance": 0.85, "quiet_zone": 0, "background": BGCOLOUR, "foreground": FGCOLOUR})
#   resizing our image to fit within our product label document
            code = code.replace("\\",".")
            code = code.replace("/",".")
            code = code.replace(":",".")
            code = code.replace("*",".")
            code = code.replace("?",".")
            code = code.replace('"',".")
            code = code.replace("<",".")
            code = code.replace(">",".")
            code = code.replace("|",".")
            filename = (code+' - '+buttonname+EXTENSION)
            if values['-CHECKOUTPUT-'] == True:
                print(filename)
            img = cv2.imread(filename)
#   resizing the image according to the parameters given
            res = cv2.resize(img, dsize=(int(WIDTH), int(HEIGHT)), interpolation=cv2.INTER_CUBIC)
            cv2.imwrite(filename, res)
# ____________________________________________________________________

# ____________________________________________________________________
#   --- MAIN QR-CODE FUNCTION ---
    def createqrcode():
        #QRVERSION = values['-QRSIZE-']
        #QRBOX_SIZE = values['-QRBOXSIZE-']
        #QRBORDER = values['-QRBORDER-']
        BGCOLOUR = values['-BGCOLOUR-']
        FGCOLOUR = values['-FGCOLOUR-']
        global IMGFORMAT, EXTENSION, code
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
            #version=QRVERSION,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            #box_size=QRBOX_SIZE,
            border=1
            )
            qr.add_data(code)
            qr.make(fit=True)
            img = qr.make_image(fill_color=FGCOLOUR, back_color=BGCOLOUR)
#   Replacing the / with a dot to make sure that URL's will not break the program when saving
            code = code.replace("\\",".")
            code = code.replace("/",".")
            code = code.replace(":",".")
            code = code.replace("*",".")
            code = code.replace("?",".")
            code = code.replace('"',".")
            code = code.replace("<",".")
            code = code.replace(">",".")
            code = code.replace("|",".")
            img.save(code+EXTENSION)
# ____________________________________________________________________

#   --- MAIN DATAMATRIX FUNCTION ---
# ____________________________________________________________________
    def createdatamatrix():
        global IMGFORMAT, EXTENSION, code
        target = values[0]
        print('\nCreating Datamatrix-Code')
        SKU = str(values[0])
        SKUS = SKU.split(',')
        for code in SKUS:
            if values["-PNG-"] == True:
                IMGFORMAT = 'PNG'
                EXTENSION = '.png'
            if values["-JPEG-"] == True:
                IMGFORMAT = 'JPEG'
                EXTENSION = '.jpeg'
            if values["-BMP-"] == True:
                IMGFORMAT = 'BMP'
                EXTENSION = '.bmp'
            if values["-GIF-"] == True:
                IMGFORMAT = 'GIF'
                EXTENSION = '.gif'
            if values['-CHECKOUTPUT-'] == True:
                print(code+EXTENSION)
#   Datamatrix Creation
#   The input needs to be formated to utf-8, otherwise the output will be a garbled mess
        encodedmatrix = encode(code.encode('utf-8'))
        encodedimg = Image.frombytes('RGB', (encodedmatrix.width, encodedmatrix.height), encodedmatrix.pixels)
        code = code.replace("\\",".")
        code = code.replace("/",".")
        code = code.replace(":",".")
        code = code.replace("*",".")
        code = code.replace("?",".")
        code = code.replace('"',".")
        code = code.replace("<",".")
        code = code.replace(">",".")
        code = code.replace("|",".")
        encodedimg.save(code+EXTENSION)
# ____________________________________________________________________

# ____________________________________________________________________
#   Main Settings Function
    def savesettings():
        global SELTHEME
        global selectedtheme
        if values["-THEME1-"] == True:
            with open("bcgsettings.txt", "w") as bcgsettings:
                bcgsettings.write('BrownBlue')
                bcgsettings.close
        elif values["-THEME2-"] == True:
            with open("bcgsettings.txt", "w") as bcgsettings:
                bcgsettings.write('LightYellow')
                bcgsettings.close
        elif values["-THEME3-"] == True:
            with open("bcgsettings.txt", "w") as bcgsettings:
                bcgsettings.write('BrightColors')
                bcgsettings.close
        elif values["-THEME4-"] == True:
            with open("bcgsettings.txt", "w") as bcgsettings:
                bcgsettings.write('DarkAmber')
                bcgsettings.close
        elif values["-THEME5-"] == True:
            with open("bcgsettings.txt", "w") as bcgsettings:
                bcgsettings.write('SystemDefault1')
                bcgsettings.close
        elif values["-THEME6-"] == True:
            with open("bcgsettings.txt", "w") as bcgsettings:
                bcgsettings.write('Topanga')
                bcgsettings.close

# ____________________________________________________________________

#   Content of the GUI, including Button Selection for which Barcode Format to use

#   User has chosen to create a QR Code
    layoutQR = [  
        [sg.Text('QR-Code Generator')],
        [sg.Text('Enter Data'), sg.InputText()],
        #[sg.Text('Size (1-40)'), sg.InputText('1', key='-QRSIZE-')],
        #[sg.Text('Box Size'), sg.InputText('10', key='-QRBOXSIZE-')],
        #[sg.Text('Border'), sg.InputText('1', key='-QRBORDER-')],
        [sg.Text('Foreground Colour:'), sg.InputText('#000000', key='-FGCOLOUR-'), sg.ColorChooserButton(button_text = "Select colour", target='-FGCOLOUR-')],
        [sg.Text('Background Colour:'), sg.InputText('#FFFFFF', key='-BGCOLOUR-'), sg.ColorChooserButton(button_text = "Select colour", target='-BGCOLOUR-')],

        [sg.Radio('PNG', "IMGFORMAT", default=True, key="-PNG-"),
        #sg.Radio('JPEG', "IMGFORMAT", key="-JPEG-"),
        sg.Radio('BMP', "IMGFORMAT", key="-BMP-")],

        [sg.Radio('QR', "SELECTION", key="-BUTTON11-", default=True)],
        #sg.Radio('DATAMATRIX', "SELECTION", key="-BUTTON12-")],

        [sg.Checkbox('Print Output to Console', default=False, key='-CHECKOUTPUT-')],

        [sg.Button('Create Barcode(s)'), sg.Button('Close')] ]

#   User has chosen to create a Datamatrix Code
    layoutDATAMATRIX = [  
        [sg.Text('Datamatrix Code Generator')],
        [sg.Text('Enter Data'), sg.InputText()],
        #[sg.Text('Size (1-40)'), sg.InputText('1', key='-QRSIZE-')],
        #[sg.Text('Box Size'), sg.InputText('10', key='-QRBOXSIZE-')],
        #[sg.Text('Border'), sg.InputText('1', key='-QRBORDER-')],

        [sg.Radio('PNG', "IMGFORMAT", default=True, key="-PNG-"),
        sg.Radio('JPEG', "IMGFORMAT", key="-JPEG-"),
        sg.Radio('BMP', "IMGFORMAT", key="-BMP-"),
        sg.Radio('GIF', "IMGFORMAT", key="-GIF-")],

        [sg.Radio('DATAMATRIX', "SELECTION", key="-BUTTON12-", default=True)],

        [sg.Checkbox('Print Output to Console', default=False, key='-CHECKOUTPUT-')],

        [sg.Button('Create Barcode(s)'), sg.Button('Close')] ]

#   User has chosen to create a Barcode
    layoutBARCODE = [  
        [sg.Text('Barcode Generator')],
        [sg.Text('Enter SKU'), sg.InputText()],
        [sg.Text('Width:'), sg.InputText('326', key='-WIDTH-')],
        [sg.Text('Height:'), sg.InputText('274', key='-HEIGHT-')],
        [sg.Text('Foreground Colour:'), sg.InputText('#000000', key='-FGCOLOUR-'), sg.ColorChooserButton(button_text = "Select colour", target='-FGCOLOUR-')],
        [sg.Text('Background Colour:'), sg.InputText('#FFFFFF', key='-BGCOLOUR-'), sg.ColorChooserButton(button_text = "Select colour", target='-BGCOLOUR-')],
        #[sg.In("", visible=True, enable_events=True, key='set_line_color'),
        #   sg.ColorChooserButton("TEST", size=(1, 1), target='set_line_color', button_color=('#1f77b4', '#1f77b4'),
        #                         border_width=1, key='set_line_color_chooser')]

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

#   User has chosen to change Settings
    layoutSETTINGS = [  
        [sg.Text('Settings:')],
        # [sg.Text('Enter SKU'), sg.InputText()],
        # [sg.Text('Width:'), sg.InputText('326', key='-WIDTH-')],
        # [sg.Text('Height:'), sg.InputText('274', key='-HEIGHT-')],

        [sg.Radio('BrownBlue', "THEME", default=True, key="-THEME1-"),
        sg.Radio('LightYellow', "THEME", key="-THEME2-"),
        sg.Radio('BrightColors', "THEME", key="-THEME3-"),
        sg.Radio('DarkAmber', "THEME", key="-THEME4-"),
        sg.Radio('SystemDefault1', "THEME", key="-THEME5-"),
        sg.Radio('Topanga', "THEME", key="-THEME6-")],
        #sg.Radio('BMP', "THEME", key="-BMP-")],
        
        #[sg.Checkbox('Print Output to Console', default=False, key='-CHECKOUTPUT-')],

        [sg.Button('Save & Exit'), sg.Button('Close')] ]
        
    if BARCODESELECTION == 1:
            window = sg.Window('Barcode Generator', layoutBARCODE)
            event, values = window.read()
    elif QRCODESELECTION == 1:
            window = sg.Window('Barcode Generator', layoutQR)
            event, values = window.read()
    elif DATAMATRIXSELECTION == 1:
            window = sg.Window('Barcode Generator', layoutDATAMATRIX)
            event, values = window.read()
    elif SETTINGSSELECTION == 1:
        window = sg.Window('Barcode Generator', layoutSETTINGS)
        event, values = window.read()

#   Creating GUI Window
    while True:
        event, values = window.read()
        if event == 'set_line_color':
            window['set_line_color_chooser'].Update(button_color=(values[event], values[event]))
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
                #if code == "":
                #    [sg.popup_error('Invalid Image Size or Input')]
                #    window.close()
                #    start()
                #elif code != "":
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
                    elif DATAMATRIXSELECTION == 1:
                            if values["-BUTTON12-"] == True:
                                createdatamatrix()
            except ValueError as err:
                err.args = ("Invalid Image Size or Input")
#   When hitting "Save & Exit" the program will write the selected Theme to the settings file and then tell the user to restart the application. The program will close automatically.
        elif event == 'Save & Exit':
            try:
                if SETTINGSSELECTION == 1:
                        if values["-THEME1-"] == True:
                            savesettings()
                            [sg.Popup("Saving Settings. Please restart the Application")]
                            break
                        elif values["-THEME2-"] == True:
                            savesettings()
                            [sg.Popup("Saving Settings. Please restart the Application")]
                            break
                        elif values["-THEME3-"] == True:
                            savesettings()
                            [sg.Popup("Saving Settings. Please restart the Application")]
                            break
                        elif values["-THEME4-"] == True:
                            savesettings()
                            [sg.Popup("Saving Settings. Please restart the Application")]
                            break
                        elif values["-THEME5-"] == True:
                            savesettings()
                            [sg.Popup("Saving Settings. Please restart the Application")]
                            break
                        elif values["-THEME6-"] == True:
                            savesettings()
                            [sg.Popup("Saving Settings. Please restart the Application")]
                            break
            except ValueError as err:
                err.args = ("Invalid Image Size or Input")
            
        window.close()

        layoutcreatecode = [  [sg.Text('Please wait for your Barcode(s) to finish before you close this window!')],
                    [sg.Text('creating barcode(s) for...')],
                   [sg.Text(str(values[0]))],
                    [sg.Button('New Barcode(s)'), sg.Button('Close')] ]

        if BARCODESELECTION == 1:
            window = sg.Window(buttonname, layoutcreatecode)
        elif QRCODESELECTION == 1:
            window = sg.Window(buttonname, layoutcreatecode)
        elif DATAMATRIXSELECTION == 1:
            window = sg.Window(buttonname, layoutcreatecode)
        # elif SETTINGSSELECTION == 1:
        #     window = sg.Window(buttonname, layoutsavesettings)'



        #window = sg.Window(buttonname, layoutcreatecode)

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

updating = 0
#   ******** IMPORTANT ********
#   Version Number of current script, don't forget to change after updating, otherwise Script Update functionality might not work
versionnr = 'v0.6'
#   ******** IMPORTANT ********

def start():
    global updating
#   LAYOUT LISTS
#   Selection changes depending on wether or not the Version in use is up to date.
#   An Update for the Script was found
    layout1 = [  
        [sg.Text('- Choose your desired Code Type -'),
        [sg.Button('Update Available!')],
        [sg.Radio('BAR - CODE', "SELECTION", default=True, key="-BARCODES-")],

        [sg.Radio('QR - CODE', "SELECTION", key="-QRCODES-")],

        [sg.Radio('Datamatrix', "SELECTION", key="-DATAMATRIX-")],

        [sg.Radio('Settings', "SELECTION", key="-SETTINGS-")],

        [sg.Button('Continue'), sg.Button('Close')] ]]

#   No Update or no Internet Connection
    layout2 = [  
        [sg.Text('- Choose your desired Code Type -'),
        [sg.Radio('BAR - CODE', "SELECTION", default=True, key="-BARCODES-")],
        
        [sg.Radio('QR - CODE', "SELECTION", key="-QRCODES-")],

        [sg.Radio('Datamatrix', "SELECTION", key="-DATAMATRIX-")],

        [sg.Radio('Settings', "SELECTION", key="-SETTINGS-")],

        [sg.Button('Continue'), sg.Button('Close')] ]]

#   Grabbing latest version number from the github repo

#   Check if connection to internet is active (For update checking only!)
    timeout = 1
    



    global BARCODESELECTION
    global QRCODESELECTION
    global DATAMATRIXSELECTION
    global SETTINGSSELECTION
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
                DATAMATRIXSELECTION = 0
                window.close()
                main()
            elif values['-QRCODES-'] == True:
                QRCODESELECTION = 1
                BARCODESELECTION = 0
                DATAMATRIXSELECTION = 0
                window.close()
                main()
            elif values['-DATAMATRIX-'] == True:
                QRCODESELECTION = 0
                BARCODESELECTION = 0
                DATAMATRIXSELECTION = 1
                window.close()
                main()
            elif values['-SETTINGS-'] == True:
                QRCODESELECTION = 0
                BARCODESELECTION = 0
                DATAMATRIXSELECTION = 0
                SETTINGSSELECTION = 1
                window.close()
                main()
        if event == 'Update Available!':
            latestrelease = 'https://github.com/ColditzColligula/Barcode-Generator/releases'
            webbrowser.open(latestrelease)
            break


#   declaring name of Settingsfile and checking if filepath exists
settingsfile = "bcgsettings.txt"
isFile = os.path.isfile(settingsfile)
#print(isFile)

#   Checking if Settingsfile can be found.
#       when file not found > create with standard theme > read > start
if isFile == False:
    with open("bcgsettings.txt", "w") as bcgsettings:
        bcgsettings.write("BrownBlue")
        bcgsettings.close
    with open("bcgsettings.txt", "r") as bcgsettings:
        settingstheme = bcgsettings.read()
        bcgsettings.close
#       when file found > read settings > start
elif isFile == True:
    with open("bcgsettings.txt", "r") as bcgsettings:
        global selectedtheme
        settingstheme = bcgsettings.read()
        print(settingstheme)
        bcgsettings.close

#   defining window colour/theme
selectedtheme = settingstheme
sg.theme(selectedtheme)

start()