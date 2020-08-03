from PyQt5 import uic, QtWidgets
import pymysql
import time
import random

try:
    connect = pymysql.connect(host="localhost",
                              user="root",
                              password="32142970",
                              database="forca")
    print("Conectando ao banco de dados...")
    time.sleep(2)
    print("Conetado ao banco de dados com sucesso!")
except:
    print("Não foi possível conectar com o banco de dados...")
cursor = connect.cursor()
cursor.execute("SELECT * FROM palavras_secretas")
dados_bd = cursor.fetchall()
connect.close()
p_secretas = []
for i in range(0, len(dados_bd)):
    p_secretas.append(dados_bd[i][1])
p_secreta = random.choice(p_secretas)
print(p_secreta)

def dica(p_secreta):
    if p_secreta == "DINOSSAURO":
        return "Animal extinto a milhões de anos"
    elif p_secreta == "SUBMARINO":
        return "Veículo aquático"
    elif p_secreta == "ORNITORRINCO":
        return "Único mamímero que põe ovos"
    elif p_secreta == "LEOPARDO":
        return "Felino"
    elif p_secreta == "RAPOZA":
        return "Canino caçador de galinhas"

def comparar(palavra):
    global p_secreta
    acabou = False
    if palavra == p_secreta and vidas > 0:
        mainWindow.lineEdit_2.setText("Venceu!")
        acabou = True

    elif vidas == 0:
        mainWindow.lineEdit_2.setText("Perdeu!")
        acabou = True

    if acabou == True:
        time.sleep(3)
        mainWindow.close()

dica = dica(p_secreta)
palavra = ''
digitadas_certas = []
vidas = 6

def functionA():
    letra = "A"
    global palavra
    palavra = ''
    global p_secreta
    global digitadas_certas
    global vidas
    digitadas_certas.append(letra)
    if letra not in p_secreta:
        digitadas_certas.pop()
        vidas -= 1
    for l in p_secreta:
        if l in digitadas_certas:
            palavra += l
        else:
            palavra += '_ '
    mainWindow.lineEdit_4.setText(palavra)
    mainWindow.lineEdit_3.setText(str(vidas))
    comparar(palavra)


def functionB():
    letra = "B"
    global palavra
    palavra = ''
    global p_secreta
    global digitadas_certas
    global vidas
    digitadas_certas.append(letra)
    if letra not in p_secreta:
        digitadas_certas.pop()
        vidas -= 1
    for l in p_secreta:
        if l in digitadas_certas:
            palavra += l
        else:
            palavra += '_ '
    mainWindow.lineEdit_4.setText(palavra)
    mainWindow.lineEdit_3.setText(str(vidas))
    comparar(palavra)

def functionC():
    letra = "C"
    global palavra
    palavra = ''
    global p_secreta
    global digitadas_certas
    global vidas
    digitadas_certas.append(letra)
    if letra not in p_secreta:
        digitadas_certas.pop()
        vidas -= 1
    for l in p_secreta:
        if l in digitadas_certas:
            palavra += l
        else:
            palavra += '_ '
    mainWindow.lineEdit_4.setText(palavra)
    mainWindow.lineEdit_3.setText(str(vidas))
    comparar(palavra)

def functionD():
    letra = "D"
    global palavra
    palavra = ''
    global p_secreta
    global digitadas_certas
    global vidas
    digitadas_certas.append(letra)
    if letra not in p_secreta:
        digitadas_certas.pop()
        vidas -= 1
    for l in p_secreta:
        if l in digitadas_certas:
            palavra += l
        else:
            palavra += '_ '
    mainWindow.lineEdit_4.setText(palavra)
    mainWindow.lineEdit_3.setText(str(vidas))
    comparar(palavra)

def functionE():
    letra = "E"
    global palavra
    palavra = ''
    global p_secreta
    global digitadas_certas
    global vidas
    digitadas_certas.append(letra)
    if letra not in p_secreta:
        digitadas_certas.pop()
        vidas -= 1
    for l in p_secreta:
        if l in digitadas_certas:
            palavra += l
        else:
            palavra += '_ '
    mainWindow.lineEdit_4.setText(palavra)
    mainWindow.lineEdit_3.setText(str(vidas))
    comparar(palavra)

