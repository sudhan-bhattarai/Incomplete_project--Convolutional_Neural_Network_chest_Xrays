# %%
'''Libraries'''

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf


# %%
'''Load data'''

df = pd.read_csv(r'Data_Entry_2017_v2020.csv')
df.head()

# %%

# %%
'''Load images'''

images = []
path = 'C:\\Users\\stan\\chest_images\\'
dir = os.listdir(path)
for image in dir:
    im_dir = path + str(image)
    images.append(tf.keras.preprocessing.image.load_img(im_dir))

# %%

'''Image preprocessing'''



# %%
