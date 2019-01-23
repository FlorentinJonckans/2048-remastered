#! /usr/bin/python3
# -*- coding: utf-8 -*-
#

import sys

from menu import *
from Jouer import *

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *


class Application(QApplication):
    def __init__(self, argv):
        super().__init__(argv)
        self.initUI()

    def initUI(self):
        #Création de la palette de couleurs
        p = self.palette();
        p.setColor(QPalette.ButtonText,QColor(125,125,125))
        p.setColor(QPalette.WindowText,QColor(243, 136, 8))
        self.setPalette(p)

class Window2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):        
        # création de la fenêtre du menu
        self.setFixedSize(1000,600)
        self.setWindowTitle('2048 Remastered!')
        
        # affiche "Comment jouer au 2048 ?"
        self.label = QLabel(self)
        self.label.setFrameStyle(QFrame.StyledPanel | QFrame.Sunken)
        self.label.setAlignment(Qt.AlignCenter)
        font = QFont("Arial", 25, QFont.Bold)
        self.label.setFont(font)
        self.label.setText("Comment jouer au 2048 ?")
        self.label.resize(420,50)
        self.label.move(self.frameGeometry().width()/2-self.label.frameGeometry().width()/2 +250  ,(self.frameGeometry().height()/2)-self.label.frameGeometry().height()/2 -240)

        # affiche une image en arrière plan
        self.setStyleSheet("background-image: url(imageTUTO.png)")

        # bouton Jouer
        self.button1 = QPushButton("Jouer",self)
        font = QFont("Arial", 20,QFont.Bold)
        self.button1.setFont(font)
        self.button1.resize(150,50)
        self.button1.move(self.frameGeometry().width()/2-self.button1.frameGeometry().width()/2 -150,self.frameGeometry().height()/2-self.button1.frameGeometry().height()/2 + 240) #aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa- voir td pour bien centrer
        self.button1.clicked.connect(self.openWindowFromButtonJouer)

        # bouton Fermer
        self.button1 = QPushButton("Fermer",self)
        font = QFont("Arial", 20,QFont.Bold)
        self.button1.setFont(font)
        self.button1.resize(150,50)
        self.button1.move(self.frameGeometry().width()/2-self.button1.frameGeometry().width()/2 -380,self.frameGeometry().height()/2-self.button1.frameGeometry().height()/2 + 240) #aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa- voir td pour bien centrer
        self.button1.clicked.connect(self.close)

        #self.insertImage()
        self.show()

    '''
    def insertImage(self):        
        # Zone de type QLabel
        self.label = QLabel(self)
        
        # Insérer une image
        pixmap2 = QPixmap('fléche.jpg')
        self.label.setPixmap(pixmap2)
        self.move(400,300)
        self.exec_()
    '''

    def openWindowFromButtonJouer(self):
        # code pour lier le fichier Jouer.py au menu
        self.play = Window1()
        self.play.show() 

    def quit(self):
        if dialog.exec_() == QMessageBox.Ok:
            QCoreApplication.instance().quit()

if __name__ == '__main__':
    app = Application(sys.argv)
    ex = App()
    sys.exit(app.exec_())