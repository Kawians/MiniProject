import streamlit as st
import tensorflow as tf
import tensorflow_datasets as tfds
import numpy as np
import cv2
import time
import random

def main():
    # Set Streamlit app title and description
    st.title("Rock Paper Scissors Game")
    st.write("Click the 'Start Game' button and make a hand gesture within 3 seconds to play Rock, Paper, Scissors against the computer.")

    # Load the pre-trained model
    model = tf.keras.models.load_model("rock_paper_scissors_model.h5")

    # Define class labels
    class_names = ["Rock", "Paper", "Scissors"]

    # Add a button to start the game
    start_game = st.button("Start Game")

    if start_game:
        st.write("Game started!")
        time.sleep(1)
        st.write("3")
        time.sleep(1)
        st.write("2")
        time.sleep(1)
        st.write("1")
        time.sleep(1)
        st.write("Capture!")

        # Initialize the webcam capture
        video_capture = cv2.VideoCapture(0)

        # Capture an image from the webcam
        ret, frame = video_capture.read()
        cv2.imshow("Captured Image", frame)

        # Preprocess the captured frame
        resized_frame = cv2.resize(frame, (300, 300))
        img_array = np.array(resized_frame) / 255.0
        img_array = np.expand_dims(img_array, axis=0)

        # Generate a random computer move (rock, paper, or scissors)
        computer_move = random.choice(["Rock", "Paper", "Scissors"])

        # Make a prediction for the user move
        user_prediction = model.predict(img_array)
        user_move_index = np.argmax(user_prediction)
        user_move = class_names[user_move_index]

        # Determine the game result
        if user_move == computer_move:
            result = "It's a tie!"
        elif (user_move == "Rock" and computer_move == "Scissors") or (user_move == "Paper" and computer_move == "Rock") or (user_move == "Scissors" and computer_move == "Paper"):
            result = "You win!"
        else:
            result = "You lose!"

        # Display the moves and result
        st.write(f"Your Move: {user_move}")
        st.write(f"Computer's Move: {computer_move}")
        st.write(result)

        # Release the webcam and close OpenCV windows
        video_capture.release()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
