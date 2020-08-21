"""
stall_menu.py has the Stall Menu class and all its associated functions.

Criteria Fulfilled:
- Feature A
- Feature B
- Feature D
- Feature F
- Interface Design
- Programming Style
- Program Organisation
- Program Correctness
- String Operations
"""
from PyQt5.QtWidgets import QScrollArea, QGridLayout, QFrame, QWidget, QLabel, QMessageBox, QVBoxLayout, QHBoxLayout, QPushButton, QSpacerItem, QSizePolicy
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QSize, Qt, QRect
from functools import partial
import sys
import datetime as dt
import app_data as info
import queue_estimate as q_est
from opening import opening_hours
from food_items import food_lister

class StallMenu(QWidget):
    # By Kyaw and Ryan
    def __init__(self, parent,name):
        self.parent = parent
        super(StallMenu,self).__init__(parent)

        # Overall Vertical Layout
        self.verticalLayout = QVBoxLayout(self)
        
        # Top Row Horizontal Layout
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(5, 5, 5, 5)

        # Top Row Date
        self.backButton = QPushButton(self)
        self.backButton.setText("Back")
        self.horizontalLayout_3.addWidget(self.backButton)

        # Top Row Horizontal Spacer
        spacerItem = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)

        # Top Row Time    
        self.time_label = QLabel(self)
        self.time_label.setText(self.parent.time_label.text())
        self.horizontalLayout_3.addWidget(self.time_label)

        # Add the Top Row Horizontal Layout to the Overall Vertical Layout
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        # Stall Logo
        self.stallLogo = QLabel(self)
        self.stallLogo.setMaximumSize(QSize(150, 150))
        self.stallLogo.setFrameShadow(QFrame.Plain)
        # Get the stall logo
        self.stallLogo.setPixmap(QPixmap("icons/"+name+".png"))
        self.stallLogo.setScaledContents(True)
        self.verticalLayout.addWidget(self.stallLogo, 0, Qt.AlignHCenter)
       
        # Location Label
        self.location_label = QLabel(self)
        self.verticalLayout.addWidget(self.location_label, 0, Qt.AlignHCenter)

        # Cuisine Label
        self.cuisine_label = QLabel(self)
        self.verticalLayout.addWidget(self.cuisine_label, 0, Qt.AlignHCenter)
        self.cuisine_label.setText("Cuisine: Western")

        # Horizontal Row Layout for Triple Button Row
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)

        # Opening Hours Button
        self.opening_button = QPushButton(self)
        self.opening_button.setMinimumSize(QSize(0, 75))
        self.horizontalLayout.addWidget(self.opening_button)
        self.opening_button.setText("Opening Hours")
        
        # self.opening_button.clicked.connect(self.opening_hours)
        # Queue Estimator Button
        self.queue_button = QPushButton(self)
        self.queue_button.setMinimumSize(QSize(0, 75))
        self.horizontalLayout.addWidget(self.queue_button)
        self.queue_button.setText("Queue Estimator")

        # Add the Horizontal Layout to Overall Vertical Layout
        self.verticalLayout.addLayout(self.horizontalLayout)

        # Define Scroll Area for the Food Menu
        self.scrollArea = QScrollArea(self)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 547, 587))

        # Define Grid Layout inside the Scroll Area
        self.gridLayout_2 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout = QGridLayout()
        
        # Set Column Stretching Values for the Food Menu
        # Basically Food:Price is 6:1 space
        self.gridLayout.setColumnStretch(0, 6)
        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        
        # gets information about the food
        self.get_info(name)

    def strike(self,text):
        # By Kyaw
        # Strikethrough the text
        return ''.join([u'\u0336{}'.format(c) for c in text])
        

    def get_info(self,name):
        # By Kyaw
        set_button=True
        # Get the basic information
        self.day_of_week =  self.day_of_week(self.time_label.text())
        self.hour = self.hour(self.time_label.text())
        self.minute = self.minute(self.time_label.text())
        self.name = info.stalls[name]
        
        # Get stall location and cuisine information
        self.location_label.setText("Location: " + info.stall_data[info.stall_data["Stall"]==self.name]["Location"].item())
        self.cuisine_label.setText("Cuisine: " + info.stall_data[info.stall_data["Stall"]==self.name]["Cuisine"].item())
        
        # Get the stall menu items
        currentStallData = info.food_data[info.food_data["Stall"]==self.name]
        
        # List of food items, calls the food_lister function to populate the food_labels list
        self.food_labels=[]
        food_lister(self,currentStallData)
                
        # Connect the opening hours button to the opening hours function
        self.opening_button.clicked.connect(lambda: opening_hours(self,name))

        # Connect the queue estimator button to the queue estimator function
        self.queue_button.clicked.connect(lambda: self.queue_estimator(name,self.set_button))
        if self.set_button == False:
            QMessageBox.about(self, "Stall is Closed", "Stall is closed right now, but you can view further information about it.")
    # Creates a QueueEstimator object and shows it in a new window
    def queue_estimator(self,name,flag):
        # By Nisha
        # flag is to check whether the timing is 9pm or beyond, indicated by an earlier function. If it is, then disable the button and give an error popup
        if not(flag):
            self.queue_button.setEnabled(False)
            QMessageBox.about(self, "Stall Error", "Stall is closed right now.")
        else:
            self.name = name
            self.QueueEstimator = q_est.QueueEstimator(name)
            self.QueueEstimator.show()

    """
    Date and Time Functions
    """
    def day_of_week(self,date_string):
        # By Kyaw
        # date_string can either be the live datetime or one that is set by user. For the latter case, the string will start with 'Set Time:'
        # and so the string should be snipped to include only the datetime.
        # Returns the day of the week in words.
        if "Set Time: " in date_string:
            date_string = date_string[10:]
        return info.days[dt.datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S').weekday()]
        

    def hour(self,date_string):
        # By Ryan
        # date_string can either be the live datetime or one that is set by user. For the latter case, the string will start with 'Set Time:'
        # and so the string should be snipped to include only the datetime.
        # Returns the hour of the day in integers.
        if "Set Time: " in date_string:
            date_string = date_string[10:]
        return int(dt.datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S').hour)

    def minute(self,date_string):
        # By Ryan
        # date_string can either be the live datetime or one that is set by user. For the latter case, the string will start with 'Set Time:'
        # and so the string should be snipped to include only the datetime.
        # Returns the hour of the day in integers.
        if "Set Time: " in date_string:
            date_string = date_string[10:]
        return int(dt.datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S').minute)


