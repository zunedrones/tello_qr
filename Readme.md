# Tello QR

## Descrição

Aplicações de visão computacional para navegação do drone DJI Tello utilizando Python. O drone se locomove de acordo com os comandos recebidos pela leitura dos códigos QR.

## Tabela de Comandos

| Comando         | Descrição                    |
|-----------------|------------------------------|
| `takeoff`       | Decolar                      |
| `land`          | Pousar                       |
| `up x`          | Subir x cm                   |
| `down x`        | Descer x cm                  |
| `right x`       | Mover-se à direita x cm      |
| `left x`        | Mover-se à esquerda x cm     |
| `forward x`     | Mover-se para frente x cm    |
| `back x`        | Mover-se para trás x cm      |

## Instalação

Siga as instruções abaixo para instalar e configurar o projeto:

```bash
# Clone o repositório
git clone https://github.com/zunedrones/tello_qr
```
# Navegue até o diretório do projeto
cd tello_qr

```bash
# Instalar dependências
pip install opencv-python
pip install pyzbar
pip install tello_zune
```