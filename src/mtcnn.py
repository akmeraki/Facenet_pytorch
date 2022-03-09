
import os
from turtle import shape 
import numpy as np 
from pathlib import Path 
from inspect import ArgSpec
from PIL import Image
from facenet_pytorch import MTCNN
import argparse

""" Extract faces using a MTCNN face detector."""

def valid_ext(ext):
    return ext.lower() in ['.jpg', '.jpeg', '.png']

def detect_and_store(path,final_root_dir,resize_dim):
    """
    Detect face in a image, crop and  store it in a new directory.
    """
    img = Image.open(path) 
    
    mtcnn = MTCNN()

    boxes,_ =  mtcnn.detect(img)
    
    if boxes is None:
        print("No face detected on image", path)

    # Image should only contain one face 

    elif boxes.shape[0] == 1:

        for a,b,c,d in boxes:
            
            path_ = Path(path)
            dst = os.path.join(final_root_dir, os.path.basename(path_.parent.name))
            os.makedirs(dst, exist_ok=True)
            final_name = os.path.join(dst,path_.name)

            try:
                img = img.crop((a,b,c,d))
                img = img.resize((resize_dim,resize_dim), Image.BILINEAR)
                img.save(final_name)
            
            except Exception as e:
                print("Error occurred while saving", final_name)
                print("Error:", str(e))

    else:
        print("Multiple faces detected on image", path)




if __name__ == "__main__":


    parser = argparse.ArgumentParser(description='Face Detection using MTCNN')

    parser.add_argument('--root-dir',type=str,help='absolute path to dataset root dir')
    parser.add_argument('--final-dir',type=str,help='Final absolute root directory to store all the files')   
    parser.add_argument('--resize',type=int,help='Resize the image to a given squared size', default=128)

    args = parser.parse_args()

    final_path = args.final_dir
    
    for root, dirs, files in os.walk(args.root_dir):
        for file in files:
            
            path = os.path.join(root, file)

            if not valid_ext(file[-4:]):
                print(path,'is not valid image. Expected extension: .jpg, .jpeg, .png')
                continue
            detect_and_store(path, final_path, args.resize)

        