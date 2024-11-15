from tracking_base import tracking
from detect_qr import process
import time

def moves(tello, frame):
    '''
    Processa o frame para detectar QR codes e executa comandos no drone Tello com base no texto detectado.
Args:
    tello: Objeto da classe TelloZune, que possui métodos para enviar comandos e obter estado.
    frame: Frame de vídeo a ser processado para detecção de QR codes.
Returns:
    frame: Frame processado após a detecção e execução dos comandos.
    '''
    old_move = ''
    pace = ' 20'
    pace_moves = ['up', 'down', 'left', 'right', 'forward', 'back']
    frame, _, _, _, _, detections, text = process(frame)
    if text == 'dados de leitura': # lembrar de imprimir um qrcode: 'follow'
        frame = tracking(tello, frame)
    if detections == 1 and text == 'land':
        while float(tello.get_state_field('h')) >= 13:
            tello.send_rc_control(0, 0, -70, 0)
        tello.send_cmd(text)
        print(text)
        #time.sleep(1)
    elif detections == 1 and text == 'takeoff' and old_move != 'takeoff':
        response = tello.send_cmd_return(text)
        print(text, response)
        #time.sleep(1)
    elif detections == 1 and text in pace_moves: # movimentos com passo
        response = tello.send_cmd_return(f"{text}' '{pace}")
        if response == 'ok':
            print(f"{text}' '{pace}", response)
    else: # rotina para procurar QR code
        if detections == 0 and old_move != 'land':
            response = tello.send_cmd_return('cw 20')
            if response == 'ok':
                print('cw 20', response)
        tello.send_rc_control(0, 0, 0, 0) # testar
        time.sleep(0.1)
    #print(f'texto lido: {text}')
    old_move = text
    response = ''
    return frame

