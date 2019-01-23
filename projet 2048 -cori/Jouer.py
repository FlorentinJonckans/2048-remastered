#! /usr/bin/python3
# -*- coding: utf-8 -*-
#

import sys

from menu import *
from Mode_Normal import *
from Mode_Aveugle import *
from Mode_VS_IA import *
from Mode_VS_IA_Aveugle import *

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *

class Application(QApplication):
    def __init__(self, argv):
        super().__init__(argv)
        self.initUI()

    def initUI(self):
        # création de la palette de couleurs
        p = self.palette();
        p.setColor(QPalette.ButtonText,QColor(125,125,125))
        p.setColor(QPalette.WindowText,QColor(243, 136, 8))
        self.setPalette(p)

class Window1(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):      
        # création de la fenêtre du menu
        self.setFixedSize(1000,600)
        self.setWindowTitle('2048 Remastered!')

        # affiche " 2048 "
        self.label = QLabel(self)
        self.label.setFrameStyle(QFrame.StyledPanel | QFrame.Sunken)
        self.label.setAlignment(Qt.AlignCenter)
        font = QFont("Arial", 25, QFont.Bold)
        self.label.setFont(font)
        self.label.setText("2048")
        self.label.resize(100,50)
        self.label.move(self.frameGeometry().width()/2-self.label.frameGeometry().width()/2 -410 ,self.frameGeometry().height()/2-self.label.frameGeometry().height()/2 -240)

        # affiche une image en arrière plan
        self.setStyleSheet("background-image: url(image2.jpg)")

        # bouton 1 - Mode : Normal
        self.button1 = QPushButton("Mode : Normal",self)
        font = QFont("Arial", 20,QFont.Bold)
        self.button1.setFont(font)
        self.button1.resize(400,50)
        self.button1.move(self.frameGeometry().width()/2-self.button1.frameGeometry().width()/2 ,self.frameGeometry().height()/2-self.button1.frameGeometry().height()/2 + 0) #aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa- voir td pour bien centrer
        self.button1.clicked.connect(self.openWindowFromButtonJouer_2048_Normal)
                
        # bouton 2 - Mode : Aveugle
        self.button2 = QPushButton("Mode : Aveugle",self)
        self.button2.setFont(font)
        self.button2.resize(400,50)    
        self.button2.move(self.frameGeometry().width()/2-self.button2.frameGeometry().width()/2 ,self.frameGeometry().height()/2-self.button2.frameGeometry().height()/2 + 60) #aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa- voir td pour bien centrer
        self.button2.clicked.connect(self.openWindowFromButtonJouer_2048_Aveugle)

        # bouton 3 - Mode : Normal vs IA
        self.button3 = QPushButton("Mode : Normal vs IA",self)
        self.button3.setFont(font)
        self.button3.resize(400,50)
        self.button3.move(self.frameGeometry().width()/2-self.button3.frameGeometry().width()/2 ,self.frameGeometry().height()/2-self.button3.frameGeometry().height()/2 + 120) #aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa- voir td pour bien centrer
        self.button3.clicked.connect(self.openWindowFromButtonJouer_2048_Normal_vs_IA)
                
        # bouton 4 - Mode : Aveugle vs IA
        self.button4 = QPushButton("Mode : Aveugle vs IA",self)
        self.button4.setFont(font)
        self.button4.resize(400,50)    
        self.button4.move(self.frameGeometry().width()/2-self.button4.frameGeometry().width()/2 ,self.frameGeometry().height()/2-self.button4.frameGeometry().height()/2 + 180) #aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa- voir td pour bien centrer
        self.button4.clicked.connect(self.openWindowFromButtonJouer_2048_Aveugle_vs_IA)

        # bouton Fermer
        self.button1 = QPushButton("Fermer",self)
        font = QFont("Arial", 20,QFont.Bold)
        self.button1.setFont(font)
        self.button1.resize(150,50)
        self.button1.move(self.frameGeometry().width()/2-self.button1.frameGeometry().width()/2 -380,self.frameGeometry().height()/2-self.button1.frameGeometry().height()/2 + 240) #aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa- voir td pour bien centrer
        self.button1.clicked.connect(self.close)

        self.show()
    #----------------------------------------------------------------------------------------------------------------------
    def openWindowFromButtonJouer_2048_Normal(self):
        self.tuto = Window3()
        self.tuto.show()

    def openWindowFromButtonJouer_2048_Aveugle(self):
        self.tuto = Window4()
        self.tuto.show()

    def openWindowFromButtonJouer_2048_Normal_vs_IA(self):
        self.tuto = Window5()
        self.tuto.show()

    def openWindowFromButtonJouer_2048_Aveugle_vs_IA(self):
        self.tuto = Window6()
        self.tuto.show()
    #----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    app = Application(sys.argv)
    ex = App()
    sys.exit(app.exec_())