# **Behavioral Cloning**

## Writeup Template

### Dependencies
This lab requires:

* [CarND Term1 Starter Kit](https://github.com/udacity/CarND-Term1-Starter-Kit)

where I update tensorflow and keras
* tensorflow-gpu==1.2
* keras==2.1.2

---

**Behavioral Cloning Project**

The goals / steps of this project are the following:
* Use the simulator to collect data of good driving behavior
* Build, a convolution neural network in Keras that predicts steering angles from images
* Train and validate the model with a training and validation set
* Test that the model successfully drives around track one without leaving the road
* Summarize the results with a written report


[//]: # (Image References)

[image1]: ./examples/placeholder.png "Model Visualization"
[image2]: ./examples/left_center_right_show.jpg "left_center_right_show"
[image3]: ./examples/fliplr.jpg "fliplr Image"
[image4]: ./examples/shear.jpg "shear Image"
[image5]: ./examples/gamma.jpg "gamma Image"
[image6]: ./examples/placeholder_small.png "Normal Image"
[image7]: ./examples/placeholder_small.png "Flipped Image"

## Rubric Points
### Here I will consider the [rubric points](https://review.udacity.com/#!/rubrics/432/view) individually and describe how I addressed each point in my implementation.  

---
### Files Submitted & Code Quality

#### 1. Submission includes all required files and can be used to run the simulator in autonomous mode

My project includes the following files:
* model.py containing the script to create and train the model
* drive.py for driving the car in autonomous mode
* model.h5 containing a trained convolution neural network
* writeup_report.md or writeup_report.pdf summarizing the results

#### 2. Submission includes functional code
Using the Udacity provided simulator and my drive.py file, the car can be driven autonomously around the track by executing
```sh
python drive.py model.h5
```

#### 3. Submission code is usable and readable

The model.py file contains the code for training and saving the convolution neural network. The file shows the pipeline I used for training and validating the model, and it contains comments to explain how the code works.

### Model Architecture and Training Strategy

#### 1. An appropriate model architecture has been employed


My model consists of a convolution neural network (model.py lines 31-60) with:
- 3 convolution layers with 5x5 filter sizes
- 2 convolution layers
- 3 pooling layers
- 3 dropout layers
- 1 flatten layters
- 5 dense layers

The model includes RELU layers to introduce nonlinearity ,
- and the data is normalized in the model using a Keras lambda layer (code line 32),
- and the data is cropped in model (code line 33),
- and is resized (code line 34).

#### 2. Attempts to reduce overfitting in the model

The model contains dropout layers in order to reduce overfitting.

The model was trained and validated on different data sets to ensure that the model was not overfitting (code line 13).

The model was tested by running it through the simulator and ensuring that the vehicle could stay on the track.

#### 3. Model parameter tuning

The model used an adam optimizer, and considering the speed of training and the use of dropout, I used the learning_rate 1e3.
After several trial, dropout rate 0.3,0.2,0.1 are selected.

#### 4. Appropriate training data

I used the data offered by Udacity and random 90% as training data and the others as validation data.


For details about how I created the training data, see the next section.

### Model Architecture and Training Strategy

#### 1. Solution Design Approach

The overall strategy for deriving a model architecture was to use a pretrained model and then tune step by step.

My first step was to use a convolution neural network model of NVIDIA's End to End Learning for Self-Driving Cars paper.

In order to gauge how well the model was working, I split my image and steering angle data into a training and validation set. This implied that the model was a little underfitting.

To combat the underfitting, I modified the model by add polling so that the model was a little overfitting.

Then I add dropout into the model.

At the end of the process, the vehicle is able to drive autonomously around the track without leaving the road.

#### 2. Final Model Architecture

The final model architecture (model.py lines 31-61) consisted of a convolution neural network with the following layers and layer sizes.

Here is a visualization of the architecture:
```
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
lambda_1 (Lambda)            (None, 160, 320, 3)       0         
_________________________________________________________________
cropping2d_1 (Cropping2D)    (None, 90, 320, 3)        0         
_________________________________________________________________
lambda_2 (Lambda)            (None, 64, 64, 3)         0         
_________________________________________________________________
conv2d_1 (Conv2D)            (None, 32, 32, 24)        1824      
_________________________________________________________________
max_pooling2d_1 (MaxPooling2 (None, 31, 31, 24)        0         
_________________________________________________________________
dropout_1 (Dropout)          (None, 31, 31, 24)        0         
_________________________________________________________________
conv2d_2 (Conv2D)            (None, 16, 16, 36)        21636     
_________________________________________________________________
max_pooling2d_2 (MaxPooling2 (None, 15, 15, 36)        0         
_________________________________________________________________
dropout_2 (Dropout)          (None, 15, 15, 36)        0         
_________________________________________________________________
conv2d_3 (Conv2D)            (None, 8, 8, 48)          43248     
_________________________________________________________________
max_pooling2d_3 (MaxPooling2 (None, 7, 7, 48)          0         
_________________________________________________________________
dropout_3 (Dropout)          (None, 7, 7, 48)          0         
_________________________________________________________________
conv2d_4 (Conv2D)            (None, 7, 7, 64)          27712     
_________________________________________________________________
max_pooling2d_4 (MaxPooling2 (None, 6, 6, 64)          0         
_________________________________________________________________
conv2d_5 (Conv2D)            (None, 6, 6, 64)          36928     
_________________________________________________________________
max_pooling2d_5 (MaxPooling2 (None, 5, 5, 64)          0         
_________________________________________________________________
flatten_1 (Flatten)          (None, 1600)              0         
_________________________________________________________________
dense_1 (Dense)              (None, 1164)              1863564   
_________________________________________________________________
dense_2 (Dense)              (None, 100)               116500    
_________________________________________________________________
dense_3 (Dense)              (None, 50)                5050      
_________________________________________________________________
dense_4 (Dense)              (None, 10)                510       
_________________________________________________________________
dense_5 (Dense)              (None, 1)                 11        
=================================================================
Total params: 2,116,983
Trainable params: 2,116,983
Non-trainable params: 0
_________________________________________________________________

```


#### 3. Creation of the Training Set & Training Process

To capture good driving behavior, based on the data provided by Udacity, I used the following data augmentation.

- left, center, right image show

![alt text][image2]

- random fliplr

![fliplr][image3]
- random shear

![shear][image4]
- random gamma correction

![gamma][image5]


I finally randomly shuffled the data set and put 90% of the data into a training set.
I used this training data for training the model.
I finally randomly shuffled the data set and put 10% of the data into a validation set.
The validation set helped determine if the model was over or under fitting.

The ideal number of epochs was 5. I used an adam optimizer with learning rate 1e3 considering the speed of the model training.
