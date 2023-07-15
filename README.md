# MiniProject
Introduction: 
 In this project we have decided to build a model for the Paper,rock and scissor game. The motivation for this project comes from the idea that this game is mainly based on the player choice of scissor, rock or paper and this enables us to model this game using image classification. In fact, the idea is to capture the player hand's gesture and predict if it is rock, paper or scissors, and then make a random guess by computer and see which one wins.<br>
Dataset:
As we are aware, the TensorFlow Datasets library provides a collection of datasets that are readily compatible with TensorFlow. To build our model, we utilized the rock paper scissors dataset available in the TensorFlow library. This dataset contained a collection of images representing the hand gestures for Rock, Paper, and Scissors.<br>
Model/Methodology:
Our CNN model consisted of five layers to effectively extracting relevant features from input images. The first layer comprised 16 filters with a kernel size of 3*3. This choice of architecture allowed the model to extract relevant features from the input images effectively. We applied max pooling and flattening techniques to downsample the extracted features, reshape and reduce the computational complexity.   Finally, the flattened features were passed through a dense layer, enablinto enable the model to learn and predict the probabilities associated with the three possible outcomeswe Scissors Rock and Paper.  <br>

Notebooks:<br>
We generated two notebooks.  <br>
1- reduced_accuracy_for_streamlit Notebook: Within this notebook, we trained a model from scratch considering the ideas came from the reference that could be found at the starting part of the notebook. We reduced the depth of the model, or in other words layers to reduce the number of parameters and as a resualt, reducing the size of the saved model. The reason was that we couldn't commit saved model file over 25Mb to Github. We needed this trained file to use in our streamlit app.<br>  
So, this model will not be accurate enough, but at the moment for miniproject we are satisfied with it for deployment it in streamlit app.<br>
  <br>
2- cnn_rock_paper_scissors Notebook: We generated this notebook to solve the overfitting problem and increasing the accuracy. This is the notebook that we implemented some part of our reference code at and we solved the overfitting, and low accuracy problem.  <br>
Also, at the end of this note book we used functional plot.<br>
   <br> 

### Group Members:
1- Dusan Birtasevic <br>
2- Narjes Amousoltani <br>
3- Tina Khazaei <br>
4- Kavian Mashayekhi
