import cv2
from pyzbar.pyzbar import decode

data = []
x, y, w, h = 0, 0, 0, 0

"""
Recebe um frame, detecta os códigos desenhando as bordas e o texto,
armazena o texto em uma lista e retorna o frame
"""
def process(frame):
    decoded_objects = decode(frame)
    global x, y, w, h, data, qr_text
    qr_text = ''
    for obj in decoded_objects:
        (x, y, w, h) = obj.rect
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 255), 2)
        qr_text = obj.data.decode('utf-8')
        cv2.circle(frame, (x + w // 2, y + h // 2), 5, (0, 0, 255), cv2.FILLED)
        cv2.putText(frame, qr_text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        #print(qr_text)
        if qr_text not in data:
            data.append(qr_text)
    #print(data)
    return [frame, x, y, x+w, y+h, len(decoded_objects), qr_text]

#cv2.namedWindow('QR Code', cv2.WINDOW_AUTOSIZE)
