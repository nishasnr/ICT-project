"""
mainwindow.py has the MainWindow class and defines the startMainMenu and startStallMenu functions.

Criteria Fulfilled:
- Program Organization
- Programming Style
- Program Correctness
"""

from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QImage, QPalette, QBrush
from PyQt5.QtCore import QSize
from functools import partial
import sys
import mainmenu as main_menu
import stall_menu
import app_data as info

class MainWindow(QMainWindow):
    # By Kyaw and Nisha
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        # Background Image
        self.setGeometry(50, 50, 400, 450)
        self.setFixedSize(592, 808)
        oImage = QImage("icons/background.jpg")
        sImage = oImage.scaled(QSize(592,808))
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))                    
        self.setPalette(palette)

        # Start the Main Menu
        self.startMainMenu()

    # startStallMenu is called when a stall's button is clicked on the GUI. 
    # This function will then get the necessary information and open up the Stall Menu GUI.
    def startStallMenu(self,name):
        # By Kyaw
        self.name = name
        self.StallMenu = stall_menu.StallMenu(self.Window,name)
        
        self.setWindowTitle(info.stalls[name]+" Menu")
        self.setCentralWidget(self.StallMenu)
        self.StallMenu.backButton.clicked.connect(self.startMainMenu)
        self.show()

    # startMainMenu is called when the application first starts up 
    #and whenever the back button on the Stall Menu is clicked
    def startMainMenu(self):
        # By Nisha
        self.Window = main_menu.MainMenu(self)
        self.setWindowTitle("North Spine Food Explorer")
        self.setCentralWidget(self.Window)
        for x in range(25):
            self.Window.btn[x].clicked.connect(partial(self.startStallMenu, info.stalls_list[x]))
        # If time has been set by user, then don't run live timer, just show the user-set time.
        # But if it's not, it will throw an error, which we want to avoid, so just do nothing for the error
        try:
            if "Set Time: " in self.StallMenu.time_label.text():
                self.Window.timer.stop()
                self.Window.time_label.setText(self.StallMenu.time_label.text())          
        except:
            pass
        self.show()


