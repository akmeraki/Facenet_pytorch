import argparse
import glob
import pandas as pd 
import os 
import time 
import multitasking as mt 




def generate_set(data,process_name,filename):

    print("The number of files:", len(data))













if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description='Face Recognition using Triplet Loss')

    parser.add_argument('--root-dir',type=str,help='path to dataset root dir')
    parser.add_argument('--final-file',type=str,help='Final file name')
    
    args = parser.parse_args()

    root_dir = args.root_dir
    file_name = args.final_file

    # Create a list of all image directories
    files = glob.glob(root_dir+'/*/*')
    
    div = len(files) // 4
    
    # Divide directories to 4 chunks 
    chunk1 = files[0:div]
    chunk2 = files[div:2*div]
    chunk3 = files[2*div:3*div]
    chunk4 = files[3*div:]
    
    


























