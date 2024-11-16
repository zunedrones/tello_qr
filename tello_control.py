from tracking_base import tracking
from detect_qr import process
import time

old_move = ''
pace = ' 20'
pace_moves = ['up', 'down', 'left', 'right', 'forward', 'back']

start_time = time.time()  # Inicializa o tempo
searching = False  # Indica se a rotina de busca está ativa

def timer():
    '''
    Retorna True se o tempo desde a última detecção for maior que 10 segundos.
    '''
    global start_time
    if time.time() - start_time >= 10:
        start_time = time.time()  # Reinicia o timer
        return True
    return False

def search(tello, frame, detections):
    '''
    Função de busca que é chamada quando não há detecção de QR code após o timer expirar.
    Executa uma rotação para procurar QR codes até que haja uma detecção.
    '''
    print("Buscando QR code...")

    if detections > 0:
        print(f"Detecção encontrada")
        return frame, True  # Retorna o frame e indica que encontrou o QR code

    response = tello.send_cmd_return('cw 20')  # Rotaciona 20 graus
    print(response)
    time.sleep(0.1)  # Pequena pausa para evitar sobrecarga
    return frame, False  # Retorna o frame e False, indicando que ainda não encontrou nada

def moves(tello, frame):
    '''
    Processa o frame para detectar QR codes e executa comandos no drone Tello com base no texto detectado.
    Args:
        tello: Objeto da classe TelloZune, que possui métodos para enviar comandos e obter estado.
        frame: Frame de vídeo a ser processado para detecção de QR codes.
    Returns:
        frame: Frame processado após a detecção e execução dos comandos.
    '''
    global old_move, pace, pace_moves, searching, start_time
    
    frame, _, _, _, _, detections, text = process(frame)

    if detections > 0:
        searching = False
        start_time = time.time()  # Reinicia o timer

    if detections == 0 and old_move != 'land' and not searching:
        if timer():  # Se 10 segundos se passaram sem detecção
            searching = True
            frame, detected = search(tello, frame, detections)  # Inicia a busca
            if detected:
                searching = False  # Sai da busca ao encontrar um QR code

    if text == 'dados de leitura':
        frame = tracking(tello, frame)
    
    if detections == 1 and text == 'land':
        while float(tello.get_state_field('h')) >= 13:
            tello.send_rc_control(0, 0, -70, 0)
        tello.send_cmd(text)
        print(text)
    
    elif detections == 1 and text == 'takeoff' and old_move != 'takeoff':
        response = tello.send_cmd_return(text)
        print(text, response)
    
    elif detections == 1 and text in pace_moves:
        response = tello.send_cmd_return(f"{text}{pace}")
        if response == 'ok':
            print(f"{text}{pace}", response)

    old_move = text
    return frame
