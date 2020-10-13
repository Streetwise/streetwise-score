#!/usr/bin/env python
# coding: utf-8

# # Scoring
# Produce a geoJSON file containing the trueskill score associated to the perceived safety of a certain location (by analyzing pictures of that location)

# ### Imports

# In[1]:


# Import libraries
import trueskill
import tensorflow
from tensorflow.keras.models import Model, Sequential, load_model
import matplotlib.pyplot as plt
import numpy as np
from tensorflow.keras.applications.resnet50 import preprocess_input
import cv2
import json
import os
from IPython.display import display, Markdown, Latex
import logging
import random
import csv
import itertools

logger = tensorflow.get_logger()
logger.setLevel(logging.ERROR)


# ### Variables
# Adjust these to reflect the desired input and output files

# In[2]:


network_path = "../../../net/scratch/dottip/mlsw/models/CROWDSOURCING_27k_FULLDATASET_finetuned_lr-5_decreasing_Conv8MaxPool3x3B4lr0.002siameselayer1epo_then_augmentedx4lr0.000000120epochs_thenunfrozenandfinetunedagain.h5"
training_path = "../../../net/dataset/dottip/mlsw/crowdsourcing/enhanced_preproc/"
data_path = "../../../net/dataset/dottip/mlsw/scoring/"
csv_name = "zurich-scoring.csv"
img_folder = "Zurich/"
output_file = "safety_scores/zurich_internalcomp_p1.json"
training_size = 30


# ### Setup
# Select which GPU to use when several are available. This can be removed when few GPUs are available

# In[3]:


os.environ['CUDA_VISIBLE_DEVICES'] = '2'


# Load pretrained ML model to compare image couples

# In[4]:


siamese_net = load_model(network_path)


# ### Data loading
# Create dictionary containing images to be scored from csv file, and associated metadata

# In[7]:


metadata = {}
with open(data_path+csv_name) as f:
    csv_data = list(csv.reader(f))
    csv_data = csv_data[1:len(csv_data)//3]
    for r in csv_data:
        metadata[r[0]] = {"coord": [r[2], r[3]], "score": trueskill.Rating()}


# Load and preprocess images to be scored

# In[8]:

print("loading images")
images = {}
for imName in metadata.keys():
    im = cv2.imread(data_path+img_folder+imName+".jpg")

    if im is not None:
        im = cv2.resize(im, (224, 224), interpolation=cv2.INTER_CUBIC)
        im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)

        images[imName] = preprocess_input(im)

# Keep only the "mu" value of the trueskill scores

# In[9]:


# Experimental: compare the analyzed images                    
print("Loading left and right")
nComp = 30
length = 20
i = 0
endi = len(images)/length

for l in range(0, len(images), length):
    leftIds = [tId for tId in random.sample(images.keys(), nComp) for u in range(0, length)]
    rightIds = [tId for tId in list(images.keys())[l:l+length] for u in range(0, nComp)]

    leftIds = leftIds[:len(rightIds)] # To prevent different dimesions
    
    left = np.array([images[tId] for tId in leftIds])
    right = np.array([images[tId] for tId in rightIds])

    result = siamese_net.predict([left, right])

    for j,r in enumerate(result):
        if r[1]>r[0]: #left wins
            metadata[leftIds[j]]["score"] ,metadata[rightIds[j]]["score"] = trueskill.rate_1vs1(metadata[leftIds[j]]["score"], metadata[rightIds[j]]["score"])
        else: #right wins
            metadata[rightIds[j]]["score"], metadata[leftIds[j]]["score"] = trueskill.rate_1vs1(metadata[rightIds[j]]["score"], metadata[leftIds[j]]["score"])
    
    i+=1
    print(f'Progress: {i/endi*100}', end="\r")

# In[10]:


results = {}
mink = list(metadata.keys())[0]
maxk = list(metadata.keys())[0]

for k in metadata.keys():
    metadata[k]["score"] = metadata[k]["score"].mu
    
    if metadata[k]["score"] > metadata[maxk]["score"]:
        maxk = k
    if metadata[k]["score"] < metadata[mink]["score"]:
        mink = k  


# Transform data to geoJSON format

# In[12]:


geojson = {"type": "FeatureCollection",
  "features":[]}

for k, v in metadata.items():
    geojson["features"].append({"type": "Feature",
                   "properties": {
                       "name": k,
                       "score": v["score"]
                   },
                   "geometry": {
                       "type": "Point",
                       "coordinates": [float(v["coord"][1]), float(v["coord"][0])]
                   }})


# Save geoJSON data to external json file

# In[13]:


with open(output_file, 'w') as fp:
    json.dump(geojson, fp)


# In[ ]:




