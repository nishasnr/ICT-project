from PyQt5.QtWidgets import QApplication
import sys
import mainwindow as main_window

def window():
	# By Kyaw
	app = QApplication(sys.argv)
	# window() creates a MainWindow object and shows it. 
	win = main_window.MainWindow()
	win.show()
	# When application signals exit, meaning when the user presses the close button, the program will also stop running
	sys.exit(app.exec_())

window()