def functionF():
    letra = "F"
    global palavra
    palavra = ''
    global p_secreta
    global digitadas_certas
    global vidas
    digitadas_certas.append(letra)
    if letra not in p_secreta:
        digitadas_certas.pop()
        vidas -= 1
    for l in p_secreta:
        if l in digitadas_certas:
            palavra += l
        else:
            palavra += '_ '
    mainWindow.lineEdit_4.setText(palavra)
    mainWindow.lineEdit_3.setText(str(vidas))
    comparar(palavra)

def functionG():
    letra = "G"
    global palavra
    palavra = ''
    global p_secreta
    global digitadas_certas
    global vidas
    digitadas_certas.append(letra)
    if letra not in p_secreta:
        digitadas_certas.pop()
        vidas -= 1
    for l in p_secreta:
        if l in digitadas_certas:
            palavra += l
        else:
            palavra += '_ '
    mainWindow.lineEdit_4.setText(palavra)
    mainWindow.lineEdit_3.setText(str(vidas))
    comparar(palavra)

def functionH():
    letra = "H"
    global palavra
    palavra = ''
    global p_secreta
    global digitadas_certas
    global vidas
    digitadas_certas.append(letra)
    if letra not in p_secreta:
        digitadas_certas.pop()
        vidas -= 1
    for l in p_secreta:
        if l in digitadas_certas:
            palavra += l
        else:
            palavra += '_ '
    mainWindow.lineEdit_4.setText(palavra)
    mainWindow.lineEdit_3.setText(str(vidas))
    comparar(palavra)

def functionI():
    letra = "I"
    global palavra
    palavra = ''
    global p_secreta
    global digitadas_certas
    global vidas
    digitadas_certas.append(letra)
    if letra not in p_secreta:
        digitadas_certas.pop()
        vidas -= 1
    for l in p_secreta:
        if l in digitadas_certas:
            palavra += l
        else:
            palavra += '_ '
    mainWindow.lineEdit_4.setText(palavra)
    mainWindow.lineEdit_3.setText(str(vidas))
    comparar(palavra)

def functionJ():
    letra = "J"
    global palavra
    palavra = ''
    global p_secreta
    global digitadas_certas
    global vidas
    digitadas_certas.append(letra)
    if letra not in p_secreta:
        digitadas_certas.pop()
        vidas -= 1
    for l in p_secreta:
        if l in digitadas_certas:
            palavra += l
        else:
            palavra += '_ '
    mainWindow.lineEdit_4.setText(palavra)
    mainWindow.lineEdit_3.setText(str(vidas))
    comparar(palavra)

def functionK():
    letra = "K"
    global palavra
    palavra = ''
    global p_secreta
    global digitadas_certas
    global vidas
    digitadas_certas.append(letra)
    if letra not in p_secreta:
        digitadas_certas.pop()
        vidas -= 1
    for l in p_secreta:
        if l in digitadas_certas:
            palavra += l
        else:
            palavra += '_ '
    mainWindow.lineEdit_4.setText(palavra)
    mainWindow.lineEdit_3.setText(str(vidas))
    comparar(palavra)

def functionL():
    letra = "L"
    global palavra
    palavra = ''
    global p_secreta
    global digitadas_certas
    global vidas
    digitadas_certas.append(letra)
    if letra not in p_secreta:
        digitadas_certas.pop()
        vidas -= 1
    for l in p_secreta:
        if l in digitadas_certas:
            palavra += l
        else:
            palavra += '_ '
    mainWindow.lineEdit_4.setText(palavra)
    mainWindow.lineEdit_3.setText(str(vidas))
    comparar(palavra)

def functionM():
    letra = "M"
    global palavra
    palavra = ''
    global p_secreta
    global digitadas_certas
    global vidas
    digitadas_certas.append(letra)
    if letra not in p_secreta:
        digitadas_certas.pop()
        vidas -= 1
    for l in p_secreta:
        if l in digitadas_certas:
            palavra += l
        else:
            palavra += '_ '
    mainWindow.lineEdit_4.setText(palavra)
    mainWindow.lineEdit_3.setText(str(vidas))
    comparar(palavra)

