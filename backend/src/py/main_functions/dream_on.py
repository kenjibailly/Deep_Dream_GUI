'''
Some info on various layers, so you know what to expect
depending on which layer you choose:

layer 1: wavy
layer 2: lines
layer 3: boxes
layer 4: circles?
layer 6: dogs, bears, cute animals.
layer 7: faces, buildings
layer 8: fish begin to appear, frogs/reptilian eyes.
layer 10: Monkies, lizards, snakes, duck

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
import cv2
import os
import random as random
import glob

def start_dream_on(input_layer, iterations, recursive_level, frames_amount, input_file, output_folder, self):

    # Folders into variables
    dream_on_output_folder = ""+output_folder+"/"
    temp_folder = 'backend\src\etc\deep_dream_images_temp'
    # dream_on_image_input_folder = input_folder

    print(" ")
    print("------------------------------------------------------")
    print('Cleaning up temporary files...')
    print("------------------------------------------------------")

    print("removing... "+temp_folder+"/0.png")
    if os.path.exists('{}'.format('{}/0.png'.format(temp_folder))):
        os.remove('{}'.format('{}/0.png'.format(temp_folder)))

    print("Choose a layer or experiment by choosing another layer.")
    print("------------------------------------------------------")
    print("layer 1: wavy")
    print("layer 2: lines")
    print("layer 3: boxes")
    print("layer 4: circles?")
    print("layer 6: dogs, bears, cute animals")
    print("layer 7: faces, buildings")
    print("layer 8: fish begin to appear, frogs/reptilian eyes.")
    print("layer 10: Monkey's, lizards, snakes, duck")
    print("------------------------------------------------------")

    # Ask input from the user
    layer_tensor = model.layer_tensors[int(input_layer)] 
    iterations = int(iterations)
    recursive_level = int(recursive_level)

    if recursive_level == '0':
        print('Recursive Level 0 cannot be used for "Dream On", Recursive Level set to minimum: 1')

    amount_of_frames = frames_amount
    print("------------------------------------------------------")

    if recursive_level == 0:
        recursive_level = 1

    # Check and convert if img is RGBA > RGB
    img = PIL.Image.open(r'{}'.format(input_file))
    print('bit depth :', img.mode)

    if img.mode == "RGBA":
        rgba_image = PIL.Image.open(input_file)
        rgb_image = rgba_image.convert('RGB')
        rgb_image.save('{}/{}.png'.format(temp_folder, 0))
    else:
        img = PIL.Image.open(input_file)
        img.save('{}/{}.png'.format(temp_folder, 0))

    # file = input_file
    file = [] 
    for (path, dirnames, filenames) in os.walk(temp_folder):
        file.extend(os.path.join(path, name) for name in filenames)

    file_check = file[0].split('\\')
    check_file = file_check[-1]
    if check_file == ".gitignore":
        del file[0]

    file = file[0]


    img_file=PIL.Image.open(file)
    w,h=img_file.size    # w=Width and h=Height
    x_size = w
    y_size = h

    created_count = 0
    max_count = int(amount_of_frames)


    print("Starting Deep Dream with chosen parameters:")
    # Show the user the parameters being used
    print('Layer = {}'.format(input_layer))
    print('Iterations = {}'.format(iterations))
    print('Recursive Level = {}'.format(recursive_level))
    print('Amount of frames = {}'.format(amount_of_frames))
    print("------------------------------------------------------")

    # Start progress bar as indication generate button worked, reset progress bar but don't show
    self.completed = 5
    self.progress.setValue(self.completed)
    self.completed = 0

    for i in range(0, 9999999999999999):

        if os.path.isfile('{}/img_{}.png'.format(dream_on_output_folder, i+1)):
            print('{} already exists, continuing along...'.format(i+1))

        else:

            img_result = load_image(filename='{}'.format(file))

            # this impacts how quick the "zoom" is
            x_trim = 2
            y_trim = 1

            img_result = img_result[0+y_trim:y_size-y_trim, 0+x_trim:x_size-x_trim]
            img_result = cv2.resize(img_result, (x_size, y_size))

            # Use these to modify the general colors and brightness of results.
            # results tend to get dimmer or brighter over time, so you want to
            # manually adjust this over time.

            # +2 is slowly dimmer
            # +3 is slowly brighter
            img_result[:, :, 0] += 2  # reds
            img_result[:, :, 1] += 2  # greens
            img_result[:, :, 2] += 2  # blues

            img_result = np.clip(img_result, 0.0, 255.0)
            img_result = img_result.astype(np.uint8)

            img_result = recursive_optimize(layer_tensor=layer_tensor,
                                            image=img_result,
                                            num_iterations=iterations,
                                            step_size=1.0,
                                            rescale_factor=0.7,
                                            num_repeats=recursive_level,
                                            blend=0.2)

            img_result = np.clip(img_result, 0.0, 255.0)
            img_result = img_result.astype(np.uint8)
            result = PIL.Image.fromarray(img_result, mode='RGB')
            result.save('{}{}.png'.format(dream_on_output_folder, i+1))
            print('')
            print('Frame {}{}.png saved.'.format(dream_on_output_folder, i+1))

            self.completed += 100/max_count
            self.progress.setValue(self.completed)


            created_count += 1
            if created_count > max_count -1:

                print('')
                print("------------------------------------------------------")
                print('Dream On finished. Check out {}'.format(dream_on_output_folder))
                print("------------------------------------------------------")
                break