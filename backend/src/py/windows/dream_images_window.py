from PyQt5 import QtCore, QtGui, QtWidgets
import main
import random
import backend.src.py.windows.sub_menu_one_template as sub_menu_one_template
import backend.src.py.windows.windows_validation as windows_validation
import backend.src.py.main_functions.dream_images as dream_images
import backend.src.py.windows.help_window as help_window

window = "dream_images"

#  Button Navigation
def clicked(button, MainWindow, self):
        
        # Declare global variables so they are recognized when pressing "generate"
        global input_folder
        global output_folder
        global input_file

        if button == 'input_folder':

                # Chosen input folder path to var
                # input_folder = QtWidgets.QFileDialog.getExistingDirectory(None, 'Select Input Folder')
                dir = "./"
                input_file = QtWidgets.QFileDialog.getOpenFileNames(None, "Select picture(s)...", dir, filter="Images (*.png *.jpg)")
                input_file = input_file[0]
                # Change the label to the path selected
                self.input_folder_path.setPlainText('{}'.format(input_file))

        elif button == 'output_folder':

                # Chosen output folder path to var
                output_folder = QtWidgets.QFileDialog.getExistingDirectory(None, 'Select Output Folder')
                # Change the label to the path selected
                self.output_folder_path.setPlainText('{}'.format(output_folder))

        elif button == 'generate':

                # Input fields to variables
                input_layer = self.input_layer.toPlainText()
                input_iterations = self.input_iterations.toPlainText()
                input_recursive_level = self.input_recursive_level.toPlainText()

                # Start validation
                initiate_generate = windows_validation.windows_validation(self, input_layer, input_iterations, input_recursive_level, window)


                # Initiate Generate process
                if initiate_generate == True:
                        print('Generate Execute')
                        
                        print("Layer: "+input_layer, " Iterations: "+input_iterations, " Recursive Level: "+input_recursive_level)
                        print('Input Files: {}'.format(input_file))
                        print('Output Folder: {}'.format(output_folder))

                        # Progress bar
                        self.completed = 0
                        self.progress.setValue(self.completed)

                        dream_images.start_dream_images(input_layer, input_iterations, input_recursive_level, input_file, output_folder, self)

                        choice = QtWidgets.QMessageBox.question(None, 'Dream Images Generated',
                                                        "Generate completed!\n Check your output folder: \n"+output_folder,
                                                        QtWidgets.QMessageBox.Ok)

                else:
                        print('Generate Execution Error')

        # Random generate button
        elif button == 'random':
                print('random') # Open Images to Video window

                random_layer = random.randint(1,10)
                random_iterations = random.randint(5,100)
                random_recursive_level = random.randint(0,8)

                self.input_layer.setPlainText('{}'.format(random_layer))
                self.input_iterations.setPlainText('{}'.format(random_iterations))
                self.input_recursive_level.setPlainText('{}'.format(random_recursive_level))

        # Home button
        elif button == 'home':
                print('home') # Open Home window
                main.start_main(MainWindow)

        # Help button
        elif button == 'help':
                print('help') # Open Help window
                help_window.start_help(MainWindow)


# Initialize window function
def start_dream_images(MainWindow):
        import sys
        ui = sub_menu_one_template.Ui_SubWindow()
        ui.setupUi(MainWindow, window)
        MainWindow.show()
