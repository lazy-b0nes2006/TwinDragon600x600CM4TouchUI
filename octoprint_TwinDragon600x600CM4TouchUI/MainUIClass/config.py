from PyQt5 import QtCore
from collections import OrderedDict

Development = True   # set to True if running on any system other than RaspberryPi

# TODO:
'''
# Remove SD card capability from octoprint settings
# Should add error/status checking in the response in some functions in the octoprintAPI
# session keys??
# printer status should show errors from printer.
# async requests
# http://eli.thegreenplace.net/2011/04/25/passing-extra-arguments-to-pyqt-slot
# fix wifi
# status bar netweorking and wifi stuff
# reconnect to printer using GUI
# check if disk is getting full
# recheck for internet being conneted, refresh button
# load filaments from a file
# store settings to a file
# change the way active extruder print stores the current active extruder using positionEvent
#settings should show the current wifi
#clean up keyboard nameing
#add asertions and exeptions
#disaable done button if empty
#oncancel change filament cooldown
#toggle temperature indipendant of motion
#get active extruder from motion controller. when pausing, note down and resume with active extruder
#QR code has dictionary with IP address also
Testing:
# handle nothing selected in file select menus when deleting and printing etc.
# Delete items from local and USB
# different file list pages for local and USB
# test USB/Local properly
# check for uploading error when uploading from USB
# Test if active extruder goes back after pausing
# TRy to fuck with printing process from GUI
# PNG Handaling
# dissable buttons while printing
'''

ip = '192.168.0.20'
apiKey = 'B508534ED20348F090B4D0AD637D3660'
file_name = ''
filaments = [
                ("PLA", 220),
                ("ABS", 240),
                ("PETG", 240),
                ("PVA", 230),
                ("TPU", 240),
                ("Nylon", 250),
                ("PolyCarbonate", 265),
                ("HIPS", 240),
                ("WoodFill", 220),
                ("CopperFill", 200),
                ("Breakaway", 240)
]

filaments = OrderedDict(filaments)

calibrationPosition = {'X1': 42, 'Y1': 21,
                       'X2': 174, 'Y2': 21,
                       'X3': 108, 'Y3': 195
                       }

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s
