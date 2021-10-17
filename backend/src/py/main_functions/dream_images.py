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
layer 10: monkey's, lizards, snakes, duck

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
# import PIL.Image as Image
import random as random
import os

def start_dream_images(input_layer, iterations, recursive_level, input_file, output_folder, self):
    # Folders into variables
    deep_dream_images_ouput_folder = ""+output_folder+"/"
    layer_tensor = model.layer_tensors[int(input_layer)]
    iterations = int(iterations)
    recursive_level = int(recursive_level)
    temp_folder = 'backend\src\etc\deep_dream_images_temp'

    # files = input_file

    frames_amount = len(input_file) # Amount of images stored in the folder
    print('Files ({}):'.format(len(input_file)))

    # Show the user the parameters being used

    print("Starting Deep Dream with chosen parameters:")
    print("Chosen parameters: ")
    print('Layer = {}'.format(input_layer))
    print('Iterations = {}'.format(iterations))
    print('Recursive Level = {}'.format(recursive_level))
    print("------------------------------------------------------")

    # Start progress bar as indication generate button worked, reset progress bar but don't show
    self.completed = 5
    self.progress.setValue(self.completed)
    self.completed = 0


    # Push all images to temp folder and convert rgba images to rgb 
    for i in range(frames_amount):
        #Load the img    
        img = PIL.Image.open(r'{}'.format(input_file[i]))
        print('bit depth :', img.mode)

        if img.mode == "RGBA":
            rgba_image = PIL.Image.open(input_file[i])
            rgb_image = rgba_image.convert('RGB')
            rgb_image.save('{}/{}.png'.format(temp_folder, i))
        else:
            img = PIL.Image.open(input_file[i])
            img.save('{}/{}.png'.format(temp_folder, i))

    files = [] 
    folders = [] 
    for (path, dirnames, filenames) in os.walk(temp_folder):
        folders.extend(os.path.join(path, name) for name in dirnames)
        files.extend(os.path.join(path, name) for name in filenames)

    file_check = files[0].split('\\')
    check_file = file_check[-1]
    if check_file == ".gitignore":
        del files[0]

    for i in range(0, 9999999999999999):

        if i+1 > frames_amount:

            print(" ")
            print("------------------------------------------------------")
            print('Cleaning up temporary files...')
            print("------------------------------------------------------")

            for i in range(frames_amount):
                print("removing... "+files[i])
                if os.path.exists('{}'.format(files[i])):
                    os.remove('{}'.format(files[i]))
                i += 1


            print(" ")
            print("------------------------------------------------------")
            print('All pictures have been saved, Deep Dream is done.')
            print('Check out {} '.format(deep_dream_images_ouput_folder))
            print("------------------------------------------------------")

            break

        else:
            # print(i)
            # print(files[i])
            # file_name_and_folder = files[i]  # Load file name from files array
            
            # file_name = file_name_and_folder.split('/')[1] # Split the file to get just the name of the file with the extension

            img_result = load_image(str(files[i])) # Load the image

            img_result = recursive_optimize(layer_tensor=layer_tensor, image=img_result,
                            # how clear is the dream vs original image        
                            num_iterations = iterations, step_size=1.0, rescale_factor=0.5,
                            # How many "passes" over the data. More passes, the more granular the gradients will be.
                            num_repeats = recursive_level, blend=0.2)

            img_result = np.clip(img_result, 0.0, 255.0)
            img_result = img_result.astype(np.uint8)
            result = PIL.Image.fromarray(img_result, mode='RGB')

            result.save('{}{}.png'.format(deep_dream_images_ouput_folder, i)) # Save the image

            # Output to user
            print("")
            print('Picture {} saved.'.format(files[i]))

            self.completed += 100/frames_amount
            self.progress.setValue(self.completed)

            i += 1

            if frames_amount == 1:
                result.show()