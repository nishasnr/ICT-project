"""
timesetterobj.py handles the time setting window and functions.

Criteria Fulfilled:
- Feature D
- Programming Style
- Program Organisation
- Program Correctness
- String Methods
- Exception Handling
"""
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QLineEdit, QLabel, QPushButton
from PyQt5.QtGui import QFont, QPalette, QImage, QBrush
from PyQt5.QtCore import QRect, QSize
from functools import partial
import sys
from dateutil.parser import parse

class TimeSetter(QMainWindow):
    # By Kyaw
    def __init__(self,parent):
        # Have Window (MainMenu object) as a parent so that we can refer to objects and values stored in it
        self.parent = parent
        super().__init__()

        # Title and window size
        self.setWindowTitle("Set Date and Time")
        self.setFixedSize(643,261)
        oImage = QImage("icons/background.jpg")
        sImage = oImage.scaled(QSize(643,261))
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))                    
        self.setPalette(palette)


        # Set default font size
        font = QFont()
        font.setPointSize(10)

        # Main Title
        self.main_title = QLabel(self)
        self.main_title.setGeometry(QRect(170, 10, 301, 21))
        self.main_title.setFont(font)
        self.main_title.setText("Set Your Own Date and Time")

        # Ask for date
        self.date_entry = QLabel(self)
        self.date_entry.setGeometry(QRect(10, 70, 291, 31))
        self.date_entry.setFont(font)
        self.date_entry.setText("Enter Date (MM/DD/YYYY):")

        # Ask for time
        self.time_entry = QLabel(self)
        self.time_entry.setGeometry(QRect(90, 120, 281, 31))
        self.time_entry.setFont(font)
        self.time_entry.setText("Enter Time (23:59):")

        # Date input field
        self.date_input = QLineEdit(self)
        self.date_input.setGeometry(QRect(300, 70, 291, 41))
        self.date_input.setFont(font)

        # Time input field
        self.time_input = QLineEdit(self)
        self.time_input.setGeometry(QRect(300, 120, 291, 41))
        self.time_input.setFont(font)

        # Submit button. Upon clicking, it will setting_time will be executed with input values from the 2 input fields
        self.submit_button = QPushButton(self)
        self.submit_button.setGeometry(QRect(220, 190, 201, 51))
        self.submit_button.setFont(font)
        self.submit_button.setText("Set Date and Time")
        self.submit_button.clicked.connect(lambda: self.setting_time(self.date_input.text(),self.time_input.text()))
        
    def setting_time(self,date,time):
        # By Kyaw
        # Exception handling done through while loop and try/except statements. parse() will throw a ValueError if the inputs are not valid
        error_shown_or_passed = False
        while error_shown_or_passed == False:
            try: 
                # If parse throws no errors, then the timer on the main window will stop,
                # the value of time_label will be replaced with the user-inputted time
                # The current window will close upon finishing
                date_and_time = parse(date + " " + time)
                self.parent.timer.stop()
                self.parent.time_label.setText("Set Time: "+ str(date_and_time))
                self.close()
                error_shown_or_passed = True
            except:
                # If error, then reset the input fields, open message box that says got error.
                self.time_input.setText("")
                self.date_input.setText("")
                QMessageBox.about(self, "Input Error", "Please enter date and time in proper format.")
                error_shown_or_passed = True
