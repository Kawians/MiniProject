# MiniProject
Introduction: 
 In this project we have decided to build a model using Tensorflow for the Paper,rock and scissor play, the motivation for this project comes from the idea that this game is mainly based on the player choice of scissor, rock or paper and this enables us to model this game and enhance our image classification model building.
The model would be the CNN model (Convolutional Neural Network) which is a DL algorithm
Dataset:
The TensorFlow Datasets library provides a collection of datasets that are readily compatible with TensorFlow.
To build our model, we utilized a dataset available in the TensorFlow library. This dataset contained a collection of images representing the hand gestures for Rock, Paper, and Scissors.
Model/Methodology:
Our CNN model consisted of five layers. The first layer comprised 16 filters with a kernel size of three by three. This choice of architecture allowed the model to extract relevant features from the input images effectively. We applied max pooling and flattening techniques to downsample and reshape the obtained features. Finally, we passed the flattened features to a dense layer to obtain the output corresponding to the three possible images: Scissors Rock and Paper.
