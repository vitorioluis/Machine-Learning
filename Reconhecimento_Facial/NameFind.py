# -*- coding:utf-8 -*-
#     ----------- FUNCTION TO READ THE FILE AND ADD THE NAMES AND IDs IN TO TUPLES


import math
import os
import time

import cv2

from constantes import EYE_CASCADE, FACE_CASCADE, WHITE, CODING

now_time = time.clock()
base_nomes = 'dados/Names.txt'


def FileRead():
    if os.path.exists(base_nomes) is False:
        with open(base_nomes, 'w', encoding=CODING) as ope:
            ope.write('1 , Desconhecido\n')

    Info = open(base_nomes, "r", encoding=CODING)  # Open th text file in readmode
    NAME = []  # The tuple to store Names
    while (True):  # Read all the lines in the file and store them in two tuples
        Line = Info.readline()
        if Line == '':
            break
        NAME.append(Line.split(",")[1].rstrip())

    return NAME  # Return the two tuples


Names = FileRead()  # Run the above Function to get the ID and Names Tuple


#     ------------------- FUNCTION TO FIND THE NAME  -----------------------------------------------------------

# Verification of the last ID in Names.txt (last_string) - CREATED BY IGOR
def file_is_empty(path):
    return os.stat(path).st_size == 0


with open(base_nomes, encoding=CODING) as f:
    lines = f.readlines()
    if file_is_empty(base_nomes):
        last_string = 1
    else:
        last_row = lines[-1]
        string_last = last_row
        for s in string_last.split():
            if s.isdigit():
                last_string = int(s)
                print("A base possui: " + str(last_string) + " " + "pessoas")


def ID2Name(ID, conf):
    if 1 <= ID <= last_string:
        NameString = "Name: " + Names[ID - 1] + " Confidence: " + (
            str(round(conf)))  # Find the Name using the index of the ID
    else:
        NameString = " Face Not Recognised "  # Find the Name using the index of the ID

    return NameString


#     ------------------- THIS FUNCTION READ THE FILE AND ADD THE NAME TO THE END OF THE FILE  -----------------


def AddName():
    x = 'r+' if os.path.exists(base_nomes) else 'r'

    Name = input('Enter Your Name ')
    with open(base_nomes, x, encoding=CODING) as Info:
        ID = ((sum(1 for line in Info)) + 1)
        Info.write(str(ID) + " " + "," + " " + Name + "\n")
        print("Name Stored in " + str(ID))
    return ID


#     ------------------- DRAW THE BOX AROUND THE FACE, ID and CONFIDENCE  -------------------------------------


def DispID(x, y, w, h, NAME, Image):
    #  --------------------------------- THE POSITION OF THE ID BOX  ---------------------------------------------

    Name_y_pos = y - 10
    Name_X_pos = x + w / 2 - (len(NAME) * 7 / 2)

    if Name_X_pos < 0:
        Name_X_pos = 0
    elif (Name_X_pos + 10 + (len(NAME) * 7) > Image.shape[1]):
        Name_X_pos = Name_X_pos - (Name_X_pos + 10 + (len(NAME) * 7) - (Image.shape[1]))
    if Name_y_pos < 0:
        Name_y_pos = y + h + 10

    #  ------------------------------------    THE DRAWING OF THE BOX AND ID   --------------------------------------

    draw_box(Image, x, y, w, h)

    # cv2.rectangle(Image, (int(Name_X_pos-10), int(Name_y_pos-25)),(int(Name_X_pos +10 + (len(NAME) * 7)), int(Name_y_pos-1)), (0,0,0), -2)
    cv2.rectangle(Image, (int(Name_X_pos - 10), int(Name_y_pos - 25)),
                  (int(Name_X_pos + 10 + (len(NAME) * 7)), int(Name_y_pos - 1)), (0, 0, 0), -2)
    cv2.rectangle(Image, (int(Name_X_pos - 10), int(Name_y_pos - 25)),
                  (int(Name_X_pos + 10 + (len(NAME) * 7)), int(Name_y_pos - 1)), WHITE,
                  1)  # Draw a Black Rectangle over the face frame
    cv2.putText(Image, NAME, (int(Name_X_pos), int(Name_y_pos - 10)), cv2.FONT_HERSHEY_DUPLEX, .4,
                WHITE)  # Print the name of the ID


def draw_box(Image, x, y, w, h):
    cv2.line(Image, (x, y), (x + (int(w / 5)), y), WHITE, 2)
    cv2.line(Image, (x + (int(w / 5) * 4), y), (x + w, y), WHITE, 2)
    cv2.line(Image, (x, y), (x, y + (int(h / 5))), WHITE, 2)
    cv2.line(Image, (x + w, y), (x + w, y + int((h / 5))), WHITE, 2)
    cv2.line(Image, (x, (y + int((h / 5 * 4)))), (x, y + h), WHITE, 2)
    cv2.line(Image, (x, (y + h)), (x + int((w / 5)), y + h), WHITE, 2)
    cv2.line(Image, (x + (int((w / 5) * 4)), y + h), (x + w, y + h), WHITE, 2)
    cv2.line(Image, (x + w, (y + int((h / 5 * 4)))), (x + w, y + h), WHITE, 2)


