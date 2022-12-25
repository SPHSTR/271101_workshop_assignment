# This code demonstrate how to show location of hand landmark
import cv2
import mediapipe as mp


cap = cv2.VideoCapture(0)

# Call hand pipe line module
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    # print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                if id == 5:
                    cx5 = cx
                    cy5 = cy
                if id == 17:
                    cx17 = cx
                    cy17 = cy
                if id == 9:
                    cy9 = cy
                    cx9 = cx
                if id == 0:
                    cy0 = cy
                    cx0 = cx
                if id == 4:
                    cx4 = cx
                    cy4 = cy
                if id == 3:
                    cx3 = cx
                    cy3 = cy
                if id == 8:
                    cx8 = cx
                    cy8 = cy
                if id == 7:
                    cx7 = cx
                    cy7 = cy
                if id == 12:
                    cx12 = cx
                    cy12 = cy
                if id == 11:
                    cx11 = cx
                    cy11 = cy
                if id == 16:
                    cx16 = cx
                    cy16 = cy
                if id == 15:
                    cx15 = cx
                    cy15 = cy
                if id == 20:
                    cx20 = cx
                    cy20 = cy
                if id == 19:
                    cx19 = cx
                    cy19 = cy
                if id == 5:
                    cx5 = cx
                    cy5 = cy
                if id == 2:
                    cx2 = cx
                    cy2 = cy
            if cy0 > cy9 and cy17 < cy0:
                cv2.putText(img, "Up", (80, 40),
                            cv2.FONT_HERSHEY_PLAIN, 1.5, (138, 138, 253), 3)
                if cx17 > cx5:
                    cv2.putText(img, "Left", (10, 40),
                                cv2.FONT_HERSHEY_PLAIN, 1.5, (102, 209, 255), 3)
                    if cx4 < cx3:
                        cv2.putText(
                            img, "Thumb", (10, 70), cv2.FONT_HERSHEY_PLAIN, 1.5, (219, 180, 205), 3)
                    if cy8 < cy7:
                        cv2.putText(img, "Index", (110, 70),
                                    cv2.FONT_HERSHEY_PLAIN, 1.5, (221, 200, 255), 3)
                    if cy12 < cy11:
                        cv2.putText(img, "Middle", (190, 70),
                                    cv2.FONT_HERSHEY_PLAIN, 1.5, (204, 175, 255), 3)
                    if cy16 < cy15:
                        cv2.putText(
                            img, "Ring", (280, 70), cv2.FONT_HERSHEY_PLAIN, 1.5, (254, 224, 189), 3)
                    if cy20 < cy19:
                        cv2.putText(img, "Pinky", (350, 70),
                                    cv2.FONT_HERSHEY_PLAIN, 1.5, (255, 210, 162), 3)
                if cx5 > cx17:
                    cv2.putText(img, "Right", (10, 40),
                                cv2.FONT_HERSHEY_PLAIN, 1.5, (178, 138, 17), 3)
                    if cx4 > cx3:
                        cv2.putText(
                            img, "Thumb", (10, 70), cv2.FONT_HERSHEY_PLAIN, 1.5, (219, 180, 205), 3)
                    if cy8 < cy7:
                        cv2.putText(img, "Index", (110, 70),
                                    cv2.FONT_HERSHEY_PLAIN, 1.5, (221, 200, 255), 3)
                    if cy12 < cy11:
                        cv2.putText(img, "Middle", (190, 70),
                                    cv2.FONT_HERSHEY_PLAIN, 1.5, (204, 175, 255), 3)
                    if cy16 < cy15:
                        cv2.putText(
                            img, "Ring", (280, 70), cv2.FONT_HERSHEY_PLAIN, 1.5, (254, 224, 189), 3)
                    if cy20 < cy19:
                        cv2.putText(img, "Pinky", (350, 70),
                                    cv2.FONT_HERSHEY_PLAIN, 1.5, (255, 210, 162), 3)
            if cy9 > cy0 and cy17 > cy0:
                cv2.putText(img, "Down", (80, 40),
                            cv2.FONT_HERSHEY_PLAIN, 1.5, (160, 214, 6), 3)
                if cx5 < cx17:
                    cv2.putText(img, "Right", (10, 40),
                                cv2.FONT_HERSHEY_PLAIN, 1.5, (178, 138, 17), 3)
                    if cx4 < cx3:
                        cv2.putText(
                            img, "Thumb", (10, 70), cv2.FONT_HERSHEY_PLAIN, 1.5, (219, 180, 205), 3)
                    if cy8 > cy7:
                        cv2.putText(img, "Index", (110, 70),
                                    cv2.FONT_HERSHEY_PLAIN, 1.5, (221, 200, 255), 3)
                    if cy12 > cy11:
                        cv2.putText(img, "Middle", (190, 70),
                                    cv2.FONT_HERSHEY_PLAIN, 1.5, (204, 175, 255), 3)
                    if cy16 > cy15:
                        cv2.putText(
                            img, "Ring", (280, 70), cv2.FONT_HERSHEY_PLAIN, 1.5, (254, 224, 189), 3)
                    if cy20 > cy19:
                        cv2.putText(img, "Pinky", (350, 70),
                                    cv2.FONT_HERSHEY_PLAIN, 1.5, (255, 210, 162), 3)
                if cx5 > cx17:
                    cv2.putText(img, "Left", (10, 40),
                                cv2.FONT_HERSHEY_PLAIN, 1.5, (102, 209, 255), 3)
                    if cx4 > cx3:
                        cv2.putText(
                            img, "Thumb", (10, 70), cv2.FONT_HERSHEY_PLAIN, 1.5, (219, 180, 205), 3)
                    if cy8 > cy7:
                        cv2.putText(img, "Index", (110, 70),
                                    cv2.FONT_HERSHEY_PLAIN, 1.5, (221, 200, 255), 3)
                    if cy12 > cy11:
                        cv2.putText(img, "Middle", (190, 70),
                                    cv2.FONT_HERSHEY_PLAIN, 1.5, (204, 175, 255), 3)
                    if cy16 > cy15:
                        cv2.putText(
                            img, "Ring", (280, 70), cv2.FONT_HERSHEY_PLAIN, 1.5, (254, 224, 189), 3)
                    if cy20 > cy19:
                        cv2.putText(img, "Pinky", (350, 70),
                                    cv2.FONT_HERSHEY_PLAIN, 1.5, (255, 210, 162), 3)
            if cx9 > cx0 and cy17 > cy0 and cy5 < cy0:
                cv2.putText(img, "Left", (80, 40),
                            cv2.FONT_HERSHEY_PLAIN, 1.5, (169, 90, 255), 3)
                cv2.putText(img, "Left", (10, 40),
                            cv2.FONT_HERSHEY_PLAIN, 1.5, (102, 209, 255), 3)
                if cy4 < cy3:
                    cv2.putText(img, "Thumb", (10, 70),
                                cv2.FONT_HERSHEY_PLAIN, 1.5, (219, 180, 205), 3)
                if cx8 > cx7:
                    cv2.putText(img, "Index", (110, 70),
                                cv2.FONT_HERSHEY_PLAIN, 1.5, (221, 200, 255), 3)
                if cx12 > cx11:
                    cv2.putText(img, "Middle", (190, 70),
                                cv2.FONT_HERSHEY_PLAIN, 1.5, (204, 175, 255), 3)
                if cx16 > cx15:
                    cv2.putText(img, "Ring", (280, 70),
                                cv2.FONT_HERSHEY_PLAIN, 1.5, (254, 224, 189), 3)
                if cx20 > cx19:
                    cv2.putText(img, "Pinky", (350, 70),
                                cv2.FONT_HERSHEY_PLAIN, 1.5, (255, 210, 162), 3)
            if cx9 > cx0 and cy17 < cy0 and cx2 < cx17:
                cv2.putText(img, "Left", (80, 40),
                            cv2.FONT_HERSHEY_PLAIN, 1.5, (169, 90, 255), 3)
                cv2.putText(img, "Right", (10, 40),
                            cv2.FONT_HERSHEY_PLAIN, 1.5, (178, 138, 17), 3)
                if cy4 > cy3:
                    cv2.putText(img, "Thumb", (10, 70),
                                cv2.FONT_HERSHEY_PLAIN, 1.5, (219, 180, 205), 3)
                if cx8 > cx7:
                    cv2.putText(img, "Index", (110, 70),
                                cv2.FONT_HERSHEY_PLAIN, 1.5, (221, 200, 255), 3)
                if cx12 > cx11:
                    cv2.putText(img, "Middle", (190, 70),
                                cv2.FONT_HERSHEY_PLAIN, 1.5, (204, 175, 255), 3)
                if cx16 > cx15:
                    cv2.putText(img, "Ring", (280, 70),
                                cv2.FONT_HERSHEY_PLAIN, 1.5, (254, 224, 189), 3)
                if cx20 > cx19:
                    cv2.putText(img, "Pinky", (350, 70),
                                cv2.FONT_HERSHEY_PLAIN, 1.5, (255, 210, 162), 3)
            if cx9 < cx0 and cy17 < cy0 and cy5 > cy0:
                cv2.putText(img, "Right", (80, 40),
                            cv2.FONT_HERSHEY_PLAIN, 1.5, (51, 255, 204), 3)
                cv2.putText(img, "Left", (10, 40),
                            cv2.FONT_HERSHEY_PLAIN, 1.5, (102, 209, 255), 3)
                if cy4 > cy3:
                    cv2.putText(img, "Thumb", (10, 70),
                                cv2.FONT_HERSHEY_PLAIN, 1.5, (219, 180, 205), 3)
                if cx8 < cx7:
                    cv2.putText(img, "Index", (110, 70),
                                cv2.FONT_HERSHEY_PLAIN, 1.5, (221, 200, 255), 3)
                if cx12 < cx11:
                    cv2.putText(img, "Middle", (190, 70),
                                cv2.FONT_HERSHEY_PLAIN, 1.5, (204, 175, 255), 3)
                if cx16 < cx15:
                    cv2.putText(img, "Ring", (280, 70),
                                cv2.FONT_HERSHEY_PLAIN, 1.5, (254, 224, 189), 3)
                if cx20 < cx19:
                    cv2.putText(img, "Pinky", (350, 70),
                                cv2.FONT_HERSHEY_PLAIN, 1.5, (255, 210, 162), 3)
            if cx9 < cx0 and cy17 > cy0 and cx2 > cx17:
                cv2.putText(img, "Right", (80, 40),
                            cv2.FONT_HERSHEY_PLAIN, 1.5, (51, 255, 204), 3)
                cv2.putText(img, "Right", (10, 40),
                            cv2.FONT_HERSHEY_PLAIN, 1.5, (178, 138, 17), 3)
                if cy4 < cy3:
                    cv2.putText(img, "Thumb", (10, 70),
                                cv2.FONT_HERSHEY_PLAIN, 1.5, (219, 180, 205), 3)
                if cx8 < cx7:
                    cv2.putText(img, "Index", (110, 70),
                                cv2.FONT_HERSHEY_PLAIN, 1.5, (221, 200, 255), 3)
                if cx12 < cx11:
                    cv2.putText(img, "Middle", (190, 70),
                                cv2.FONT_HERSHEY_PLAIN, 1.5, (204, 175, 255), 3)
                if cx16 < cx15:
                    cv2.putText(img, "Ring", (280, 70),
                                cv2.FONT_HERSHEY_PLAIN, 1.5, (254, 224, 189), 3)
                if cx20 < cx19:
                    cv2.putText(img, "Pinky", (350, 70),
                                cv2.FONT_HERSHEY_PLAIN, 1.5, (255, 210, 162), 3)

            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    cv2.imshow("aow wai bok wa shu new arai yoo", img)
    cv2.waitKey(1)
# Closeing all open windows
# cv2.destroyAllWindows()