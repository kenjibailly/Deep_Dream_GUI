import cv2
import os

def create_video(deep_dream_frames_folder, frames_amount, frame_width, frame_height, fps, output_folder):

    # deep_dream_frames_folder = "deep_dream_frames/"

    save_path = ""+output_folder+"/"
    output_name = 'output_video'

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')

    out = cv2.VideoWriter('{}{}.mp4'.format(save_path, output_name),fourcc, fps, (frame_width,frame_height))

    for i in range(frames_amount):
        img_path = os.path.join(deep_dream_frames_folder,'{}.png'.format(i))
        # img_path = os.path.join(files[i])
        print(img_path)
        frame = cv2.imread(img_path)
        out.write(frame)

    out.release()

    print("------------------------------------------------------")
    print('Video has been saved to the "video_output" folder.')
    print("------------------------------------------------------")