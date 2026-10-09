import cv2
import sounddevice as sd
from scipio.io.wavfile import write
import wavio as wv

camera = cv2.VideoCapture(0)

width = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (width, height))

try:
    while True:
        ret, frame = camera.read()
        out.write(frame)

        cv2.imshow('Camera', frame)

        if cv2.waitKey(1) == ord('q'):
            break
finally:
    camera.release()
    out.release()
    cv2.destroyAllWindows()