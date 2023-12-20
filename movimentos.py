import time
from flask import Flask, render_template, request, jsonify
import socket
import binascii


app = Flask(__name__)
TCP_IP = '192.168.1.1'
TCP_PORT = 2001
BUFFER_SIZE = 1024



def send_msg(message):
 s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 s.connect((TCP_IP, TCP_PORT))
 s.send(binascii.unhexlify(message))
 s.close()

angulo_servo1 = 45
angulo_servo2 = 45
angulo_servo3 = 45
angulo_servo4 = 45
angulo_servo5 = 45
angulo_servo6 = 45
angulo_servo7 = 45
angulo_servo8 = 45

@app.route("/", methods=['GET', 'POST'])
def robo():
    global angulo_servo1
    global angulo_servo2
    global angulo_servo3
    global angulo_servo4
    global angulo_servo5
    global angulo_servo6
    global angulo_servo7
    global angulo_servo8

    if request.method == 'POST':
        if request.form.get('Frente') == 'Frente':
            send_msg("FF000300FF")
            time.sleep(0.1)
            send_msg("FF000000FF")

        elif request.form.get('Tras') == 'Tras':
            send_msg("FF000400FF")
            time.sleep(0.1)
            send_msg("FF000000FF")

        elif request.form.get('Parar') == 'Parar':
            send_msg("FF000000FF")


        elif request.form.get('Direita') == 'Direita':

            send_msg("FF000200FF")
            time.sleep(0.1)
            send_msg("FF000000FF")

        elif request.form.get('Esquerda') == 'Esquerda':
            send_msg("FF000100FF")
            time.sleep(0.1)
            send_msg("FF000000FF")

            # camera lado

        elif request.form.get('Câmera Lado') == 'Câmera Lado':

            angulo_servo1 = angulo_servo1 + 5

            anguloHexa = hex(angulo_servo1)[2:].upper()

            print(f'Servo: {angulo_servo1}; Hexa: {anguloHexa}')

            if angulo_servo1 < 20:
                send_msg("FF0101" + str(anguloHexa) + "FF")
                time.sleep(0.1)
                send_msg("FF000000FF")
            else:
                send_msg("FF0101" + str(anguloHexa) + "FF")
                time.sleep(0.1)
                send_msg("FF000000FF")
                # camera baixo

        elif request.form.get('Câmera Baixo') == 'Câmera Baixo':
            angulo_servo2 += 5
            anguloHexa = hex(angulo_servo2)[2:].zfill(2).upper()

            print(f'Servo: {angulo_servo2}; Hexa: {anguloHexa}')
            if angulo_servo2 < 20:
                send_msg("FF0102" + anguloHexa + "FF")
                time.sleep(0.1)
                send_msg("FF000000FF")
            else:
                send_msg("FF0102" + anguloHexa + "FF")
                time.sleep(0.1)
                send_msg("FF000000FF")

                # BRAÇO CIMA
        elif request.form.get('Levantar o Braço') == 'Levantar o Braço':
            angulo_servo3 += 5
            anguloHexa = hex(angulo_servo3)[2:].upper()
            print(f'Servo: {angulo_servo3}; Hexa: {anguloHexa}')
            if angulo_servo3 < 20:
                send_msg("FF0103" + anguloHexa + "FF")
                time.sleep(0.1)
                send_msg("FF000000FF")
            else:
                send_msg("FF0103" + anguloHexa + "FF")
                time.sleep(0.1)
                send_msg("FF000000FF")

        elif request.form.get('Mexe a menor parte do braço para cima') == 'Mexe a menor parte do braço para cima':
            angulo_servo4 += 5
            anguloHexa = hex(angulo_servo4)[2:].upper()
            print(f'Servo: {angulo_servo4}; Hexa: {anguloHexa}')
            if angulo_servo4 < 20:
                send_msg("FF0104" + anguloHexa + "FF")
                time.sleep(0.1)
                send_msg("FF000000FF")
            else:
                send_msg("FF0104" + anguloHexa + "FF")
                time.sleep(0.1)
                send_msg("FF000000FF")

        elif request.form.get('Pinça Lado') == 'Pinça Lado':
            angulo_servo5 += 5
            anguloHexa = hex(angulo_servo5)[2:].upper()
            print(f'Servo: {angulo_servo5}; Hexa: {anguloHexa}')
            if angulo_servo5 < 20:
                send_msg("FF0105" + anguloHexa + "FF")
                time.sleep(0.1)
                send_msg("FF000000FF")
            else:
                send_msg("FF0105" + anguloHexa + "FF")
                time.sleep(0.1)
                send_msg("FF000000FF")

        elif request.form.get('Fechar Pinça') == 'Fechar Pinça':
            angulo_servo6 += 5
            anguloHexa = hex(angulo_servo6)[2:].upper()
            print(f'Servo: {angulo_servo6}; Hexa: {anguloHexa}')
            if angulo_servo6 < 20:
                send_msg("FF0106" + anguloHexa + "FF")
                time.sleep(0.1)
                send_msg("FF000000FF")
            else:
                send_msg("FF0106" + anguloHexa + "FF")
                time.sleep(0.1)
                send_msg("FF000000FF")

        elif request.form.get('Câmera Lado Oposto') == 'Câmera Lado Oposto':
            angulo_servo1 -= 5
            anguloHexa = hex(angulo_servo1)[2:].upper()
            print(f'Servo: {angulo_servo1}; Hexa: {anguloHexa}')
            if angulo_servo1 < 20:
                send_msg("FF0101" + anguloHexa + "FF")
                time.sleep(0.1)
                send_msg("FF000000FF")
            else:
                send_msg("FF0101" + anguloHexa + "FF")
                time.sleep(0.1)
                send_msg("FF000000FF")

        elif request.form.get('Câmera Cima') == 'Câmera Cima':
            angulo_servo2 -= 5
            anguloHexa = hex(angulo_servo2)[2:].upper()
            print(f'Servo: {angulo_servo2}; Hexa: {anguloHexa}')
            if angulo_servo2 < 20:
                send_msg("FF0102" + anguloHexa + "FF")
                time.sleep(0.1)
                send_msg("FF000000FF")
            else:
                send_msg("FF0102" + anguloHexa + "FF")
                time.sleep(0.1)
                send_msg("FF000000FF")

        elif request.form.get('Baixar o Braço') == 'Baixar o Braço':
            angulo_servo3 -= 5
            anguloHexa = hex(angulo_servo3)[2:].upper()
            print(f'Servo: {angulo_servo1}; Hexa: {anguloHexa}')
            if angulo_servo3 < 10:
                send_msg("FF0103" + anguloHexa + "FF")
                time.sleep(0.1)
                send_msg("FF000000FF")
            else:
                send_msg("FF0103" + anguloHexa + "FF")
                time.sleep(0.1)
                send_msg("FF000000FF")

        elif request.form.get('Mexe a menor parte do braço para baixo') == 'Mexe a menor parte do braço para baixo':
            angulo_servo4 -= 5
            anguloHexa = hex(angulo_servo4)[2:].upper()
            print(f'Servo: {angulo_servo1}; Hexa: {anguloHexa}')
            if angulo_servo4 < 20:
                send_msg("FF0104" + anguloHexa + "FF")
                time.sleep(0.1)
                send_msg("FF000000FF")
            else:
                send_msg("FF0104" + anguloHexa + "FF")
                time.sleep(0.1)
                send_msg("FF000000FF")

        elif request.form.get('Pinça Lado Oposto') == 'Pinça Lado Oposto':
            angulo_servo5 -= 5
            anguloHexa = hex(angulo_servo5)[2:].upper()
            print(f'Servo: {angulo_servo1}; Hexa: {anguloHexa}')
            if angulo_servo5 < 20:
                send_msg("FF0105" + anguloHexa + "FF")
                time.sleep(0.1)
                send_msg("FF000000FF")
            else:
                send_msg("FF0105" + anguloHexa + "FF")
                time.sleep(0.1)
                send_msg("FF000000FF")

        elif request.form.get('Abrir Pinça') == 'Abrir Pinça':
            angulo_servo6 -= 5
            anguloHexa = hex(angulo_servo6)[2:].upper()
            print(f'Servo: {angulo_servo1}; Hexa: {anguloHexa}')
            if angulo_servo6 < 10:
                send_msg("FF0106" + anguloHexa + "FF")
                time.sleep(0.1)
                send_msg("FF000000FF")
            else:
                send_msg("FF0106" + anguloHexa + "FF")
                time.sleep(0.1)
                send_msg("FF000000FF")

    elif request.method == 'GET':
        return render_template('robo.html')

    return render_template("robo.html")

if __name__ == "__main__":
    # Start the control_robot thread
   # robot_thread = threading.Thread(target=control_robot)
   # robot_thread.start()
    # Run the Flask app
    app.run(debug=True)