'''
Some info on various layers, so you know what to expect
depending on which layer you choose:

layer 1: wavy
layer 2: lines
layer 3: boxes
layer 4: circles?
layer 5: eyes
layer 6: dogs, bears, cute animals.
layer 7: faces, buildings
layer 8: fish begin to appear, frogs/reptilian eyes.
layer 10: Monkey's, lizards, snakes, duck

Choosing various parameters like num_iterations, rescale,
and num_repeats really varies on which layer you're doing.


We could probably come up with some sort of formula. The
deeper the layer is, the more iterations and
repeats you will want.

Layer 3: 20 iterations, 0.5 rescale, and 8 repeats is decent start
Layer 10: 40 iterations and 25 repeats is good. 
'''

from backend.src.py.functions.deepdreamer import model, load_image, recursive_optimize
import numpy as np
import PIL.Image
import random as random
import os
import cv2
import glob
import backend.src.py.functions.dream_video_start as dream_video_start
import backend.src.py.functions.start_deep_dream as start_deep_dream
import json

def start_dream_video(input_layer, iterations, recursive_level, input_folder, output_folder, self):

    # Folders into variables
    deep_dream_frames_folder = "backend/src/etc/deep_dream_frames/"
    frames_to_deep_dream_folder = "backend/src/etc/frames_to_deep_dream/"

    print("------------------------------------------------------")
    print("Checking if video hasn't fully finished yet")
    print("------------------------------------------------------")

    deep_dream_files = [] 
    for (path, dirnames, filenames) in os.walk(deep_dream_frames_folder):
        deep_dream_files.extend(os.path.join(path, name) for name in filenames)
    deep_dream_files = len(deep_dream_files)

    frames_files = [] 
    for (path, dirnames, filenames) in os.walk(frames_to_deep_dream_folder):
        frames_files.extend(os.path.join(path, name) for name in filenames)
    frames_to_del = frames_files

    # Start progress bar as indication generate button worked
    self.completed = 5
    self.progress.setValue(self.completed)

    dream_video_start.initiate_start(deep_dream_frames_folder, input_layer, iterations, recursive_level, input_folder, output_folder, self)


def resume(self):

    deep_dream_frames_folder = "backend/src/etc/deep_dream_frames/"
    frames_to_deep_dream_folder = "backend/src/etc/frames_to_deep_dream/"

    print("------------------------------------------------------")
    print("Checking if video hasn't fully finished yet")
    print("------------------------------------------------------")

    deep_dream_files = [] 
    for (path, dirnames, filenames) in os.walk(deep_dream_frames_folder):
        deep_dream_files.extend(os.path.join(path, name) for name in filenames)
    deep_dream_files = len(deep_dream_files)

    frames_files = [] 
    for (path, dirnames, filenames) in os.walk(frames_to_deep_dream_folder):
        frames_files.extend(os.path.join(path, name) for name in filenames)
    frames_to_del = frames_files

    # Delete the frames up to the length
    if deep_dream_files > 0:
        print("Last video hasn't been finished. Starting where left of...")
        print("------------------------------------------------------")
        for i in range(deep_dream_files):
            print("removing... "+frames_to_del[i])
            if os.path.exists('{}'.format(frames_to_del[i])):
                os.remove('{}'.format(frames_to_del[i]))
            i += 1
        
        # Check the last parameters used to enable them again
        with open('backend/src/json/last_parameters.json') as file:
            last_parameters = json.load(file)
        print("Last used parameters loaded.")

        # Loading variables
        fps = last_parameters["fps"]
        input_layer = last_parameters["input_layer"]
        iterations = last_parameters["iterations"]
        recursive_level = last_parameters["recursive_level"]
        total_frames = last_parameters["total_frames"]
        layer_tensor = model.layer_tensors[int(input_layer)]
        output_folder = last_parameters["output_folder"]

        print("------------------------------------------------------")
        print('Video FPS: {}'.format(fps))

        last_index = deep_dream_files 

        # Progress bar, 80 because 10 init and 10 end
        self.completed += 5
        self.progress.setValue(self.completed)

        start_deep_dream.start_deep_dream(deep_dream_frames_folder, fps, layer_tensor, input_layer, iterations, recursive_level, last_index, total_frames, output_folder, self)
 