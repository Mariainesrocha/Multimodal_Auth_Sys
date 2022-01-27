from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
import statistics, cv2
from PyQt5.QtGui import QImage, QPixmap
import mediapipe as mp
from pymongo import MongoClient
from voice_register import Ui_voice_register_window
from error_window import Ui_error_window
from voice_login import Ui_voice_login_window

current_user = None
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands
trains = []
recording = True

def showErrorMessage(wd, msg): #error in hand login/register
    wd.window = QtWidgets.QDialog()
    wd.ui = Ui_error_window()
    wd.ui.setupUi(wd.window)
    wd.window.show()
    wd.ui.error_msg.setText(msg)

def openVoiceWindow(wd, register=False): #after hand regsiter/login
    wd.window = QtWidgets.QMainWindow()
    if register:
        wd.ui = Ui_voice_register_window()
    else:
        wd.ui = Ui_voice_login_window()
    wd.ui.setupUi(wd.window)
    wd.ui.set_user(current_user)
    wd.window.show()    

def compare(metric,z, hand_metric):
    error = 0.004
    print(metric)
    print(hand_metric)

    if metric-error<hand_metric<metric+error:
        return True

def calculateDistances(wd,results,register):
        #Get x,y for each point in the hand
        thumb_tip = np.array((
        results.landmark[mp_hands.HandLandmark.THUMB_TIP].x,
        results.landmark[mp_hands.HandLandmark.THUMB_TIP].y
        ))
        thumb_mcp = np.array((
        results.landmark[mp_hands.HandLandmark.THUMB_MCP].x,
        results.landmark[mp_hands.HandLandmark.THUMB_MCP].y
        ))
        index_finger_tip = np.array((
        results.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x,
        results.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y
        ))
        index_finger_mcp = np.array((
        results.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP].x,
        results.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP].y
        ))
        middle_finger_tip = np.array((
        results.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].x,
        results.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y
        ))
        middle_finger_mcp = np.array((
        results.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP].x,
        results.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP].y
        ))
        ring_finger_tip = np.array((
        results.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].x,
        results.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].y
        ))
        ring_finger_mcp = np.array((
        results.landmark[mp_hands.HandLandmark.RING_FINGER_MCP].x,
        results.landmark[mp_hands.HandLandmark.RING_FINGER_MCP].y
        ))
        pinky_tip = np.array((
        results.landmark[mp_hands.HandLandmark.PINKY_TIP].x,
        results.landmark[mp_hands.HandLandmark.PINKY_TIP].y
        ))
        pinky_mcp = np.array((
        results.landmark[mp_hands.HandLandmark.PINKY_MCP].x,
        results.landmark[mp_hands.HandLandmark.PINKY_MCP].y
        ))
        wrist = np.array((
        results.landmark[mp_hands.HandLandmark.WRIST].x,
        results.landmark[mp_hands.HandLandmark.WRIST].y
        ))

        #Calculate the distances between the fingertips and the mcp
        dist1 = np.linalg.norm(thumb_tip - thumb_mcp)
        dist2 = np.linalg.norm(index_finger_tip - index_finger_mcp)
        dist3 = np.linalg.norm(middle_finger_tip - middle_finger_mcp)
        dist4 = np.linalg.norm(ring_finger_tip - ring_finger_mcp)
        dist5 = np.linalg.norm(pinky_tip - pinky_mcp)

        #Calculate the distances between the knuckles
        dist6 = np.linalg.norm(thumb_mcp - index_finger_mcp)
        dist7 = np.linalg.norm(index_finger_mcp - middle_finger_mcp)
        dist8 = np.linalg.norm(middle_finger_mcp - ring_finger_mcp)
        dist9 = np.linalg.norm(ring_finger_mcp - pinky_mcp)

        #Calculate across the palm distance and wrist main points
        dist10 = np.linalg.norm(thumb_mcp - wrist)
        dist11 = np.linalg.norm(middle_finger_mcp - wrist)
        dist12 = np.linalg.norm(pinky_mcp - wrist)
        dist13 = np.linalg.norm(pinky_mcp - thumb_mcp)

        metric = dist11/(dist1+dist2+dist3+dist4+dist5+dist6+dist7+dist8+dist9+dist10+dist12+dist13)

        if len(trains) <= 1000:
            trains.append(metric)
        else:
            myclient = MongoClient("mongodb://localhost:27017/")
            mydb = myclient["biometry"]
            mycol = mydb["user_Data"]
            global recording
            recording = False
            if register:
                mycol.update_one({"user": current_user}, {"$set": {"hand_metric": statistics.mean(trains)}}) 
                openVoiceWindow(wd,True)
            else:
                mydoc = mycol.find({"user": current_user},{"_id":0,"hand_metric":1})
                hand_metric = mydoc[0]["hand_metric"]

                if compare(metric, results.landmark[mp_hands.HandLandmark.WRIST].z, hand_metric):
                    openVoiceWindow(wd)
                else:
                    #openVoiceWindow(wd)
                    showErrorMessage(wd, "Invalid hand metrics!")

def video(wd,username, register=False):
    global current_user
    current_user = username

    #Video Capture
    cap = cv2.VideoCapture(0)
    with mp_hands.Hands(
            model_complexity=0,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5) as hands:
        while cap.isOpened():
            success, image = cap.read()
            if not success:
                print("Ignoring empty camera frame.")
                continue

            image.flags.writeable = False
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            results = hands.process(image)

            # Draw the hand annotations on the image.
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            if results.multi_hand_landmarks:
                calculateDistances(wd,results.multi_hand_landmarks[0],register)
                for hand_landmarks in results.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(
                        image,
                        hand_landmarks,
                        mp_hands.HAND_CONNECTIONS,
                        mp_drawing_styles.get_default_hand_landmarks_style(),
                        mp_drawing_styles.get_default_hand_connections_style())
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            height, width, channel = image.shape
            step = channel * width
            qImg = QImage(image.data, width, height, step, QImage.Format.Format_RGB888)
            wd.image.setPixmap(QPixmap.fromImage(qImg))
            if not recording:
                break
            else:
                cv2.waitKey()
                
    cap.release()