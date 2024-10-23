from tello_zune import TelloZune
import cv2
from tracking_base import tracking

#cap = cv2.VideoCapture(0)

tello = TelloZune()
tello.start_tello()

while True:
    #ret, frame = cap.read()
    frame = tello.get_frame()
    tello.calc_fps(frame)
    frame = cv2.resize(frame, (800, 600))
    
    tracking(tello, frame)
    cv2.imshow('QR Code', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
#print(data)
#cap.release()
tello.end_tello()
cv2.destroyAllWindows()