# ---------------     SECOND ID BOX      ----------------------
def DispID2(x, y, w, h, NAME, Image):
    #  --------------------------------- THE POSITION OF THE ID BOX  -------------------------------------------------

    Name_y_pos = y - 40
    Name_X_pos = x + w / 2 - (len(NAME) * 7 / 2)

    if Name_X_pos < 0:
        Name_X_pos = 0
    elif (Name_X_pos + 10 + (len(NAME) * 7) > Image.shape[1]):
        Name_X_pos = Name_X_pos - (Name_X_pos + 10 + (len(NAME) * 7) - (Image.shape[1]))
    if Name_y_pos < 0:
        Name_y_pos = y + h + 10

    #  ------------------------------------    THE DRAWING OF THE BOX AND ID   --------------------------------------
    cv2.rectangle(Image, (int(Name_X_pos - 10), int(Name_y_pos - 25)),
                  (int(Name_X_pos + 10 + (len(NAME) * 7)), int(Name_y_pos - 1)), (0, 0, 0), -2)
    cv2.rectangle(Image, (int(Name_X_pos - 10), int(Name_y_pos - 25)),
                  (int(Name_X_pos + 10 + (len(NAME) * 7)), int(Name_y_pos - 1)), WHITE,
                  1)  # Draw a Black Rectangle over the face frame
    cv2.putText(Image, NAME, (int(Name_X_pos), int(Name_y_pos - 10)), cv2.FONT_HERSHEY_DUPLEX, .4,
                WHITE)  # Print the name of the ID


# ---------------     THIRD ID BOX      ----------------------
def DispID3(x, y, w, h, NAME, Image):
    #  --------------------------------- THE POSITION OF THE ID BOX  -------------------------------------------------

    Name_y_pos = y - 70
    Name_X_pos = x + w / 2 - (len(NAME) * 7 / 2)

    if Name_X_pos < 0:
        Name_X_pos = 0
    elif (Name_X_pos + 10 + (len(NAME) * 7) > Image.shape[1]):
        Name_X_pos = Name_X_pos - (Name_X_pos + 10 + (len(NAME) * 7) - (Image.shape[1]))
    if Name_y_pos < 0:
        Name_y_pos = y + h + 10

    #  ------------------------------------    THE DRAWING OF THE BOX AND ID   --------------------------------------
    cv2.rectangle(Image, (int(Name_X_pos - 10), int(Name_y_pos - 25)),
                  (int(Name_X_pos + 10 + (len(NAME) * 7)), int(Name_y_pos - 1)), (0, 0, 0), -2)
    cv2.rectangle(Image, (int(Name_X_pos - 10), int(Name_y_pos - 25)),
                  (int(Name_X_pos + 10 + (len(NAME) * 7)), int(Name_y_pos - 1)), WHITE,
                  1)  # Draw a Black Rectangle over the face frame
    cv2.putText(Image, NAME, (int(Name_X_pos), int(Name_y_pos - 10)), cv2.FONT_HERSHEY_DUPLEX, .4,
                WHITE)  # Print the name of the ID


def DrawBox(Image, x, y, w, h):
    cv2.rectangle(Image, (x, y), (x + w, y + h), (255, 255, 255), 1)  # Draw a rectangle arround the face


# ----------------------------- THIS FUNCTION TAKES IN SPEC CASCADE, FACE CASCADE AND AN IMAGE
# ------------------------- IT RETURNS A CROPPED FACE AND IF POSSIBLE STRAIGHTENS THE TILT OF THE HEAD


def DetectEyes(Image):
    Theta = 0
    rows, cols = Image.shape
    glass = EYE_CASCADE.detectMultiScale(Image)  # This ditects the eyes
    for (sx, sy, sw, sh) in glass:
        if glass.shape[0] == 2:  # The Image should have 2 eyes
            if glass[1][0] > glass[0][0]:
                DY = ((glass[1][1] + glass[1][3] / 2) - (
                        glass[0][1] + glass[0][3] / 2))  # Height diffrence between the glass
                DX = ((glass[1][0] + glass[1][2] / 2) - glass[0][0] + (
                        glass[0][2] / 2))  # Width diffrance between the glass
            else:
                DY = (-(glass[1][1] + glass[1][3] / 2) + (
                        glass[0][1] + glass[0][3] / 2))  # Height diffrence between the glass
                DX = (-(glass[1][0] + glass[1][2] / 2) + glass[0][0] + (
                        glass[0][2] / 2))  # Width diffrance between the glass

            if (DX != 0.0) and (DY != 0.0):  # Make sure the the change happens only if there is an angle
                Theta = math.degrees(math.atan(round(float(DY) / float(DX), 2)))  # Find the Angle
                print("Theta  " + str(Theta))

                M = cv2.getRotationMatrix2D((cols / 2, rows / 2), Theta, 1)  # Find the Rotation Matrix
                Image = cv2.warpAffine(Image, M, (cols, rows))
                # cv2.imshow('ROTATED', Image)                                              # UNCOMMENT IF YOU WANT TO SEE THE

                Face2 = FACE_CASCADE.detectMultiScale(Image, 1.3, 5)  # This detects a face in the image
                for (FaceX, FaceY, FaceWidth, FaceHeight) in Face2:
                    CroppedFace = Image[FaceY: FaceY + FaceHeight, FaceX: FaceX + FaceWidth]
                    return CroppedFace


def tell_time_passed():
    print('TIME PASSED ' + str(round(((time.clock() - now_time) / 60), 2)) + ' MINS')
