from backend.src.py.functions.deepdreamer import model, load_image, recursive_optimize
import numpy as np
import PIL.Image
import random as random
import os
import cv2
import glob
import backend.src.py.functions.start_deep_dream as start_deep_dream
import json

def initiate_start(deep_dream_frames_folder, input_layer, iterations, recursive_level, input_file, output_folder, self):

    print("------------------------------------------------------")
    print("Cleaning previous session...")
    print("------------------------------------------------------")
    clean_up_deep_frames = glob.glob('backend/frames_to_deep_dream/*')
    for file in clean_up_deep_frames:
        os.remove(file)
    print("Previous session cleaned.")
    print("------------------------------------------------------")
    print("Choose a layer or experiment by choosing another layer.")
    print("------------------------------------------------------")
    print("layer 1: wavy")
    print("layer 2: lines")
    print("layer 3: boxes")
    print("layer 4: circles?")
    print("layer 5: eyes")
    print("layer 6: dogs, bears, cute animals")
    print("layer 7: faces, buildings")
    print("layer 8: fish begin to appear, frogs/reptilian eyes.")
    print("layer 10: Monkey's, lizards, snakes, duck")
    print("------------------------------------------------------")

    # Strings to ints
    layer_tensor = model.layer_tensors[int(input_layer)]    
    iterations = int(iterations)
    recursive_level = int(recursive_level)

    print("Starting video frames extraction")
    print("------------------------------------------------------")

    # Find the video name
    # video_names = [] 
    # video_folders = [] 
    # for (path, dirnames, filenames) in os.walk(input_folder):
    #     video_folders.extend(os.path.join(path, name) for name in dirnames)
    #     video_names.extend(os.path.join(path, name) for name in filenames)
    # video_name = video_names[0] # Video name

    video_name = input_file

    vidcap = cv2.VideoCapture(video_name) # Get Video
    fps = int(vidcap.get(cv2.CAP_PROP_FPS)) # Get FPS
    total_frames = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
    success,image = vidcap.read() # read frame
    count = 0
    while success: # While reading and extracting video
        cv2.imwrite("backend/src/etc/frames_to_deep_dream/%d.png" % count, image)     # save frame as png file      
        success,image = vidcap.read() # read new frame
        print('Frame {} done.'.format(count))
        count += 1

    # Start progress bar as indication generate button worked, reset progress bar but don't show
    self.completed = 10
    self.progress.setValue(self.completed)

    print("------------------------------------------------------")
    print("Video to frames extraction done.")
    print("------------------------------------------------------")
    print('Video FPS: {}'.format(fps))

    parameters_to_json_file = {
        "fps": fps,
        "input_layer": input_layer,
        "iterations": iterations,
        "recursive_level": recursive_level,
        "total_frames": total_frames,
        "output_folder": output_folder
    }

    with open('backend/src/json/last_parameters.json', 'w') as json_file:
        json.dump(parameters_to_json_file, json_file)

    last_index = 0
    start_deep_dream.start_deep_dream(deep_dream_frames_folder, fps, layer_tensor, input_layer, iterations, recursive_level, last_index, total_frames, output_folder, self)