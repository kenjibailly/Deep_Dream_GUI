from PyQt5 import QtCore, QtGui, QtWidgets
import main
import backend.src.py.windows.sub_menu_one_template as sub_menu_one_template
import os
import webbrowser
window = "help"

#  Button Navigation
def clicked(button, MainWindow, self):

        if button == 'bug_report':
            webbrowser.open('http://github.com/kenjibailly/deep_dream')
            print('open http://github.com/kenjibailly/deep_dream')
            
        # Home button
        elif button == 'home':
                print('home') # Open Home window
                main.start_main(MainWindow)

        # Help button
        elif button == 'help':
                print('help') # Open Help window


# Initialize window function
def start_help(MainWindow):
    import sys
    ui = sub_menu_one_template.Ui_SubWindow()
    ui.setupUi(MainWindow, window)
    MainWindow.show()