import cv2
import sounddevice as sd
import wavio as wv
import numpy as np

camera = cv2.VideoCapture(0)

width = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
videoOut = cv2.VideoWriter('output.mp4', fourcc, 20.0, (width, height))

audioOut = np.array([], dtype=np.int16)

def callback(in_data, out_data, frame_count, time_info, status):
    global audioOut
    audioOut = np.append(audioOut, in_data)

audioStream = sd.Stream(samplerate=44100, channels=1, dtype='int16', callback=callback)

try:
    audioStream.start()
    while True:

        ret, frame = camera.read()
        videoOut.write(frame)

        cv2.imshow('Camera', frame)

        if cv2.waitKey(1) == ord('q'):
            break
finally:
    #close audio
    audioStream.stop()
    audioStream.close()
    wv.write("output.wav", audioOut, 44100)

    #close video
    camera.release()
    videoOut.release()
    cv2.destroyAllWindows()

print(audioOut)