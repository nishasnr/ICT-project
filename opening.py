"""
opening.py handles the opening hours functionality.

Criteria Fulfilled:
- Feature F
- Programming Style
- Program Organisation
- Program Correctness
"""
from PyQt5.QtWidgets import QMessageBox
from functools import partial
import app_data as info

def opening_hours(self,name):
    # By Ryan
    self.name = info.stalls[name]

    # Get the opening hours information for weekdays and put them into a string
    weekdays_opening = info.opening_data[(info.opening_data["Stall"]==self.name) & (info.opening_data["Day"]=="Monday")]["Opening Time"].item()
    weekdays_closing = info.opening_data[(info.opening_data["Stall"]==self.name) & (info.opening_data["Day"]=="Monday")]["Closing Time"].item()
    weekdays_string = "Monday to Friday: "+ weekdays_opening + " to " + weekdays_closing

    # Get the opening hours information for Saturdays and put them into a string
    saturday_opening = info.opening_data[(info.opening_data["Stall"]==self.name) & (info.opening_data["Day"]=="Saturday")]["Opening Time"].item()
    saturday_closing = info.opening_data[(info.opening_data["Stall"]==self.name) & (info.opening_data["Day"]=="Saturday")]["Closing Time"].item()
    # If it's closed, then data will say closed for both opening and closing
    if (saturday_opening == saturday_closing):
        saturday_string = "Saturday: Closed"
    else:
        saturday_string = "Saturday: " + saturday_opening + " to " + saturday_closing

    # Get the opening hours information for Sundays and put them into a string
    sunday_opening = info.opening_data[(info.opening_data["Stall"]==self.name) & (info.opening_data["Day"]=="Sunday")]["Opening Time"].item()
    sunday_closing = info.opening_data[(info.opening_data["Stall"]==self.name) & (info.opening_data["Day"]=="Sunday")]["Closing Time"].item()
    
    # If it's closed, then data will say closed for both opening and closing
    if (sunday_opening==sunday_closing):
        sunday_string = "Sunday: Closed"
    else:
        sunday_string = "Sunday: " + sunday_opening + " to " + sunday_closing

    # Pop-up window to show the information
    QMessageBox.about(self, "Opening Hours", weekdays_string + "\n" + saturday_string + "\n" + sunday_string)