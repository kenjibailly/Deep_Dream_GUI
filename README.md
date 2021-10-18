# Contents


1. [Important Notes](#notes)
2. [Info](#info)
3. [Install on Windows](#install)
4. [Stunning UI](#ui)
5. [Development](#development)
6. [Credits](#credits)

‎

# <div id="notes">Important notes</div>

1. This software is made for Windows and for Nvidia CUDA supported devices.
If your graphics card isn't Nvidia CUDA supported, the software should still run fine. 
Instead of using your graphics card, the software will use your CPU. 

2. After opening the app, wait a moment before it opens. It will try to connect your GPU before displaying the user interface.

3. After you pressed "Generate" try not to click inside the window or the program will "stop responding". This means the program is still running in the background, but you won't see the progress bar moving until it has finished.

‎

# <div id="info">Info</div>

The Deep Dream Generator has 4 functions:

## 1. Dream Images

Select one or more images to convert them to deep dream.

## 2. Dream Video

Select a video to convert it to a deep dream video.

## 3. Dream On

Select an image to create multiple deep dream frames with a stepped process to create the deep dream effect. These frames can later be converted to a video using the Images to Video function.

## 4. Images to Video

Select multiple frames to convert them to a video.

‎

# <div id="install">Install on Windows</div>


1. Download the setup in the <a href="https://github.com/kenjibailly/Deep_Dream_GUI/releases/tag/v1.0.0">Releases</a> section on the right.
2. Run the setup and install the software.
3. Run the app and wait a moment.

‎

# <div id="ui">Stunning UI</div>

<img src="backend\src\images\screenshots\main.png">
<img src="backend\src\images\screenshots\1.png">
<img src="backend\src\images\screenshots\2.png">
<img src="backend\src\images\screenshots\3.png">
<img src="backend\src\images\screenshots\4.png">
<img src="backend\src\images\screenshots\help.png">

‎

# <div id="development">Development</div>

This section is only for development purposes of the app.

‎

## 1. Download Python

‎

To download Python, open Command Prompt and type in
    
    python

‎

## 2. Download Anaconda
‎

Download here https://www.anaconda.com/products/individual

‎
## 3. Open Anaconda (Powershell Prompt) and run the following lines of code

‎

    conda create -n tf_gpu_env python=3.9   
    conda activate tf_gpu_env
    conda install tensorflow-gpu -c anaconda
    conda install cudnn -c conda-forge 
    conda install cudatoolkit -c anaconda
    conda install -c conda-forge opencv ffmpeg
    conda install -c conda-forge matplotlib
    conda install -c anaconda pillow
    conda install -c conda-forge glob2

‎

## 4. Activate / Check if Tensorflow is running on your gpu

‎

    python

‎

    import tensorflow as tf
    print('Num GPUs Available', len(tf.config.list_physical_devices('GPU')))
    exit()

‎

## 5. Run the script

‎

    python main.py


‎

# <div id="credits">Credits</div>

- Sentdex: https://github.com/Sentdex
    
    Resources used: https://www.youtube.com/playlist?list=PLQVvvaa0QuDdfN3lrO0NDYxa1JwCYes-E

- Hvass-Labs: https://github.com/Hvass-Labs

    Resources used: https://github.com/Hvass-Labs/TensorFlow-Tutorials

‎



I have coded the rest of the code including the GUI. I also designed the GUI.
I have learned Python just for this project, so to speak this is my first Python project.