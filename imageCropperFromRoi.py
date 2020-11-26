import numpy as np
import os
from PIL import Image
import pandas as pd

#importing .csv files contain ROI coordinates
dfGlovesLabels = pd.read_csv('dataset/gloves_labels.csv', sep=',')
dfHandsLabels = pd.read_csv('dataset/hands_labels.csv', sep=',')
#datadir
DATADIR = "C:/Users/Mehmet/glovesDetection/dataset"
SAVEDIR = "C:/Users/Mehmet/glovesDetection/dataset/cropped"
#folder names
CATEGORIES = ["hands","gloves"]

for category in CATEGORIES:
    path = os.path.join(DATADIR,category)
    savepath = os.path.join(SAVEDIR,category)
    if category=="hands":
    	df = dfHandsLabels
	elif category == "gloves": 
		df = dfGlovesLabels

    for img in os.listdir(path):
    	image = Image.open(os.path.join(path,img))
    	coordinates= df.loc[df['filename'] == img,"xmin":"ymax"].values[0]#extracting ROI coordinates
    	img_cropped = image.crop(coordinates)
    	img_cropped.save(os.path.join(SAVEDIR,category),format="jpeg")
    	break
    break