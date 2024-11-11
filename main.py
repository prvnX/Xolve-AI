import cvzone
import cv2
import numpy as np
from cvzone.HandTrackingModule import HandDetector
import google.generativeai as genai
import os
from dotenv import load_dotenv
from PIL import Image 
import streamlit as streamlit

streamlit.set_page_config(page_title="Xolve", page_icon="🧮", layout="wide", initial_sidebar_state="collapsed")
streamlit.title("Xolve - Your AI math companion")
streamlit.image("xolve.png")

# Load environment variables from .env file
load_dotenv()

# Access the GEMINI_API_KEY from environment variables
genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

# Initialize the webcam to capture video
# The '2' indicates the third camera connected to your computer; '0' would usually refer to the built-in camera
cap = cv2.VideoCapture(0)
cap.set(3, 1280)  # Set the width of the frame
cap.set(4, 720)  # Set the height of the frame
# Initialize the HandDetector class with the given parameters
detector = HandDetector(staticMode=False, maxHands=1, modelComplexity=1, detectionCon=0.7 , minTrackCon=0.5)

def getHandInfo(img):
    # Find hands in the current frame
    # The 'draw' parameter draws landmarks and hand outlines on the image if set to True
    # The 'flipType' parameter flips the image, making it easier for some detections
    hands, img = detector.findHands(img, draw=False, flipType=True)

    # Check if any hands are detected
    if hands:
        # Information for the first hand detected
        hand = hands[0]  # Get the first hand detected
        lmList = hand["lmList"]  # List of 21 landmarks for the first hand
        # Count the number of fingers up for the first hand
        fingers = detector.fingersUp(hand)
        return fingers, lmList
    else:
        return None

def draw(img,handInfo,prev_Pos,canvas):
    fingers, lmList = handInfo
    current_Pos = None
    if fingers == [0, 1, 0, 0, 0]:
        current_Pos= lmList[8][0:2]
        if prev_Pos is None:
            prev_Pos = current_Pos
        cv2.line(canvas,current_Pos,prev_Pos,(94, 23, 235),5)
    elif fingers == [1,0,1,1,1]:
        canvas.fill(0)  # Set all pixels to black for a clear canvas
        prev_Pos = None  # Reset previous position as well

    return current_Pos
 
def sendToGemini(model,canvas,fingers):
    if fingers == [1,1,1,1,0]:
        pil_img = Image.fromarray(canvas)
        response = model.generate_content(["Please provide the solution to the math problem. First Start by stating the question, just give the answer and then add a explanation.",pil_img])        
        print(response.text)
        

    
    

prev_Pos = None
canvas = None
image_combination = None
# Continuously get frames from the webcam
while True:
    # Capture each frame from the webcam
    # 'success' will be True if the frame is successfully captured, 'img' will contain the frame
    success, img = cap.read()
    img = cv2.flip(img, 1)

    if canvas is None:
        canvas= np.zeros_like(img)
         

    # Get information about the hand in the current frame
    handInfo = getHandInfo(img) 
    if handInfo:
        fingers, lmList = handInfo
        prev_Pos=draw(img,handInfo,prev_Pos,canvas)
        sendToGemini(model,canvas,fingers) 

    image_combination=cv2.addWeighted(img,0.5,canvas,1,0)
    

    # Display the image in a window
    cv2.imshow("Image-Combination", image_combination)
    cv2.imshow("Canvas", canvas)

    # Keep the window open and update it for each frame; wait for 1 millisecond between frames
    cv2.waitKey(1)