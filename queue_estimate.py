"""
queue_estimate.py has the QueueEstimator class which is needed for the queue estimator requirement.

Criteria Fulfilled:
- Feature E
- Interface Design
- Programming Style
- Program Organisation
- Program Correctness
- Exception Handling
"""

from PyQt5.QtWidgets import QMainWindow, QMessageBox, QLineEdit, QLabel, QPushButton
from PyQt5.QtGui import QFont, QImage, QPalette, QBrush
from PyQt5.QtCore import Qt, QRect, QSize
import sys
import pandas as pd
import app_data as info

class QueueEstimator(QMainWindow):
    # By Nisha
    def __init__(self,name):
        super().__init__()

        # Sizing, background, font
        self.setWindowTitle("Queue Estimator")
        self.setFixedSize(536, 219)
        font = QFont()
        font.setPointSize(10)
        oImage = QImage("icons/background.jpg")
        sImage = oImage.scaled(QSize(536,219))
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))                    
        self.setPalette(palette)

        # Input label
        self.input_label = QLabel(self)
        self.input_label.setGeometry(QRect(10, 60, 391, 41))
        self.input_label.setText("Enter Number of People in the Queue:")
        self.input_label.setFont(font)
 
        # In-line input box entry field
        self.lineEdit = QLineEdit(self)
        self.lineEdit.setGeometry(QRect(410, 60, 113, 41))
        self.lineEdit.setFont(font)

        # Title label
        self.title = QLabel(self)
        self.title.setGeometry(QRect(130, 10, 291, 31))
        self.title.setText("Queue Estimator")
        self.title.setFont(font)
        self.title.setAlignment(Qt.AlignCenter)

        # Result label
        self.result = QLabel(self)
        self.result.setGeometry(QRect(90, 180, 500, 21))
        self.result.setFont(font)
        self.result.setText("")
        self.result.setScaledContents(True)

        # Push button 
        self.pushButton = QPushButton(self)
        self.pushButton.setGeometry(QRect(220, 120, 93, 28))
        self.pushButton.setText("Calculate")
        self.pushButton.clicked.connect(lambda:self.pressed(name))

    def pressed(self,name):
        #By Nisha
        self.name=info.stalls[name]
        # Ensure that user inputs only integers, if not raise error and reset the entry field. 
        # Using a while loop with try-except-else for exception handling
        error_shown_or_passed = False
        while error_shown_or_passed == False:
            try:
                x = int(self.lineEdit.text())
                if x <= 0:
                    raise ValueError
                error_shown_or_passed = True
            except ValueError:
                QMessageBox.about(self, "Input Error", "Please enter a positive integer.")
                self.lineEdit.setText("")
                error_shown_or_passed = True
            else:
                # If the interger is valid, then get the average waiting time information for that specific stall and calculate the time
                wait_time=float(info.stall_data[info.stall_data["Stall"]==self.name]["Waiting time"].item())
                self.result.setText("Estimate Waiting Time: {} minutes".format(x*wait_time))

            