def functionN():
    letra = "N"
    global palavra
    palavra = ''
    global p_secreta
    global digitadas_certas
    global vidas
    digitadas_certas.append(letra)
    if letra not in p_secreta:
        digitadas_certas.pop()
        vidas -= 1
    for l in p_secreta:
        if l in digitadas_certas:
            palavra += l
        else:
            palavra += '_ '
    mainWindow.lineEdit_4.setText(palavra)
    mainWindow.lineEdit_3.setText(str(vidas))
    comparar(palavra)

def functionO():
    letra = "O"
    global palavra
    palavra = ''
    global p_secreta
    global digitadas_certas
    global vidas
    digitadas_certas.append(letra)
    if letra not in p_secreta:
        digitadas_certas.pop()
        vidas -= 1
    for l in p_secreta:
        if l in digitadas_certas:
            palavra += l
        else:
            palavra += '_ '
    mainWindow.lineEdit_4.setText(palavra)
    mainWindow.lineEdit_3.setText(str(vidas))
    comparar(palavra)

def functionP():
    letra = "P"
    global palavra
    palavra = ''
    global p_secreta
    global digitadas_certas
    global vidas
    digitadas_certas.append(letra)
    if letra not in p_secreta:
        digitadas_certas.pop()
        vidas -= 1
    for l in p_secreta:
        if l in digitadas_certas:
            palavra += l
        else:
            palavra += '_ '
    mainWindow.lineEdit_4.setText(palavra)
    mainWindow.lineEdit_3.setText(str(vidas))
    comparar(palavra)

def functionQ():
    letra = "Q"
    global palavra
    palavra = ''
    global p_secreta
    global digitadas_certas
    global vidas
    digitadas_certas.append(letra)
    if letra not in p_secreta:
        digitadas_certas.pop()
        vidas -= 1
    for l in p_secreta:
        if l in digitadas_certas:
            palavra += l
        else:
            palavra += '_ '
    mainWindow.lineEdit_4.setText(palavra)
    mainWindow.lineEdit_3.setText(str(vidas))
    comparar(palavra)

def functionR():
    letra = "R"
    global palavra
    palavra = ''
    global p_secreta
    global digitadas_certas
    global vidas
    digitadas_certas.append(letra)
    if letra not in p_secreta:
        digitadas_certas.pop()
        vidas -= 1
    for l in p_secreta:
        if l in digitadas_certas:
            palavra += l
        else:
            palavra += '_ '
    mainWindow.lineEdit_4.setText(palavra)
    mainWindow.lineEdit_3.setText(str(vidas))
    comparar(palavra)

def functionS():
    letra = "S"
    global palavra
    palavra = ''
    global p_secreta
    global digitadas_certas
    global vidas
    digitadas_certas.append(letra)
    if letra not in p_secreta:
        digitadas_certas.pop()
        vidas -= 1
    for l in p_secreta:
        if l in digitadas_certas:
            palavra += l
        else:
            palavra += '_ '
    mainWindow.lineEdit_4.setText(palavra)
    mainWindow.lineEdit_3.setText(str(vidas))
    comparar(palavra)

def functionT():
    letra = "T"
    global palavra
    palavra = ''
    global p_secreta
    global digitadas_certas
    global vidas
    digitadas_certas.append(letra)
    if letra not in p_secreta:
        digitadas_certas.pop()
        vidas -= 1
    for l in p_secreta:
        if l in digitadas_certas:
            palavra += l
        else:
            palavra += '_ '
    mainWindow.lineEdit_4.setText(palavra)
    mainWindow.lineEdit_3.setText(str(vidas))
    comparar(palavra)

def functionU():
    letra = "U"
    global palavra
    palavra = ''
    global p_secreta
    global digitadas_certas
    global vidas
    digitadas_certas.append(letra)
    if letra not in p_secreta:
        digitadas_certas.pop()
        vidas -= 1
    for l in p_secreta:
        if l in digitadas_certas:
            palavra += l
        else:
            palavra += '_ '
    mainWindow.lineEdit_4.setText(palavra)
    mainWindow.lineEdit_3.setText(str(vidas))
    comparar(palavra)

def functionV():
    letra = "V"
    global palavra
    palavra = ''
    global p_secreta
    global digitadas_certas
    global vidas
    digitadas_certas.append(letra)
    if letra not in p_secreta:
        digitadas_certas.pop()
        vidas -= 1
    for l in p_secreta:
        if l in digitadas_certas:
            palavra += l
        else:
            palavra += '_ '
    mainWindow.lineEdit_4.setText(palavra)
    mainWindow.lineEdit_3.setText(str(vidas))
    comparar(palavra)

