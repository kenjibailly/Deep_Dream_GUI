from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QTextCursor
import backend.src.py.windows.dream_video_window as dream_video_window
import backend.src.py.windows.dream_images_window as dream_images_window
import backend.src.py.windows.dream_on_window as dream_on_window
import backend.src.py.windows.images_to_video_window as images_to_video_window
import backend.src.py.windows.help_window as help_window

# Window creation class
class Ui_SubWindow(object):
    def setupUi(self, MainWindow, window):

        # Window to file conversion through import to window_callback variable
        if window == "dream_video":
            window_callback = dream_video_window
        elif window == "dream_images":
            window_callback = dream_images_window
        elif window == "dream_on":
            window_callback = dream_on_window
        elif window == "images_to_video":
            window_callback = images_to_video_window

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1152, 700)
        MainWindow.setMinimumSize(QtCore.QSize(1152, 700))
        MainWindow.setMaximumSize(QtCore.QSize(1152, 700))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1152, 700))
        self.label.setStyleSheet("background-image: url(backend/src/images/main/bg.png);")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("backend/src/images/main/bg.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.button_home = QtWidgets.QPushButton(self.centralwidget)
        self.button_home.setGeometry(QtCore.QRect(70, 600, 62, 63))
        self.button_home.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_home.setStyleSheet("background-image: url(backend/src/images/main/home.png);\n"
        "border: no-border;")
        self.button_home.setText("")
        self.button_home.setObjectName("button_home")
        self.button_help = QtWidgets.QPushButton(self.centralwidget)
        self.button_help.setGeometry(QtCore.QRect(1010, 600, 62, 63))
        self.button_help.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_help.setStyleSheet("background-image: url(backend/src/images/main/help.png);\n"
        "border: no-border;")
        self.button_help.setText("")
        self.button_help.setObjectName("button_help")

        if not window == "help":
            self.sub_menu_info = QtWidgets.QLabel(self.centralwidget)
            self.sub_menu_info.setGeometry(QtCore.QRect(100, 160, 954, 87))
            self.sub_menu_info.setStyleSheet('background-image: url(backend/src/images/'+window+'/info_bg_'+window+'.png);')
            self.sub_menu_info.setText("")
            self.sub_menu_info.setObjectName(""+window+"_info")
            self.sub_menu_bg = QtWidgets.QLabel(self.centralwidget)
            self.sub_menu_bg.setGeometry(QtCore.QRect(90, 260, 968, 304))
            self.sub_menu_bg.setStyleSheet("background-image: url(backend/src/images/"+window+"/"+window+"_bg.png);\n"
            "background-image: url(backend/src/images/"+window+"/"+window+"_bg.png);")
            self.sub_menu_bg.setText("")
            self.sub_menu_bg.setObjectName(""+window+"_bg")
            self.button_generate = QtWidgets.QPushButton(self.centralwidget)
            self.button_generate.setGeometry(QtCore.QRect(420, 590, 305, 70))
            self.button_generate.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.button_generate.setStyleSheet("background-image: url(backend/src/images/"+window+"/button_generate_"+window+".png);\n"
            "border: no-border;")
            self.button_generate.setText("")
            self.button_generate.setObjectName("button_generate_"+window+"")
            self.progress = QtWidgets.QProgressBar(self.centralwidget)
            self.progress.setGeometry(460, 560, 250, 20)
            self.label_5 = QtWidgets.QLabel(self.centralwidget)
            self.label_5.setGeometry(QtCore.QRect(140, 320, 461, 101))
            self.label_5.setStyleSheet("background-color: rgb(255,255,255,50);\n"
            "border: 2px solid #ffffff;\n"
            "border-radius: 15px;")
            self.label_5.setText("")
            self.label_5.setObjectName("label_5")
            self.button_input_folder = QtWidgets.QPushButton(self.centralwidget)
            self.button_input_folder.setGeometry(QtCore.QRect(290, 370, 161, 41))
            self.button_input_folder.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.button_input_folder.setStyleSheet("background-color: rgb(255,255,255,50);\n"
            "border: 2px solid #ffffff;\n"
            "border-radius: 15px;\n"
            "color: #ffffff;\n"
            "font: 25px \"Dense\";")
            self.button_input_folder.setObjectName("button_input_folder")
            self.label_6 = QtWidgets.QLabel(self.centralwidget)
            self.label_6.setGeometry(QtCore.QRect(140, 430, 461, 101))
            self.label_6.setStyleSheet("background-color: rgb(255,255,255,50);\n"
            "border: 2px solid #ffffff;\n"
            "border-radius: 15px;\n")
            self.label_6.setText("")
            self.label_6.setObjectName("label_6")
            self.button_output_folder = QtWidgets.QPushButton(self.centralwidget)
            self.button_output_folder.setGeometry(QtCore.QRect(290, 480, 161, 41))
            self.button_output_folder.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.button_output_folder.setStyleSheet("background-color: rgb(255,255,255,50);\n"
            "border: 2px solid #ffffff;\n"
            "border-radius: 15px;\n"
            "color: #ffffff;\n"
            "font: 25px \"Dense\";")
            self.button_output_folder.setObjectName("button_output_folder")
            self.input_folder_path = QtWidgets.QPlainTextEdit(self.centralwidget)
            self.input_folder_path.setGeometry(QtCore.QRect(160, 330, 441, 41))
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.input_folder_path.sizePolicy().hasHeightForWidth())
            self.input_folder_path.setSizePolicy(sizePolicy)
            self.input_folder_path.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
            self.input_folder_path.setStyleSheet("background-color: rgb(255,255,255,0);\n"
            "border: no-border;\n"
            "color: #ffffff;\n"
            "font: 25px \"Dense\";")
            self.input_folder_path.setReadOnly(True)
            self.input_folder_path.setOverwriteMode(False)
            self.input_folder_path.setBackgroundVisible(False)
            self.input_folder_path.setCenterOnScroll(False)
            self.input_folder_path.setObjectName("input_folder_path")
            self.output_folder_path = QtWidgets.QPlainTextEdit(self.centralwidget)
            self.output_folder_path.setGeometry(QtCore.QRect(150, 440, 441, 41))
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.output_folder_path.sizePolicy().hasHeightForWidth())
            self.output_folder_path.setSizePolicy(sizePolicy)
            self.output_folder_path.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
            self.output_folder_path.setStyleSheet("background-color: rgb(255,255,255,0);\n"
            "border: no-border;\n"
            "color: #ffffff;\n"
            "font: 25px \"Dense\";")
            self.output_folder_path.setReadOnly(True)
            self.output_folder_path.setOverwriteMode(False)
            self.output_folder_path.setBackgroundVisible(False)
            self.output_folder_path.setCenterOnScroll(False)
            self.output_folder_path.setObjectName("output_folder_path")

        # Different template modifications on different windows

        if window == "dream_on":
            print('')
            self.button_random = QtWidgets.QPushButton(self.centralwidget)
            self.button_random.setGeometry(QtCore.QRect(800, 505, 111, 31))
            self.button_random.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.button_random.setStyleSheet("background-color: rgb(255,255,255,50);\n"
            "border: 2px solid #ffffff;\n"
            "border-radius: 15px;\n"
            "color: #ffffff;\n"
            "font: 25px \"Dense\";")
            self.button_random.setObjectName("button_random")
            self.label_2 = QtWidgets.QLabel(self.centralwidget)
            self.label_2.setGeometry(QtCore.QRect(800, 320, 121, 31))
            self.label_2.setLayoutDirection(QtCore.Qt.RightToLeft)
            self.label_2.setStyleSheet("color: #ffffff;\n"
            "font: 30px \"Dense\";")
            self.label_2.setObjectName("label_2")
            self.label_3 = QtWidgets.QLabel(self.centralwidget)
            self.label_3.setGeometry(QtCore.QRect(750, 365, 161, 31))
            self.label_3.setLayoutDirection(QtCore.Qt.RightToLeft)
            self.label_3.setStyleSheet("color: #ffffff;\n"
            "font: 30px \"Dense\";")
            self.label_3.setObjectName("label_3")
            self.label_4 = QtWidgets.QLabel(self.centralwidget)
            self.label_4.setGeometry(QtCore.QRect(725, 410, 191, 31))
            self.label_4.setLayoutDirection(QtCore.Qt.RightToLeft)
            self.label_4.setStyleSheet("color: #ffffff;\n"
            "font: 30px \"Dense\";")
            self.label_4.setObjectName("label_4")
            self.input_layer = QtWidgets.QPlainTextEdit(self.centralwidget)
            self.input_layer.setGeometry(QtCore.QRect(920, 315, 50, 35))
            self.input_layer.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
            self.input_layer.setStyleSheet("background-color: rgb(255,255,255,50);\n"
            "border: 2px solid #ffffff;\n"
            "border-radius: 10px;\n"
            "color: #ffffff;\n"
            "font: 20px \"Dense\";")
            self.input_layer.setTabChangesFocus(True)
            self.input_layer.setObjectName("input_layer")
            self.input_iterations = QtWidgets.QPlainTextEdit(self.centralwidget)
            self.input_iterations.setGeometry(QtCore.QRect(920, 360, 51, 35))
            self.input_iterations.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
            self.input_iterations.setStyleSheet("background-color: rgb(255,255,255,50);\n"
            "border: 2px solid #ffffff;\n"
            "border-radius: 10px;\n"
            "color: #ffffff;\n"
            "font: 20px \"Dense\";")
            self.input_iterations.setTabChangesFocus(True)
            self.input_iterations.setObjectName("input_iterations")
            self.input_recursive_level = QtWidgets.QPlainTextEdit(self.centralwidget)
            self.input_recursive_level.setGeometry(QtCore.QRect(920, 405, 51, 35))
            self.input_recursive_level.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
            self.input_recursive_level.setStyleSheet("background-color: rgb(255,255,255,50);\n"
            "border: 2px solid #ffffff;\n"
            "border-radius: 10px;\n"
            "color: #ffffff;\n"
            "font: 20px \"Dense\";")
            self.input_recursive_level.setTabChangesFocus(True)
            self.input_recursive_level.setObjectName("input_recursive_level")
            self.label_7 = QtWidgets.QLabel(self.centralwidget)
            self.label_7.setGeometry(QtCore.QRect(750, 455, 191, 31))
            self.label_7.setLayoutDirection(QtCore.Qt.RightToLeft)
            self.label_7.setStyleSheet("color: #ffffff;\n"
            "font: 30px \"Dense\";")
            self.label_7.setObjectName("label_7")
            self.input_frames_amount = QtWidgets.QPlainTextEdit(self.centralwidget)
            self.input_frames_amount.setGeometry(QtCore.QRect(920, 450, 51, 35))
            self.input_frames_amount.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
            self.input_frames_amount.setStyleSheet("background-color: rgb(255,255,255,50);\n"
            "border: 2px solid #ffffff;\n"
            "border-radius: 10px;\n"
            "color: #ffffff;\n"
            "font: 20px \"Dense\";")
            self.input_frames_amount.setTabChangesFocus(True)
            self.input_frames_amount.setObjectName("input_frames_amount")
        elif window == "images_to_video":
            self.label_8 = QtWidgets.QLabel(self.centralwidget)
            self.label_8.setGeometry(QtCore.QRect(750, 395, 150, 31))
            self.label_8.setLayoutDirection(QtCore.Qt.RightToLeft)
            self.label_8.setStyleSheet("color: #ffffff;\n"
            "font: 30px \"Dense\";")
            self.label_8.setObjectName("label_2")
            self.input_fps = QtWidgets.QPlainTextEdit(self.centralwidget)
            self.input_fps.setGeometry(QtCore.QRect(920, 390, 50, 40))
            self.input_fps.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
            self.input_fps.setStyleSheet("background-color: rgb(255,255,255,50);\n"
            "border: 2px solid #ffffff;\n"
            "border-radius: 10px;\n"
            "color: #ffffff;\n"
            "font: 25px \"Dense\";")
            self.input_fps.setTabChangesFocus(True)
            self.input_fps.setObjectName("input_layer")
            self.input_fps.setPlainText('24')
        elif window == "help":
            print("help window")
        else:
            self.button_random = QtWidgets.QPushButton(self.centralwidget)
            self.button_random.setGeometry(QtCore.QRect(800, 490, 111, 31))
            self.button_random.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.button_random.setStyleSheet("background-color: rgb(255,255,255,50);\n"
            "border: 2px solid #ffffff;\n"
            "border-radius: 15px;\n"
            "color: #ffffff;\n"
            "font: 25px \"Dense\";")
            self.button_random.setObjectName("button_random")
            self.label_2 = QtWidgets.QLabel(self.centralwidget)
            self.label_2.setGeometry(QtCore.QRect(800, 330, 121, 31))
            self.label_2.setLayoutDirection(QtCore.Qt.RightToLeft)
            self.label_2.setStyleSheet("color: #ffffff;\n"
            "font: 35px \"Dense\";")
            self.label_2.setObjectName("label_2")
            self.label_3 = QtWidgets.QLabel(self.centralwidget)
            self.label_3.setGeometry(QtCore.QRect(740, 380, 161, 31))
            self.label_3.setLayoutDirection(QtCore.Qt.RightToLeft)
            self.label_3.setStyleSheet("color: #ffffff;\n"
            "font: 35px \"Dense\";")
            self.label_3.setObjectName("label_3")
            self.label_4 = QtWidgets.QLabel(self.centralwidget)
            self.label_4.setGeometry(QtCore.QRect(710, 430, 191, 31))
            self.label_4.setLayoutDirection(QtCore.Qt.RightToLeft)
            self.label_4.setStyleSheet("color: #ffffff;\n"
            "font: 35px \"Dense\";")
            self.label_4.setObjectName("label_4")
            self.input_layer = QtWidgets.QPlainTextEdit(self.centralwidget)
            self.input_layer.setGeometry(QtCore.QRect(920, 320, 50, 41))
            self.input_layer.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
            self.input_layer.setStyleSheet("background-color: rgb(255,255,255,50);\n"
            "border: 2px solid #ffffff;\n"
            "border-radius: 10px;\n"
            "color: #ffffff;\n"
            "font: 25px \"Dense\";")
            self.input_layer.setTabChangesFocus(True)
            self.input_layer.setObjectName("input_layer")
            self.input_iterations = QtWidgets.QPlainTextEdit(self.centralwidget)
            self.input_iterations.setGeometry(QtCore.QRect(920, 370, 51, 41))
            self.input_iterations.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
            self.input_iterations.setStyleSheet("background-color: rgb(255,255,255,50);\n"
            "border: 2px solid #ffffff;\n"
            "border-radius: 10px;\n"
            "color: #ffffff;\n"
            "font: 25px \"Dense\";")
            self.input_iterations.setTabChangesFocus(True)
            self.input_iterations.setObjectName("input_iterations")
            self.input_recursive_level = QtWidgets.QPlainTextEdit(self.centralwidget)
            self.input_recursive_level.setGeometry(QtCore.QRect(920, 420, 51, 41))
            self.input_recursive_level.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
            self.input_recursive_level.setStyleSheet("background-color: rgb(255,255,255,50);\n"
            "border: 2px solid #ffffff;\n"
            "border-radius: 10px;\n"
            "color: #ffffff;\n"
            "font: 25px \"Dense\";")
            self.input_recursive_level.setTabChangesFocus(True)
            self.input_recursive_level.setObjectName("input_recursive_level")
        
        if window == "dream_video":
            self.button_resume = QtWidgets.QPushButton(self.centralwidget)
            self.button_resume.setGeometry(QtCore.QRect(600, 590, 305, 70))
            self.button_generate.setGeometry(QtCore.QRect(240, 590, 305, 70))
            self.button_resume.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.button_resume.setStyleSheet("background-image: url(backend/src/images/"+window+"/button_resume_"+window+".png);\n"
            "border: no-border;")            
            self.button_resume.setText("")
            self.button_resume.setObjectName("button_resume_"+window+"")

        if window == "help":
            self.help_dream_images = QtWidgets.QLabel(self.centralwidget)
            self.help_dream_images.setGeometry(QtCore.QRect(90, 150, 414, 93))
            self.help_dream_images.setStyleSheet("background-image: url(backend/src/images/help/help_dream_images.png);")
            self.help_dream_images.setText("")
            self.help_dream_images.setObjectName("help_dream_images")
            self.help_dream_video = QtWidgets.QLabel(self.centralwidget)
            self.help_dream_video.setGeometry(QtCore.QRect(600, 150, 414, 96))
            self.help_dream_video.setStyleSheet("background-image: url(backend/src/images/help/help_dream_video.png);")
            self.help_dream_video.setText("")
            self.help_dream_video.setObjectName("help_dream_video")
            self.help_dream_images_to_video = QtWidgets.QLabel(self.centralwidget)
            self.help_dream_images_to_video.setGeometry(QtCore.QRect(600, 270, 414, 96))
            self.help_dream_images_to_video.setStyleSheet("background-image: url(backend/src/images/help/help_dream_images_to_video.png);")
            self.help_dream_images_to_video.setText("")
            self.help_dream_images_to_video.setObjectName("help_dream_images_to_video")
            self.help_dream_on = QtWidgets.QLabel(self.centralwidget)
            self.help_dream_on.setGeometry(QtCore.QRect(90, 260, 414, 190))
            self.help_dream_on.setStyleSheet("background-image: url(backend/src/images/help/help_dream_on.png);")
            self.help_dream_on.setText("")
            self.help_dream_on.setObjectName("help_dream_on")
            self.help_inputs_info = QtWidgets.QLabel(self.centralwidget)
            self.help_inputs_info.setGeometry(QtCore.QRect(130, 500, 860, 156))
            self.help_inputs_info.setStyleSheet("background-image: url(backend/src/images/help/help_inputs_info.png);")
            self.help_inputs_info.setText("")
            self.help_inputs_info.setObjectName("help_inputs_info")
            self.button_bug_report = QtWidgets.QPushButton(self.centralwidget)
            self.button_bug_report.setGeometry(QtCore.QRect(600, 390, 414, 93))
            self.button_bug_report.setStyleSheet("background-image: url(backend/src/images/help/help_bug_report.png);\n"
            "border: no-border;")
            self.button_bug_report.setText("")
            self.button_bug_report.setObjectName("button_bug_report")
            self.button_bug_report.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        # Display folder paths after initializing, going to the home menu and going back
        if not window == "help":
            try:
                self.input_folder_path.setPlainText('{}'.format(window_callback.input_folder))
            except:
                self.input_folder_path.setPlainText('')
            try:
                self.output_folder_path.setPlainText('{}'.format(window_callback.output_folder))
            except:
                self.output_folder_path.setPlainText('')

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow, window)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # When buttons are clicked, connect them to the "clicked" function
        if not window == "images_to_video" and not window == "help":        
            self.button_random.clicked.connect(lambda: window_callback.clicked('random', MainWindow, self))

        if not window == "help":
            self.button_input_folder.clicked.connect(lambda: window_callback.clicked('input_folder', MainWindow, self))
            self.button_output_folder.clicked.connect(lambda: window_callback.clicked('output_folder', MainWindow, self))
            self.button_generate.clicked.connect(lambda: window_callback.clicked('generate', MainWindow, self))
            self.button_home.clicked.connect(lambda: window_callback.clicked('home', MainWindow, self))
            self.button_help.clicked.connect(lambda: window_callback.clicked('help', MainWindow, self))

        if window == "help":
            self.button_bug_report.clicked.connect(lambda: help_window.clicked('bug_report', MainWindow, self))
            self.button_home.clicked.connect(lambda: help_window.clicked('home', MainWindow, self))
            self.button_help.clicked.connect(lambda: help_window.clicked('help', MainWindow, self))

        if window == "dream_video":
            self.button_resume.clicked.connect(lambda: window_callback.clicked('resume', MainWindow, self))

        # Text Changed, check for enter pressed
        if window == "dream_images" or window == "dream_video" or window == "dream_on":
            self.input_layer.textChanged.connect(lambda: self.enter_pressed(window, window_callback, MainWindow))
            self.input_iterations.textChanged.connect(lambda: self.enter_pressed(window, window_callback, MainWindow))
            self.input_recursive_level.textChanged.connect(lambda: self.enter_pressed(window, window_callback, MainWindow))
        if window == "dream_on":
            self.input_frames_amount.textChanged.connect(lambda: self.enter_pressed(window, window_callback, MainWindow))
        if window == "images_to_video":
            self.input_fps.textChanged.connect(lambda: self.enter_pressed(window, window_callback, MainWindow))

    def enter_pressed(self, window, window_callback, MainWindow):
        # Input Layer pressed

        if window == "dream_images" or window == "dream_video" or window == "dream_on":

            # Input Layer pressed
            try:
                input_layer_value = self.input_layer.toPlainText()[-1]
                if input_layer_value == '\n':
                    print('You Pressed Enter!')
                    self.input_layer.setPlainText(self.input_layer.toPlainText()[:-1])
                    self.input_layer.moveCursor(QTextCursor.End)
                    window_callback.clicked('generate', MainWindow, self)
            except IndexError:
                print('Index Error occurred')
                pass

            # Input Iterations pressed
            try:
                input_iterations_value = self.input_iterations.toPlainText()[-1]
                if input_iterations_value == '\n':
                    print('You Pressed Enter!')
                    self.input_iterations.setPlainText(self.input_iterations.toPlainText()[:-1])
                    self.input_iterations.moveCursor(QTextCursor.End)
                    window_callback.clicked('generate', MainWindow, self)
            except IndexError:
                print('Index Error occurred')
                pass

            # Input Recursive Levels pressed
            try:
                input_recursive_level_value = self.input_recursive_level.toPlainText()[-1]
                if input_recursive_level_value == '\n':
                    print('You Pressed Enter!')
                    self.input_recursive_level.setPlainText(self.input_recursive_level.toPlainText()[:-1])
                    self.input_recursive_level.moveCursor(QTextCursor.End)
                    window_callback.clicked('generate', MainWindow, self)
            except IndexError:
                print('Index Error occurred')
                pass

        if window == "dream_on":

            # Input FPS pressed
            try:
                input_frames_amount_value = self.input_frames_amount.toPlainText()[-1]
                if input_frames_amount_value == '\n':
                    print('You Pressed Enter!')
                    self.input_frames_amount.setPlainText(self.input_frames_amount.toPlainText()[:-1])
                    self.input_frames_amount.moveCursor(QTextCursor.End)
                    window_callback.clicked('generate', MainWindow, self)
            except IndexError:
                print('Index Error occurred')
                pass

        if window == "images_to_video":

            # Input FPS pressed
            try:
                input_fps_value = self.input_fps.toPlainText()[-1]
                if input_fps_value == '\n':
                    print('You Pressed Enter!')
                    self.input_fps.setPlainText(self.input_fps.toPlainText()[:-1])
                    self.input_fps.moveCursor(QTextCursor.End)
                    window_callback.clicked('generate', MainWindow, self)
            except IndexError:
                print('Index Error occurred')
                pass


    def retranslateUi(self, MainWindow, window):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Deep Dream Generator"))
        if window == "images_to_video":
            self.label_8.setText(_translate("MainWindow", "Frames per second:"))
        elif window == "help":
            print('help window')
        else:
            self.button_random.setText(_translate("MainWindow", "Random"))
            self.label_2.setText(_translate("MainWindow", "Layer (1-11):"))
            self.label_3.setText(_translate("MainWindow", "Iterations (5-100):"))
            self.label_4.setText(_translate("MainWindow", "Recursive Level (0-8):"))
        if window == "dream_on":
            self.label_7.setText(_translate("MainWindow", "Amount of frames:"))

        if not window == "help":
            self.button_input_folder.setText(_translate("MainWindow", "Choose Input File(s)"))
            self.button_output_folder.setText(_translate("MainWindow", "Choose Output Folder"))

        # Display folder paths after initializing, going to the home menu and going back

        # try:
        #     self.input_folder_path.setPlainText(_translate("MainWindow", input_folder))
        # except:
        #     self.input_folder_path.setPlainText(_translate("MainWindow", ""))
        # try:
        #     self.output_folder_path.setPlainText(_translate("MainWindow", output_folder))
        # except:
        #     self.input_folder_path.setPlainText(_translate("MainWindow", ""))
