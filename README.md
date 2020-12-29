# chest_x-ray_disease_classification

This project is about utilizing real life images to draw useful insights.
I found a dataset of Xray images for the patients with Chest diseases (reference at the bottom).
This project utilizes that dataset for two purposes.
First, to classify the diseases based on the images available.
Second, to combine the image input with other numeric inputs to quantify the prognosis measure of a patient.
That is,
1. Convolutional neural network (CNN) is to classify images based on images only. (xrays.py)
2. Deep neural network (DNN) + CNN together to classify the images with better precision. (xraysANDnumeric.py)
3. DNN + DNN with linear distinctive and augumented output to locate a specific prognosis period projection of a patient. (Ongoing)
