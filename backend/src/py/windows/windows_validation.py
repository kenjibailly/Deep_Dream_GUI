from PyQt5 import QtCore, QtGui, QtWidgets
import backend.src.py.windows.dream_images_window as dream_images_window
import backend.src.py.windows.dream_video_window as dream_video_window
import backend.src.py.windows.dream_on_window as dream_on_window
import backend.src.py.windows.images_to_video_window as images_to_video_window

def windows_validation(self, input_layer, input_iterations, input_recursive_level, window):

    # Window to file conversion through import to window_callback variable
    if window == "dream_images":
        window_callback = dream_images_window
    elif window == "dream_video":
        window_callback = dream_video_window
    elif window == "dream_on":
        window_callback = dream_on_window
    elif window == "images_to_video":
        window_callback = images_to_video_window
    
    if window == "dream_on":
        font_size = '20px'
    else:
        font_size = '25px'

    # Validation through "initiate_generate" variable
    initiate_generate = True
    if window == "images_to_video":
        if images_to_video_window.fps == "" or int(images_to_video_window.fps) < 0 or int(images_to_video_window.fps) > 60:
            initiate_generate = False
            self.input_fps.setStyleSheet("background-color: rgb(255,255,255,50);\n"
            "border: 2px solid #d41e82;\n"
            "border-radius: 10px;\n"
            "color: #ffffff;\n"
            "font: "+font_size+" \"Dense\";")
        else:
            self.input_fps.setStyleSheet("background-color: rgb(255,255,255,50);\n"
            "border: 2px solid #ffffff;\n"
            "border-radius: 10px;\n"
            "color: #ffffff;\n"
            "font: "+font_size+" \"Dense\";")
    else:
        if input_layer == "" or int(input_layer) < 0 or int(input_layer) > 11:
            initiate_generate = False
            self.input_layer.setStyleSheet("background-color: rgb(255,255,255,50);\n"
            "border: 2px solid #d41e82;\n"
            "border-radius: 10px;\n"
            "color: #ffffff;\n"
            "font: "+font_size+" \"Dense\";")
        else:
            self.input_layer.setStyleSheet("background-color: rgb(255,255,255,50);\n"
            "border: 2px solid #ffffff;\n"
            "border-radius: 10px;\n"
            "color: #ffffff;\n"
            "font: "+font_size+" \"Dense\";")
        
        if input_iterations == "" or int(input_iterations) < 5 or int(input_iterations) > 100:
            initiate_generate = False
            self.input_iterations.setStyleSheet("background-color: rgb(255,255,255,50);\n"
            "border: 2px solid #d41e82;\n"
            "border-radius: 10px;\n"
            "color: #ffffff;\n"
            "font: "+font_size+" \"Dense\";")
        else:
            self.input_iterations.setStyleSheet("background-color: rgb(255,255,255,50);\n"
            "border: 2px solid #ffffff;\n"
            "border-radius: 10px;\n"
            "color: #ffffff;\n"
            "font: "+font_size+" \"Dense\";") 

        if input_recursive_level == "" or int(input_recursive_level) < 0 or int(input_recursive_level) > 8:
            initiate_generate = False
            self.input_recursive_level.setStyleSheet("background-color: rgb(255,255,255,50);\n"
            "border: 2px solid #d41e82;\n"
            "border-radius: 10px;\n"
            "color: #ffffff;\n"
            "font: "+font_size+" \"Dense\";")
        else:
            self.input_recursive_level.setStyleSheet("background-color: rgb(255,255,255,50);\n"
            "border: 2px solid #ffffff;\n"
            "border-radius: 10px;\n"
            "color: #ffffff;\n"
            "font: "+font_size+" \"Dense\";")


    # if window == "dream_video" or window == "dream_images" or window == "images_to_video":
    try:
        print(window_callback.input_file)
        if window_callback.input_file == "":
            initiate_generate = False
            self.button_input_folder.setStyleSheet("background-color: rgb(255,255,255,50);\n"
            "border: 2px solid #d41e82;\n"
            "border-radius: 15px;\n"
            "color: #ffffff;\n"
            "font: 25px \"Dense\";")
        else:
            self.button_input_folder.setStyleSheet("background-color: rgb(255,255,255,50);\n"
            "border: 2px solid #ffffff;\n"
            "border-radius: 15px;\n"
            "color: #ffffff;\n"
            "font: 25px \"Dense\";")
    except:
        initiate_generate = False
        self.button_input_folder.setStyleSheet("background-color: rgb(255,255,255,50);\n"
        "border: 2px solid #d41e82;\n"
        "border-radius: 15px;\n"
        "color: #ffffff;\n"
        "font: 25px \"Dense\";")     
    # else:
    #     try:
    #         print(window_callback.input_folder)
    #         if window_callback.input_folder == "":
    #             initiate_generate = False
    #             self.button_input_folder.setStyleSheet("background-color: rgb(255,255,255,50);\n"
    #             "border: 2px solid #d41e82;\n"
    #             "border-radius: 15px;\n"
    #             "color: #ffffff;\n"
    #             "font: 25px \"Dense\";")
    #         else:
    #             self.button_input_folder.setStyleSheet("background-color: rgb(255,255,255,50);\n"
    #             "border: 2px solid #ffffff;\n"
    #             "border-radius: 15px;\n"
    #             "color: #ffffff;\n"
    #             "font: 25px \"Dense\";")
    #     except:
    #         initiate_generate = False
    #         self.button_input_folder.setStyleSheet("background-color: rgb(255,255,255,50);\n"
    #         "border: 2px solid #d41e82;\n"
    #         "border-radius: 15px;\n"
    #         "color: #ffffff;\n"
    #         "font: 25px \"Dense\";")

    try:
        print(window_callback.output_folder)
        if window_callback.output_folder == "":
            initiate_generate = False
            self.button_output_folder.setStyleSheet("background-color: rgb(255,255,255,50);\n"
            "border: 2px solid #d41e82;\n"
            "border-radius: 15px;\n"
            "color: #ffffff;\n"
            "font: 25px \"Dense\";")
        else:
            self.button_output_folder.setStyleSheet("background-color: rgb(255,255,255,50);\n"
            "border: 2px solid #ffffff;\n"
            "border-radius: 15px;\n"
            "color: #ffffff;\n"
            "font: 25px \"Dense\";")
    except:
        initiate_generate = False
        self.button_output_folder.setStyleSheet("background-color: rgb(255,255,255,50);\n"
        "border: 2px solid #d41e82;\n"
        "border-radius: 15px;\n"
        "color: #ffffff;\n"
        "font: 25px \"Dense\";")

    if window == "dream_on":
        if dream_on_window.input_frames_amount == "":
            initiate_generate = False
            self.input_frames_amount.setStyleSheet("background-color: rgb(255,255,255,50);\n"
            "border: 2px solid #d41e82;\n"
            "border-radius: 10px;\n"
            "color: #ffffff;\n"
            "font: "+font_size+" \"Dense\";")
        else:
            self.input_frames_amount.setStyleSheet("background-color: rgb(255,255,255,50);\n"
            "border: 2px solid #ffffff;\n"
            "border-radius: 10px;\n"
            "color: #ffffff;\n"
            "font: "+font_size+" \"Dense\";")
    
    return initiate_generate