import cv2
from tracking_base import tracking
from detect_qr import process
import time

def moves(tello, frame):
    '''
    Processa o frame para detectar QR codes e executa comandos no drone Tello com base no texto detectado.
Args:
    tello: Objeto representando o drone Tello, que possui métodos para enviar comandos e obter estado.
    frame: Frame de vídeo a ser processado para detecção de QR codes.
Returns:
    frame: Frame processado após a detecção e execução dos comandos.
    '''
    old_move = ''
    frame , _, _, _, _, detections, text = process(frame)
    if(text == 'dados de leitura'):
        frame = tracking(tello, frame)
    if detections == 1 and text == 'land':
        while float(tello.get_state_field('h')) >= 13:
            tello.send_rc_control(0, 0, -70, 0)
        tello.send_cmd('land')
        time.sleep(1)
        print('LAND')
    elif detections == 1 and text == 'takeoff' and old_move != 'takeoff':
        response = tello.send_cmd_return('takeoff')
        old_move = 'takeoff'
        time.sleep(1)
        print('TAKEOFF')
    elif detections == 1 and text == 'up' and old_move != 'up':
        response = tello.send_cmd_return('up 20')
        old_move = 'up'
        print('UP', response)
    elif detections == 1 and text == 'down' and old_move != 'down':
        tello.send_cmd_return('down 20')
        old_move = 'down'
        print('DOWN')
    elif old_move != 'land':
        tello.send_rc_control(0, 0, 0, 0)
    
    return frame

