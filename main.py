import time
import keyboard
from flask import Flask, render_template, request, jsonify
import socket
import binascii
import threading

app = Flask(__name__)
TCP_IP = '192.168.1.1'
TCP_PORT = 2001
BUFFER_SIZE = 1024


def send_msg(message):
 s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 s.connect((TCP_IP, TCP_PORT))
 s.send(binascii.unhexlify(message))
 s.close()

# Ângulo inicial

angulo_servo1=0
angulo_servo2=0
angulo_servo3=0
angulo_servo4=0
angulo_servo5=0
angulo_servo6=0
angulo_servo7=0
angulo_servo8=0


while True:

    # Comandos para mexer o robo

    #Forward-Frente
    if keyboard.is_pressed('f'):
        send_msg("FF000300FF")
    #Stop - Para
    elif keyboard.is_pressed('s'):
        send_msg("FF000000FF")

    #Backward - Tras
    elif keyboard.is_pressed('t'):
        send_msg("FF000400FF")

    #TurnLeft-Esquerda
    elif keyboard.is_pressed('e'):
        send_msg("FF000100FF")
        time.sleep(0.1)
        send_msg("FF000000FF")

    #TurnRight-Direita
    elif keyboard.is_pressed('d'):
        send_msg("FF000200FF")
        time.sleep(0.1)
        send_msg("FF000000FF")

    # Comandos para mexer o braço

    # Mexe a camera para o lado- aumenta o angulo
    elif keyboard.is_pressed('1'):
        angulo_servo1 += 5
        anguloHexa= hex(angulo_servo1)[2:].upper()
        if angulo_servo1<20:
            send_msg("FF01010"+ anguloHexa + "FF")
            time.sleep(0.1)
            send_msg("FF000000FF")
        else:
            send_msg("FF0101" + anguloHexa + "FF")
            time.sleep(0.1)
            send_msg("FF000000FF")

    # Mexe a camera para baixo - aumenta o angulo
    elif keyboard.is_pressed('2'):

        angulo_servo2 += 5
        anguloHexa= hex(angulo_servo2 )[2:].upper()
        if angulo_servo2  < 20:
            send_msg("FF01020" + anguloHexa + "FF")
            time.sleep(0.1)
            send_msg("FF000000FF")
        else:
            send_msg("FF0102"+ anguloHexa + "FF")
            time.sleep(0.1)
            send_msg("FF000000FF")

    # Mexe braço para cima - aumenta o angulo
    elif keyboard.is_pressed('3'):

        angulo_servo3 += 5
        anguloHexa= hex(angulo_servo3)[2:].upper()
        if angulo_servo3 < 20:
            send_msg("FF01030"+ anguloHexa + "FF")
            time.sleep(0.1)
            send_msg("FF000000FF")
        else:
            send_msg("FF0103" + anguloHexa + "FF")
            time.sleep(0.1)
            send_msg("FF000000FF")

    # Mexe a menor parte do braço para cima - aumenta o angulo
    elif keyboard.is_pressed('4'):

        angulo_servo4 += 5
        anguloHexa= hex( angulo_servo4)[2:].upper()
        if  angulo_servo4 < 20:
            send_msg("FF01040"+ anguloHexa + "FF")
            time.sleep(0.1)
            send_msg("FF000000FF")
        else:
            send_msg("FF0104" + anguloHexa + "FF")
            time.sleep(0.1)
            send_msg("FF000000FF")

    # Mexe a pinça pro lado - aumenta o angulo
    elif keyboard.is_pressed('5'):

        angulo_servo5 += 5
        anguloHexa= hex(angulo_servo5)[2:].upper()
        if angulo_servo5 < 20:
            send_msg("FF01050"+ anguloHexa + "FF")
            time.sleep(0.1)
            send_msg("FF000000FF")
        else:
            send_msg("FF0105" + anguloHexa + "FF")
            time.sleep(0.1)
            send_msg("FF000000FF")

    # Fecha a pinça - aumenta o angulo

    elif keyboard.is_pressed('6'):

        angulo_servo6 += 5
        anguloHexa= hex(angulo_servo6)[2:].upper()
        if angulo_servo6 < 20:
            send_msg("FF01060"+ anguloHexa + "FF")
            time.sleep(0.1)
            send_msg("FF000000FF")
        else:
            send_msg("FF0106" + anguloHexa + "FF")
            time.sleep(0.1)
            send_msg("FF000000FF")


    elif keyboard.is_pressed('7'):

        angulo_servo7 += 5
        anguloHexa= hex(angulo_servo7)[2:].upper()
        if angulo_servo7 < 20:
            send_msg("FF01070"+ anguloHexa + "FF")
            time.sleep(0.1)
            send_msg("FF000000FF")
        else:
            send_msg("FF0107" + anguloHexa + "FF")
            time.sleep(0.1)
            send_msg("FF000000FF")

    elif keyboard.is_pressed('8'):

        angulo_servo8 += 5
        anguloHexa= hex(angulo_servo8)[2:].upper()
        if angulo_servo8 < 40:
            send_msg("FF01080"+ anguloHexa + "FF")
            time.sleep(0.1)
            send_msg("FF000000FF")
        else:
            send_msg("FF0108" + anguloHexa + "FF")
            time.sleep(0.1)
            send_msg("FF000000FF")



    # Mexe a camera para o lado - decrementa o angulo
    elif keyboard.is_pressed('m'):

        angulo_servo1 -= 5
        anguloHexa = hex(angulo_servo1)[2:].upper()
        if angulo_servo1 < 20:
            send_msg("FF01010" + anguloHexa + "FF")
            time.sleep(0.1)
            send_msg("FF000000FF")

        else:
            send_msg("FF0101" + anguloHexa + "FF")
            time.sleep(0.1)
            send_msg("FF000000FF")

    # Mexe a camera para cima - decrementa o angulo
    elif keyboard.is_pressed('n'):

        angulo_servo2 -= 5
        anguloHexa = hex(angulo_servo2)[2:].upper()
        if angulo_servo2 < 20:
            send_msg("FF01020" + anguloHexa + "FF")
            time.sleep(0.1)
            send_msg("FF000000FF")

        else:
            send_msg("FF0102" + anguloHexa + "FF")
            time.sleep(0.1)
            send_msg("FF000000FF")

    # Mexe braço para baixo - decrementa o angulo
    elif keyboard.is_pressed('b'):
        angulo_servo3 -= 5
        anguloHexa= hex(angulo_servo3)[2:].upper()
        if angulo_servo3 < 10:
            send_msg("FF01030"+ anguloHexa + "FF")
            time.sleep(0.1)
            send_msg("FF000000FF")
        else:
            send_msg("FF0103" + anguloHexa + "FF")
            time.sleep(0.1)
            send_msg("FF000000FF")



    # Mexe a menor parte do braço para baixo - aumenta o angulo
    elif keyboard.is_pressed('v'):

        angulo_servo4 -= 5
        anguloHexa= hex( angulo_servo4)[2:].upper()
        if  angulo_servo4 < 20:
            send_msg("FF01040"+ anguloHexa + "FF")
            time.sleep(0.1)
            send_msg("FF000000FF")
        else:
            send_msg("FF0104" + anguloHexa + "FF")
            time.sleep(0.1)
            send_msg("FF000000FF")


    # Mexe a pinça pro lado- aumenta o angulo
    elif keyboard.is_pressed('c'):

        angulo_servo5 -= 5
        anguloHexa= hex(angulo_servo5)[2:].upper()
        if angulo_servo5 < 20:
            send_msg("FF01050"+ anguloHexa + "FF")
            time.sleep(0.1)
            send_msg("FF000000FF")
        else:
            send_msg("FF0105" + anguloHexa + "FF")
            time.sleep(0.1)
            send_msg("FF000000FF")

    # Abre a pinça - aumenta o angulo
    elif keyboard.is_pressed('x'):

        angulo_servo6 -= 5
        anguloHexa= hex(angulo_servo6)[2:].upper()
        if angulo_servo6 < 10:
            send_msg("FF01060"+ anguloHexa + "FF")
            time.sleep(0.1)
            send_msg("FF000000FF")
        else:
            send_msg("FF0106" + anguloHexa + "FF")
            time.sleep(0.1)
            send_msg("FF000000FF")
            #REVER

    elif keyboard.is_pressed('z'):

        angulo_servo7 -= 5
        anguloHexa= hex(angulo_servo7)[2:].upper()
        if angulo_servo7 < 20:
            send_msg("FF01070"+ anguloHexa + "FF")
            time.sleep(0.1)
            send_msg("FF000000FF")
        else:
            send_msg("FF0107" + anguloHexa + "FF")
            time.sleep(0.1)
            send_msg("FF000000FF")

    elif keyboard.is_pressed('a'):

        angulo_servo8 += 5
        anguloHexa= hex(angulo_servo8)[2:].upper()
        if angulo_servo8 < 40:
            send_msg("FF01080"+ anguloHexa + "FF")
            time.sleep(0.1)
            send_msg("FF000000FF")
        else:
            send_msg("FF0108" + anguloHexa + "FF")
            time.sleep(0.1)
            send_msg("FF000000FF")


@app.route('/Conexão', methods=['GET'])
def conexão():

    return render_template('robo.html')

@app.route('/control', methods=['POST'])
def write_data_server():
    key_pressed = request.form['keyboard.is_pressed']
    # Handle key press if needed

if __name__ == "__main__":
    # Start the control_robot thread
    robot_thread = threading.Thread(target=control_robot)
    robot_thread.start()

    # Run the Flask app
    app.run(debug=True)