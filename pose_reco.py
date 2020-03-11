import sys
sys.path.append('../../python');

from openpose import pyopenpose as op


import cv2
import os
from sys import platform
import argparse
import time

parser = argparse.ArgumentParser()
parser.add_argument("--video", default="examples/media/video.mp4", help="Read input video (avi).")
parser.add_argument("--no_display", default=False, help="Enable to disable the visual display.")
args = parser.parse_known_args()

params = dict()
params["model_folder"] = "../../../models/" #"MODELS_PATH"
params["net_resolution"] = "-1x160"
params["model_pose"] = "BODY_25"
params["disable_multi_thread"] = "false"
params["num_gpu"] = op.get_gpu_number()

# just processing the cmd arguments
for i in range(0, len(args[1])):
    curr_item = args[1][i]
    if i != len(args[1])-1: next_item = args[1][i+1]
    else: next_item = "1"
    if "--" in curr_item and "--" in next_item:
        key = curr_item.replace('-','')
        if key not in params:  params[key] = "1"
    elif "--" in curr_item and "--" not in next_item:
        key = curr_item.replace('-','')
        if key not in params: params[key] = next_item

try:
    opWrapper = op.WrapperPython() # Constructing OpenPose object 
    opWrapper.configure(params)  # configure paramters
    opWrapper.start() 

    videoPath = args[0].video # set video path

    start = time.time()
    
    cap = cv2.VideoCapture(videoPath) # opencv object

    while cap.isOpened():
        grabbed, frame = cap.read() # read in the frames 

        if frame is None or not grabbed:
            print("Finish reading video frames...")
            break

        datums = [] # a list of all data points

        datum = op.Datum() # initalise 
        datum.cvInputData = frame
        datums.append(datum)
        opWrapper.waitAndEmplace([datums[-1]]) # analyse

        datum = datums[0] # put it on GPU 0
        opWrapper.waitAndPop([datum]) # analyse key points

        print("Body keypoints: \n" + str(datum.poseKeypoints))

        if not args[0].no_display:
            cv2.imshow("output", datum.cvOutputData)
            key = cv2.waitKey(1)
            if key == 27: break

    end = time.time()
except Exception as e:
    sys.exit(-1)