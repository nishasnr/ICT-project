"""
food_items.py handles each food item and its availability.

Criteria Fulfilled:
- Feature B
- Feature D
- Programming Style
- Program Organisation
- Program Correctness
- String Methods
"""
from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import QSize
from functools import partial
import sys
import app_data as info
from opening import opening_hours

def food_lister(self,currentStallData):
    # By Nisha
	# x is the index
    for x in range(0,len(currentStallData)*2,2):
    	# Put the food items into a list of QLabels, alternating between item name and item price

    	# Food name
        self.food_labels.append(x)
        self.food_labels[x]= QLabel(self.scrollAreaWidgetContents)
        self.food_labels[x].setMinimumSize(QSize(0, 50))
        self.food_labels[x].setText(currentStallData.iloc[x//2]["Food/Dish"])
        self.gridLayout.addWidget(self.food_labels[x], x, 0, 1, 1)

        # Food price
        self.food_labels.append(x+1)
        self.food_labels[x+1]= QLabel(self.scrollAreaWidgetContents)
        self.food_labels[x+1].setMinimumSize(QSize(0, 50))
        self.food_labels[x+1].setText("$"+str(currentStallData.iloc[x//2]["Price"])+"0")
        self.gridLayout.addWidget(self.food_labels[x+1], x, 1, 1, 1)

        # Calls the opening_checker function to check whether the food is available now or not. 
        opening_checker(self,currentStallData,x)

def opening_checker(self,currentStallData,x):
    # By Kyaw
    # Checks if stall is open on weekends
    saturday_opening = info.opening_data[(info.opening_data["Stall"]==self.name) & (info.opening_data["Day"]=="Saturday")]["Opening Time"].item()
    sunday_opening = info.opening_data[(info.opening_data["Stall"]==self.name) & (info.opening_data["Day"]=="Sunday")]["Opening Time"].item()
    self.set_button = True
    # If closed, then strikethrough the food items
    if saturday_opening == "Closed" and self.day_of_week=="Saturday":
        self.food_labels[x].setText(self.strike(self.food_labels[x].text()))
        self.set_button=False
    elif sunday_opening == "Closed" and self.day_of_week=="Sunday":
        self.food_labels[x].setText(self.strike(self.food_labels[x].text()))
        self.set_button=False
    # If it's not available on a certain day, then strikethrough
    elif (currentStallData.iloc[x//2]["Availability"] in info.days) and (currentStallData.iloc[x//2]["Availability"]!=self.day_of_week):
        self.food_labels[x].setText(self.strike(self.food_labels[x].text()))
    # If it's not available at a certain time, then strikethrough
    elif (currentStallData.iloc[x//2]["Availability"] != "Breakfast") and self.hour < 11:
        self.food_labels[x].setText(self.strike(self.food_labels[x].text()))
    # If stall closes at 8pm, and time is after 8, strikethrough
    elif info.opening_data[(info.opening_data["Stall"]==self.name) & (info.opening_data["Day"]==self.day_of_week)]["Closing Time"].item() == "20:00"  and (self.hour*100+self.minute) > 2000:
        self.food_labels[x].setText(self.strike(self.food_labels[x].text()))
        self.set_button=False
    # If stall closes at 830pm, and time is after 830, strikethrough
    elif info.opening_data[(info.opening_data["Stall"]==self.name) & (info.opening_data["Day"]==self.day_of_week)]["Closing Time"].item() == "20:30"  and (self.hour*100+self.minute) > 2030:
        self.food_labels[x].setText(self.strike(self.food_labels[x].text()))
        self.set_button=False
    # If stall opens at 7am, and time is before 7am, strikethrough
    if info.opening_data[(info.opening_data["Stall"]==self.name) & (info.opening_data["Day"]==self.day_of_week)]["Opening Time"].item() == "7:00"  and (self.hour*100+self.minute) < 700:
        self.set_button=False
    # If stall opens at 730am, and time is before 730am, strikethrough
    if info.opening_data[(info.opening_data["Stall"]==self.name) & (info.opening_data["Day"]==self.day_of_week)]["Opening Time"].item() == "7:30"  and (self.hour*100+self.minute) < 730:
        self.set_button=False