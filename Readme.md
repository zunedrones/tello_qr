# Tello QR

## Descrição

Aplicações de visão computacional para navegação do drone DJI Tello utilizando Python. 
O drone se locomove de acordo com os comandos recebidos pela leitura dos códigos QR.

## Tabela de comandos

- [takeoff](decolar)
- [land](pousar)
- [up x]('subir x cm')
- [down x](descer x cm)
- [right x](mover-se à direita x cm)
- [left x](mover-se à esquerda x cm)
- [forward x](mover-se para frente x cm)
- [back x](mover-se para trás x cm)

## Installation

```bash
# Clone o repositório
git clone https://github.com/zunedrones/tello_qr

# Instalar dependências
pip install cv2
pip install pyzbar
pip install tello_zune

# Any additional setup steps