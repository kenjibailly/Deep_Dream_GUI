import cv2
import os
import PIL.Image

def start_video(input_file, output_folder, fps, self):

    save_path = output_folder
    output_name = 'output_video'
    # deep_dream_images_folder = input_folder


    # print('Do you want to render the video from the: ')
    # print('1. dream_images.py')
    # print('2. dream_on.py')
    # dream_images_or_dream_on = input('Choose 1 or 2: ')

    # if dream_images_or_dream_on == '1':
    #     deep_dream_images_folder = 'deep_dream_images_output'
    #     print('Important Note: All your images have to be the same width and height to match the video dimensions.')
    # elif dream_images_or_dream_on == '2':
    #     deep_dream_images_folder = 'dream_on_images_output'
    # else:
    #     print('Wrong number, exiting script.')
    #     exit()

    files = input_file
    # files = [] 
    # folders = [] 
    # for (path, dirnames, filenames) in os.walk(deep_dream_images_folder):
    #     folders.extend(os.path.join(path, name) for name in dirnames)
    #     files.extend(os.path.join(path, name) for name in filenames)

    files_length = len(files)

    # determine width and height of first image
    img=PIL.Image.open(files[0])
    w,h=img.size    # w=Width and h=Height
    first_image_width = w
    first_image_height = h

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')

    fps = int(fps)

    if fps == "":
        fps = 24
    else:
        fps = int(fps)

    out = cv2.VideoWriter('{}/{}.mp4'.format(save_path, output_name),fourcc, fps, (first_image_width,first_image_height))

    # Start progress bar as indication generate button worked, reset progress bar but don't show
    self.completed = 5
    self.progress.setValue(self.completed)

    for i in range(files_length):
        # img_path = os.path.join(deep_dream_images_folder,'{}'.format(files[i]))
        self.completed += 100/files_length
        self.progress.setValue(self.completed)
        img_path = files[i]
        print(img_path)
        frame = cv2.imread(img_path)
        out.write(frame)

    out.release()
    
    self.completed = 100
    self.progress.setValue(self.completed)
    print("------------------------------------------------------")
    print('Video has been saved to the "video_output" folder.')
    print("------------------------------------------------------")