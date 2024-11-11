import cvzone
import cv2
import numpy as np
from cvzone.HandTrackingModule import HandDetector
import google.generativeai as genai
import os
from dotenv import load_dotenv
from PIL import Image 
import streamlit as st

# Streamlit app settings
st.set_page_config(page_title="Xolve", page_icon="🧮", layout="wide")
st.image("xolve.png")
st.markdown(
    """
    <style>
        .title  {
            font-size: 100px;  /* Change the font size here */
            font-weight: bold;
            font-family: 'Ubuntu', sans-serif;
            color: #ffffff;   /* Change the font color here */
            text-align: center;
            margin-top: 0;
        }
        .title p {
            font-size: 20px;  /* Change the font size here */
            font-weight: bold;
            font-family: 'Ubuntu', sans-serif;
            color: #ffffff;   /* Change the font color here */
            text-align: center;
        }
        .answer-title {
            font-size: 50px;  /* Change the font size here */
            font-weight: bold;
            font-family: 'ubuntu', sans-serif;
            color: #ffffff;   /* Change the font color here */
            font-weight: 500;
            text-align: center;
        }
        subheader {
            font-size: 30px;  /* Change the font size here */
            font-weight: bold;
            font-family: 'Ubuntu', sans-serif;
            color: #ffffff;   /* Change the font color here */
            text-align: center;
            border-radius: 15px;
            background-color: #1E90FF;
        }
        img{
            border-radius: 15px;
        
        }

    </style>
    """, unsafe_allow_html=True
)
col1, col2 = st.columns([1, 1])
with col1:
    run = st.checkbox("Run", value=True)
    FRAME_WINDOW = st.image([])

with col2:
    st.markdown(' <div class="answer-title"> Answer </div>', unsafe_allow_html=True)
    output_text_area = st.subheader("")

# Load environment variables from .env file
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

# Initialize the webcam and hand detector
cap = cv2.VideoCapture(0)
cap.set(3, 1280)  # Frame width
cap.set(4, 720)   # Frame height
detector = HandDetector(staticMode=False, maxHands=1, modelComplexity=1, detectionCon=0.7, minTrackCon=0.5)

# Initialize variables
prev_Pos = None
canvas = None
response_Answer = ""

def getHandInfo(img):
    hands, img = detector.findHands(img, draw=False, flipType=True)
    if hands:
        hand = hands[0]
        lmList = hand["lmList"]
        fingers = detector.fingersUp(hand)
        return fingers, lmList
    return None

def draw(img, handInfo, prev_Pos, canvas):
    fingers, lmList = handInfo
    current_Pos = None
    if fingers == [0, 1, 0, 0, 0]:
        current_Pos = lmList[8][0:2]
        if prev_Pos is None:
            prev_Pos = current_Pos
        cv2.line(canvas, current_Pos, prev_Pos, (94, 23, 235), 5)
    elif fingers == [1, 0, 1, 1, 1]:
        canvas.fill(0)  # Clear canvas
        prev_Pos = None
    return current_Pos

def sendToGemini(model, canvas, fingers):
    if fingers == [1, 1, 1, 1, 0]:
        pil_img = Image.fromarray(canvas)
        response = model.generate_content(["Please solve the following math problem step-by-step: \
1. Start by giving the short answer (just the result). \
2. Add a line break here and provide a brief explanation of the solution.\
3. Next, restate the question for clarity. \
4. Then, provide a detailed, step-by-step explanation of how to solve the problem, including any formulas or concepts used. Use 'Step 1:', 'Step 2:', etc., for each step. \
5. Make sure to include adequate spacing and line breaks for clarity between each section.", pil_img])        
        return response.text
    
# Streamlit loop
while run:
    success, img = cap.read()
    if not success:
        st.warning("Failed to capture video.")
        break

    img = cv2.flip(img, 1)
    if canvas is None:
        canvas = np.zeros_like(img)

    handInfo = getHandInfo(img)
    if handInfo:
        fingers, lmList = handInfo
        prev_Pos = draw(img, handInfo, prev_Pos, canvas)
        response_Answer=sendToGemini(model, canvas, fingers)

    # Merge the drawing canvas with the captured frame
    image_combination = cv2.addWeighted(img, 0.5, canvas, 1, 0)
    FRAME_WINDOW.image(image_combination, channels="BGR")
    if response_Answer:
        output_text_area.subheader(response_Answer)
    

# Release camera when done
st.write("Hello")
cap.release()
