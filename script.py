import cv2
import sys
import os

if len(sys.argv) > 1:
    directorio = "frames"
    try:
        os.stat(directorio)
    except:
        os.mkdir(directorio)

    vidcap = cv2.VideoCapture(sys.argv[1])
    success, image = vidcap.read()
    count = 0
    while success:
        cv2.imwrite(directorio+"/frame%d.jpg" % count, image)
        success, image = vidcap.read()
        print("Siguente frame")
        count += 1
else:
    print("No hay suficientes parametros")
