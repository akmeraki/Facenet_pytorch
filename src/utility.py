import os 
import numpy as np
import matplotlib.pyplot as plt
import PIL
import torchvision
from collections import Counter
from PIL import Image
from mpl_toolkits.axes_grid1 import ImageGrid


# Visualize the images in a Grid 
def show_img(dataloader):
    """ Built in pytorch function to display images in a grid """
    
    images, labels = next(iter(dataloader))
    
    fig = plt.figure(figsize=(20, 20))
    grid = torchvision.utils.make_grid(images)

    plt.imshow(grid.numpy().transpose((1, 2, 0)))
    plt.axis('off')
    plt.title('VGGface2 Images')