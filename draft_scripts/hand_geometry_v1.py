import cv2
import mediapipe as mp
import statistics
import numpy as np
from pymongo import MongoClient
from pprint import pprint

trains = []
hand_metric = None
error = 0.0001
spatial_eror = 0.1

def doConnection():
  myclient = MongoClient("mongodb://localhost:27017/")
  mydb = myclient["biometry"]
  mycol = mydb["user_Data"]
  mydoc = mycol.find({"user": "BlueDragon"},{"_id":0,"hand_metric":1})
  global hand_metric
  hand_metric = mydoc[0]["hand_metric"]

def calculateDistances(results):

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
  #print(metric)
  #print(results.landmark[mp_hands.HandLandmark.WRIST].z)
  z = results.landmark[mp_hands.HandLandmark.WRIST].z
  print(metric,z)

  if  0.000000006<z<0.000000007:
    print("Entered correct zone")
    if metric-error<hand_metric<metric+error:
      print("Authenticated")
      exit(0)
'''
  if len(trains) <= 500:
    trains.append(metric)
  else:
    print(statistics.mean(trains))
    exit()  
'''

doConnection()
#Initialize Models
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

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
      calculateDistances(results.multi_hand_landmarks[0])
      for hand_landmarks in results.multi_hand_landmarks:
        mp_drawing.draw_landmarks(
            image,
            hand_landmarks,
            mp_hands.HAND_CONNECTIONS,
            mp_drawing_styles.get_default_hand_landmarks_style(),
            mp_drawing_styles.get_default_hand_connections_style())
    # Flip the image horizontally for a selfie-view display.
    cv2.imshow('MediaPipe Hands', cv2.flip(image, 1))
    if cv2.waitKey(5) & 0xFF == 27:
      break
cap.release()