def functionW():
    letra = "W"
    global palavra
    palavra = ''
    global p_secreta
    global digitadas_certas
    global vidas
    digitadas_certas.append(letra)
    if letra not in p_secreta:
        digitadas_certas.pop()
        vidas -= 1
    for l in p_secreta:
        if l in digitadas_certas:
            palavra += l
        else:
            palavra += '_ '
    mainWindow.lineEdit_4.setText(palavra)
    mainWindow.lineEdit_3.setText(str(vidas))
    comparar(palavra)

def functionX():
    letra = "X"
    global palavra
    palavra = ''
    global p_secreta
    global digitadas_certas
    global vidas
    digitadas_certas.append(letra)
    if letra not in p_secreta:
        digitadas_certas.pop()
        vidas -= 1
    for l in p_secreta:
        if l in digitadas_certas:
            palavra += l
        else:
            palavra += '_ '
    mainWindow.lineEdit_4.setText(palavra)
    mainWindow.lineEdit_3.setText(str(vidas))
    comparar(palavra)

def functionY():
    letra = "Y"
    global palavra
    palavra = ''
    global p_secreta
    global digitadas_certas
    global vidas
    digitadas_certas.append(letra)
    if letra not in p_secreta:
        digitadas_certas.pop()
        vidas -= 1
    for l in p_secreta:
        if l in digitadas_certas:
            palavra += l
        else:
            palavra += '_ '
    mainWindow.lineEdit_4.setText(palavra)
    mainWindow.lineEdit_3.setText(str(vidas))
    comparar(palavra)

def functionZ():
    letra = "Z"
    global palavra
    palavra = ''
    global p_secreta
    global digitadas_certas
    global vidas
    digitadas_certas.append(letra)
    if letra not in p_secreta:
        digitadas_certas.pop()
        vidas -= 1
    for l in p_secreta:
        if l in digitadas_certas:
            palavra += l
        else:
            palavra += '_ '
    mainWindow.lineEdit_4.setText(palavra)
    mainWindow.lineEdit_3.setText(str(vidas))
    comparar(palavra)


app = QtWidgets.QApplication([])
mainWindow = uic.loadUi("mainWindow.ui")
mainWindow.lineEdit.setText(dica)
mainWindow.lineEdit_3.setText("6")
mainWindow.lineEdit_4.setText(palavra)
mainWindow.toolButtonA.clicked.connect(functionA)
mainWindow.toolButtonB.clicked.connect(functionB)
mainWindow.toolButtonC.clicked.connect(functionC)
mainWindow.toolButtonD.clicked.connect(functionD)
mainWindow.toolButtonE.clicked.connect(functionE)
mainWindow.toolButtonF.clicked.connect(functionF)
mainWindow.toolButtonG.clicked.connect(functionG)
mainWindow.toolButtonH.clicked.connect(functionH)
mainWindow.toolButtonI.clicked.connect(functionI)
mainWindow.toolButtonJ.clicked.connect(functionJ)
mainWindow.toolButtonK.clicked.connect(functionK)
mainWindow.toolButtonL.clicked.connect(functionL)
mainWindow.toolButtonM.clicked.connect(functionM)
mainWindow.toolButtonN.clicked.connect(functionN)
mainWindow.toolButtonO.clicked.connect(functionO)
mainWindow.toolButtonP.clicked.connect(functionP)
mainWindow.toolButtonQ.clicked.connect(functionQ)
mainWindow.toolButtonR.clicked.connect(functionR)
mainWindow.toolButtonS.clicked.connect(functionS)
mainWindow.toolButtonT.clicked.connect(functionT)
mainWindow.toolButtonU.clicked.connect(functionU)
mainWindow.toolButtonV.clicked.connect(functionV)
mainWindow.toolButtonW.clicked.connect(functionW)
mainWindow.toolButtonX.clicked.connect(functionX)
mainWindow.toolButtonY.clicked.connect(functionY)
mainWindow.toolButtonZ.clicked.connect(functionZ)


mainWindow.show()
app.exec()