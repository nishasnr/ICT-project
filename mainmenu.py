"""
mainmenu.py is the landing page's GUI layout and related functions/buttons

Criteria Fulfilled:
-Program organization
-Programming style
-Interface Design
"""

from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QGridLayout, QMainWindow, QLineEdit
from PyQt5.QtCore import QSize, QDateTime, QRect, QTimer
from PyQt5.QtGui import QPixmap, QIcon, QFont
from functools import partial
import app_data as ad
import timesetterobj as ts
import pandas as  pd


class MainMenu(QWidget):
    # By Kyaw and Nisha
    def __init__(self, parent=None):
        super(MainMenu, self).__init__(parent)

        self.centralwidget = QWidget(self)
        
        """
        Date and Time Buttons
        """

        # Create time_label object
        font = QFont()
        font.setPointSize(10)
        self.time_label = QLabel(self)
        self.time_label.setFont(font)
        self.time_label.setGeometry(QRect(10,0,250,35))        
        self.time_label.setScaledContents(True)

        # Create timer object that will run every half a second to update the time_label to the current computer time.
        self.timer = QTimer(self)
        self.timer.timeout.connect(lambda: self.time_label.setText(QDateTime.currentDateTime().toString('yyyy-MM-dd hh:mm:ss')))
        self.timer.start(500)
               
        # Create set_time_button to enable user to set time. Upon clicking the button, time_setting function will execute
        self.set_time_button = QPushButton(self)
        self.set_time_button.setGeometry(500,0,93,28)
        self.set_time_button.setText("Set Time")
        self.set_time_button.clicked.connect(self.time_setting)

        # Create reset_time_button to enable user to reset the time to live computer time upon clicking the button.
        # Lambda function used as the function is just to start the timer again which was stopped earlier due to time_setting function
        # Nothing happens if self.timer is not stopped in the first place, since it will just make the starting timer start again.
        self.reset_time_button = QPushButton(self)
        self.reset_time_button.setGeometry(400,0,93,28)
        self.reset_time_button.setText("Reset Time")
        self.reset_time_button.clicked.connect(lambda: self.timer.start())

        """
        Main Logo and Review System
        """

        self.mainlogo = QLabel(self.centralwidget)
        self.mainlogo.setGeometry(QRect(160, 40, 291, 111))
        self.mainlogo.setToolTipDuration(0)
        self.mainlogo.setPixmap(QPixmap("icons/logo.png"))
        self.mainlogo.setScaledContents(True)

        """
        Stall Buttons
        """

        # Grid Layout Widget for the stall buttons, 
        # so that all are properly spaced out and formatted uniformly
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QRect(0, 190, 591, 621))
        
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)

        # Stall Buttons
        # Store the buttons in a list, with each button having specific attributes.
        self.btn=[]
        for y in range(5):
            for x in range(5):
                self.btn.append(x)

                # Stall button creation and sizing
                self.btn[y*5+x]= QPushButton(self.gridLayoutWidget)
                self.btn[y*5+x].setMinimumSize(QSize(111, 111))
                self.btn[y*5+x].setText("")

                # Stall button icon formatting, so that the icon covers the whole button
                icon = QIcon()
                icon.addPixmap(QPixmap("./icons/"+ad.stalls_list[y*5+x]+".png"))
                self.btn[y*5+x].setIcon(icon)
                self.btn[y*5+x].setIconSize(QSize(111, 111))
                self.btn[y*5+x].setStyleSheet("border: none;")

                # Adds the stall button to the grid layout
                self.gridLayout.addWidget(self.btn[y*5+x], y, x, 1, 1)

    # time_setting function to create a TimeSetter object and shows it on screen
    # the try-except-else block is used to ensure that only one instance of the window opens.
    # it will first try to show the window if it already exists. If it does not, then handle it by making the window and showing it.
    def time_setting(self):
        # By Kyaw
        try: 
            self.TimeSetter.show()
        except:
            self.TimeSetter = ts.TimeSetter(self)
            self.TimeSetter.show()

