#! /usr/bin/python3
# -*- coding: utf-8 -*-
#

import sys

from Jouer import *
from Tutoriel import *

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

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        #-------------------------------------------------------------------------------------------------------------------------------------------------------------
        self.setWindowTitle('2048 Remastered!')
        
        #Titre affiché sur le menu
        self.label = QLabel(self)
        self.label.setFrameStyle(QFrame.StyledPanel | QFrame.Sunken)
        self.label.setAlignment(Qt.AlignCenter)
        font = QFont("Arial", 25, QFont.Bold)
        self.label.setFont(font)
        self.label.setText("2048 Remastered")
        self.label.resize(300,50)
        self.label.move(self.frameGeometry().width()/2-self.label.frameGeometry().width()/2 +175 ,(self.frameGeometry().height()/2)-self.label.frameGeometry().height()/2 -180)

        # création de la fenêtre du menu
        self.setFixedSize(1000,600)
        
        # affiche une image en arrière plan
        self.setStyleSheet("background-image: url(image2.jpg)")
          
        # bouton 1 - Jouer
        self.button1 = QPushButton("Jouer",self)
        font = QFont("Arial", 20,QFont.Bold)
        self.button1.setFont(font)
        self.button1.resize(400,50)
        self.button1.move(self.frameGeometry().width()/2-self.button1.frameGeometry().width()/2 ,self.frameGeometry().height()/2-self.button1.frameGeometry().height()/2 + 120) #aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa- voir td pour bien centrer
        self.button1.clicked.connect(self.openWindowFromButtonJouer)
                
        # bouton 2 - Tutoriel
        self.button2 = QPushButton("Tutoriel",self)
        self.button2.setFont(font)
        self.button2.resize(400,50)    
        self.button2.move(self.frameGeometry().width()/2-self.button2.frameGeometry().width()/2 ,self.frameGeometry().height()/2-self.button2.frameGeometry().height()/2 + 180) #aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa- voir td pour bien centrer
        self.button2.clicked.connect(self.openWindowFromButtonTutoriel)

        # bouton 3 - Quitter
        self.button4 = QPushButton("Quitter",self)
        self.button4.setFont(font) 
        self.button4.resize(400,50)   
        self.button4.move(self.frameGeometry().width()/2-self.button4.frameGeometry().width()/2 ,self.frameGeometry().height()/2-self.button4.frameGeometry().height()/2 +240) #aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa- voir td pour bien centrer
        self.button4.clicked.connect(quit)

        # bouton 4 - Mute
        self.button5 = QPushButton("Mute",self)
        font2 = QFont("Arial", 8,QFont.Bold)
        self.button5.setFont(font2) 
        self.button5.resize(50,50)   
        self.button5.move(self.frameGeometry().width()/2-self.button4.frameGeometry().width()/2 +610 ,self.frameGeometry().height()/2-self.button4.frameGeometry().height()/2 -240) #aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa- voir td pour bien centrer
        self.button5.clicked.connect(self.mute)
        
        # bouton 5 - Replay
        self.button5 = QPushButton("Replay",self)
        self.button5.setFont(font2) 
        self.button5.resize(50,50)   
        self.button5.move(self.frameGeometry().width()/2-self.button4.frameGeometry().width()/2 +550 ,self.frameGeometry().height()/2-self.button4.frameGeometry().height()/2 -240) #aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa- voir td pour bien centrer
        self.button5.clicked.connect(self.boutonReplay)                            
        
        self.initSong()
        
        #self.insertButtonPlay()
        #self.insertButtonTutoriel()
        

        self.setCenter()
        #self.showFullScreen()
        self.show()

    #-----------------------------------------------------------------------------------------------------------------------------------------------  
    '''
                                            # Pour des raisons obscures, ces trois définitions fonctionnent chacunes mais séparément
    def insertButtonPlay(self):
        self.button1 = QPushButton("Jouer",self)
        font = QFont("Arial", 20,QFont.Bold)
        self.button1.setFont(font)
        self.button1.resize(400,50)
        self.button1.move(self.frameGeometry().width()/2-self.button1.frameGeometry().width()/2 ,self.frameGeometry().height()/2-self.button1.frameGeometry().height()/2 + 60) #aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa- voir td pour bien centrer
        #self.button1.clicked.connect(self.buttonClicked)
 
        self.show()

    def insertButtonTutoriel(self):
        # bouton 2 - Tutoriel
        self.button2 = QPushButton("Tutoriel",self)
        font = QFont("Arial", 20,QFont.Bold)
        self.button2.setFont(font)
        self.button2.resize(400,50)    
        self.button2.move(self.frameGeometry().width()/2-self.button2.frameGeometry().width()/2 ,self.frameGeometry().height()/2-self.button2.frameGeometry().height()/2 + 120) #aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa- voir td pour bien centrer
        #self.button2.clicked.connect(self.openWindowFromButtonTutoriel())
 
        self.show()
    '''
    def openWindowFromButtonJouer(self):
        #faire le code pour lier le fichier Jouer.py au menu
        self.tuto = Window1()
        self.tuto.show()

    def openWindowFromButtonTutoriel(self):
        #faire le code pour lier le fichier Tutoriel.py au menu
        self.tuto = Window2()
        self.tuto.show()
     
    def quit(self):
        if dialog.exec_() == QMessageBox.Ok:
            QCoreApplication.instance().quit()

    #-----------------------------------------------------------------------------------------------------------------------------------------------  
    def initSong(self):
        self.soundVolume = 3
        self.player = QMediaPlayer()
        content = QMediaContent(QUrl.fromLocalFile("SONG.mp3"))
        self.player.setMedia(content)
        self.player.setVolume(self.soundVolume)
        self.player.positionChanged.connect(self.replay)
        #self.player.setPlaybackRate(3);
        self.player.play()


    def mute(self, event):
        self.player.setMuted(not self.player.isMuted())
    
    # cette def sert pour initSong(self)   
    def replay(self, event):    
        if self.player.position() > 71999:
            self.player.stop()
            self.player.play()


    def boutonReplay(self, event):
        self.player.stop()
        self.player.play()

    
    #-----------------------------------------------------------------------------------------------------------------------------------------------
    def setCenter(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    #-----------------------------------------------------------------------------------------------------------------------------------------------  
if __name__ == '__main__':
    app = Application(sys.argv)
    ex = App()
    sys.exit(app.exec_())
