from PyQt5.QtWidgets import QMessageBox, QSpinBox
from PIL import Image
from PyQt5.QtGui import QTransform
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import QBuffer
from io import BytesIO
import os
import heapq
from collections import defaultdict
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5.QtGui import QImage, QPixmap
import cv2
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QGroupBox, QRadioButton, \
    QHBoxLayout, \
    QApplication, QFileDialog
from scipy.fftpack import dct
import pywt
import numpy as np
import matplotlib.pyplot as plt
import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QFileDialog
from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
from skimage import segmentation, color
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Traitement d'image")
        MainWindow.resize(934, 667)
        MainWindow.setMinimumSize(QtCore.QSize(400, 0))
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_superior = QtWidgets.QFrame(self.centralwidget)
        self.frame_superior.setMinimumSize(QtCore.QSize(0, 35))
        self.frame_superior.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_superior.setStyleSheet("\n"
"QFrame{\n"
"\n"
"\n"
"background-color:#323232;\n"
"\n"
"}\n"
"")
        self.frame_superior.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_superior.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_superior.setObjectName("frame_superior")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_superior)
        self.horizontalLayout_8.setContentsMargins(2, 0, 2, 0)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.bt_menu = QtWidgets.QPushButton(self.frame_superior)
        self.bt_menu.setMinimumSize(QtCore.QSize(200, 0))
        self.bt_menu.setMaximumSize(QtCore.QSize(200, 16777215))
        self.bt_menu.setStyleSheet("QPushButton{\n"
"background-color:#323232;\n"
"font: 87 12pt \"Arial Black\";\n"
"color: rgb(208, 208, 208);\n"
"border-radius:0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"font: 87 12pt \"Arial Black\";\n"
"\n"
"}\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../Documents/projetVisionTraitemetImage/Icons/align-justify.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_menu.setIcon(icon)
        self.bt_menu.setIconSize(QtCore.QSize(32, 32))
        self.bt_menu.setAutoDefault(False)
        self.bt_menu.setDefault(False)
        self.bt_menu.setFlat(False)
        self.bt_menu.setObjectName("bt_menu")
        self.horizontalLayout_8.addWidget(self.bt_menu, 0, QtCore.Qt.AlignLeft)
        self.verticalLayout.addWidget(self.frame_superior)
        self.frame_inferior = QtWidgets.QFrame(self.centralwidget)
        self.frame_inferior.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_inferior.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_inferior.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_inferior.setObjectName("frame_inferior")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_inferior)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(self.frame_inferior)
        self.widget.setObjectName("widget")
        self.widget.setStyleSheet("background-color: rgb(238, 238, 236);")
        self.frame_lateral = QtWidgets.QFrame(self.widget)
        self.frame_lateral.setGeometry(QtCore.QRect(0, 0, 200, 661))
        self.frame_lateral.setMinimumSize(QtCore.QSize(240, 965))
        self.frame_lateral.setMaximumSize(QtCore.QSize(0, 16777215))
        self.frame_lateral.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame_lateral.setAutoFillBackground(False)
        self.frame_lateral.setStyleSheet("\n"
"QFrame{\n"
"background-color: #323232;\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton{\n"
"background-color: #323232;\n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;\n"
"color: rgb(208, 208, 208);\n"
"font: 75 12pt \"Arial Narrow\";\n"
"    \n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: white;\n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;\n"
"color: #323232;\n"
"font: 75 12pt \"Arial Narrow\";\n"
"}")
        self.frame_lateral.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_lateral.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_lateral.setObjectName("frame_lateral")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_lateral)
        self.verticalLayout_2.setContentsMargins(0, -1, 0, 9)
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_lateral)
        self.pushButton_7.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_7.setIconSize(QtCore.QSize(16, 16))
        self.pushButton_7.setObjectName("pushButton_7")

        self.verticalLayout_2.addWidget(self.pushButton_7)
        separator = QtWidgets.QFrame()
        separator.setFrameShape(QtWidgets.QFrame.HLine)
        separator.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.verticalLayout_2.addWidget(separator)
        self.bt_inicio = QtWidgets.QPushButton(self.frame_lateral)
        self.bt_inicio.setMinimumSize(QtCore.QSize(0, 40))
        self.bt_inicio.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.bt_inicio.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.bt_inicio.setStyleSheet("")
        self.bt_inicio.setIconSize(QtCore.QSize(32, 32))
        self.bt_inicio.setCheckable(False)
        self.bt_inicio.setObjectName("bt_inicio")
        self.bt_inicio.clicked.connect(self.imagenegative)
        self.verticalLayout_2.addWidget(self.bt_inicio)
        separator = QtWidgets.QFrame()
        separator.setFrameShape(QtWidgets.QFrame.HLine)
        separator.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.verticalLayout_2.addWidget(separator)
        self.bt_uno = QtWidgets.QPushButton(self.frame_lateral)
        self.bt_uno.setMinimumSize(QtCore.QSize(0, 40))
        self.bt_uno.setToolTipDuration(0)
        self.bt_uno.setStyleSheet("")
        self.bt_uno.clicked.connect(self.open_dialog)
        icon = QtGui.QIcon.fromTheme("rotation")
        self.bt_uno.setIcon(icon)
        self.bt_uno.setIconSize(QtCore.QSize(32, 32))
        self.bt_uno.setObjectName("bt_uno")
        self.verticalLayout_2.addWidget(self.bt_uno)
        separator = QtWidgets.QFrame()
        separator.setFrameShape(QtWidgets.QFrame.HLine)
        separator.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.verticalLayout_2.addWidget(separator)
        self.bt_dos = QtWidgets.QPushButton(self.frame_lateral)
        self.bt_dos.setMinimumSize(QtCore.QSize(0, 40))
        self.bt_dos.setStyleSheet("")
        icon = QtGui.QIcon.fromTheme("rotaion.png")
        self.bt_dos.setIcon(icon)
        self.bt_dos.setIconSize(QtCore.QSize(32, 32))
        self.bt_dos.setObjectName("bt_dos")
        self.bt_dos.clicked.connect(self.Histogramme)

        self.verticalLayout_2.addWidget(self.bt_dos)
        separator = QtWidgets.QFrame()
        separator.setFrameShape(QtWidgets.QFrame.HLine)
        separator.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.verticalLayout_2.addWidget(separator)
        self.bt_tres = QtWidgets.QPushButton(self.frame_lateral)
        self.bt_tres.setMinimumSize(QtCore.QSize(0, 40))
        self.bt_tres.setStyleSheet("")
        self.bt_tres.setIconSize(QtCore.QSize(32, 32))
        self.bt_tres.setObjectName("bt_tres")
        self.bt_tres.clicked.connect(self.EgaliserImage)
        self.verticalLayout_2.addWidget(self.bt_tres)
        separator = QtWidgets.QFrame()
        separator.setFrameShape(QtWidgets.QFrame.HLine)
        separator.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.verticalLayout_2.addWidget(separator)
        self.bt_cuatro = QtWidgets.QPushButton(self.frame_lateral)
        self.bt_cuatro.setMinimumSize(QtCore.QSize(0, 40))
        self.bt_cuatro.setStyleSheet("")
        self.bt_cuatro.setIconSize(QtCore.QSize(32, 32))
        self.bt_cuatro.setObjectName("bt_cuatro")
        self.bt_cuatro.clicked.connect(self.EtirerImage)
        self.verticalLayout_2.addWidget(self.bt_cuatro)
        separator = QtWidgets.QFrame()
        separator.setFrameShape(QtWidgets.QFrame.HLine)
        separator.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.verticalLayout_2.addWidget(separator)
        self.bt_cinco = QtWidgets.QPushButton(self.frame_lateral)
        self.bt_cinco.setMinimumSize(QtCore.QSize(0, 40))
        self.bt_cinco.setStyleSheet("")
        self.bt_cinco.setIconSize(QtCore.QSize(32, 32))
        self.bt_cinco.setObjectName("bt_cinco")

        self.bt_cinco.clicked.connect(self.open_dialogRedmesionner)
        self.verticalLayout_2.addWidget(self.bt_cinco)

        separator = QtWidgets.QFrame()
        separator.setFrameShape(QtWidgets.QFrame.HLine)
        separator.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.verticalLayout_2.addWidget(separator)
        self.pushButton_11 = QtWidgets.QPushButton(self.frame_lateral)
        self.pushButton_11.clicked.connect(self.afficher)
        self.pushButton_11.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_11.setObjectName("pushButton_11")
        self.verticalLayout_2.addWidget(self.pushButton_11)


        separator = QtWidgets.QFrame()
        separator.setFrameShape(QtWidgets.QFrame.HLine)
        separator.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.verticalLayout_2.addWidget(separator)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_lateral)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.afficher1)

        self.verticalLayout_2.addWidget(self.pushButton_2)

        separator = QtWidgets.QFrame()
        separator.setFrameShape(QtWidgets.QFrame.HLine)
        separator.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.verticalLayout_2.addWidget(separator)

        self.pushButton = QtWidgets.QPushButton(self.frame_lateral)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton.setStyleSheet("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.afficher3)
        self.verticalLayout_2.addWidget(self.pushButton)


        separator = QtWidgets.QFrame()
        separator.setFrameShape(QtWidgets.QFrame.HLine)
        separator.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.verticalLayout_2.addWidget(separator)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_lateral)
        self.pushButton_3.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.afficher2)
        self.verticalLayout_2.addWidget(self.pushButton_3)

        separator = QtWidgets.QFrame()
        separator.setFrameShape(QtWidgets.QFrame.HLine)
        separator.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.verticalLayout_2.addWidget(separator)
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_lateral)
        self.pushButton_4.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.DetectionPointInteret)
        self.verticalLayout_2.addWidget(self.pushButton_4)
        separator = QtWidgets.QFrame()
        separator.setFrameShape(QtWidgets.QFrame.HLine)
        separator.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.verticalLayout_2.addWidget(separator)
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_lateral)
        self.pushButton_5.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_5.setObjectName("pushButton_5")
        # self.pushButton_5.clicked.connect(self.afficher6)
        self.pushButton_5.clicked.connect(self.ComressionJPEG)
        self.verticalLayout_2.addWidget(self.pushButton_5)
        separator = QtWidgets.QFrame()
        separator.setFrameShape(QtWidgets.QFrame.HLine)
        separator.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.verticalLayout_2.addWidget(separator)
        self.pushButton_12 = QtWidgets.QPushButton(self.frame_lateral)
        self.pushButton_12.clicked.connect(self.afficher5)
        self.pushButton_12.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_12.setObjectName("pushButton_12")
        self.verticalLayout_2.addWidget(self.pushButton_12)
        separator = QtWidgets.QFrame()
        separator.setFrameShape(QtWidgets.QFrame.HLine)
        separator.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.verticalLayout_2.addWidget(separator)
        self.pushButton_13 = QtWidgets.QPushButton(self.frame_lateral)

        self.pushButton_13.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_13.clicked.connect(self.selectionner)
        self.verticalLayout_2.addWidget(self.pushButton_13)

        self.widget_9 = QtWidgets.QWidget(self.widget)
        self.widget_9.setGeometry(QtCore.QRect(240, 845, 211, 81))
        self.widget_9.setStyleSheet("background-color: #323232;")
        self.widget_9.setObjectName("widget_9")
        self.pushButton_29 = QtWidgets.QPushButton(self.widget_9)
        self.pushButton_29.setGeometry(QtCore.QRect(0, 40, 211, 40))
        self.pushButton_29.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_29.setStyleSheet("color: rgb(208, 208, 208);")
        self.pushButton_29.setObjectName("pushButton_29")
        self.pushButton_29.clicked.connect(self.binarisationOTSU)
        self.pushButton_30 = QtWidgets.QPushButton(self.widget_9)
        self.pushButton_30.setGeometry(QtCore.QRect(0, 0, 211, 40))
        self.pushButton_30.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_30.setStyleSheet("color: rgb(208, 208, 208);")
        self.pushButton_30.setObjectName("pushButton_30")
        self.pushButton_30.clicked.connect(self.open_dialogSeuillage)
        self.widget_7 = QtWidgets.QWidget(self.widget)
        self.widget_7.setGeometry(QtCore.QRect(240, 778, 211, 121))
        self.widget_7.setStyleSheet("background-color: #323232;")
        self.widget_7.setObjectName("widget_7")
        self.pushButton_21 = QtWidgets.QPushButton(self.widget_7)
        self.pushButton_7.clicked.connect(self.open_file_dialog)
        self.pushButton_21.setGeometry(QtCore.QRect(0, 40, 211, 40))
        self.pushButton_21.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_21.setStyleSheet("color: rgb(208, 208, 208);")
        self.pushButton_21.setObjectName("pushButton_21")
        # self.pushButton_21.clicked.connect(self.LZW)
        self.pushButton_22 = QtWidgets.QPushButton(self.widget_7)
        self.pushButton_22.setGeometry(QtCore.QRect(0, 80, 211, 40))
        self.pushButton_22.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_22.setStyleSheet("color: rgb(208, 208, 208);")
        self.pushButton_22.setObjectName("pushButton_22")
        self.pushButton_22.clicked.connect(self.compress_huffman)
        self.pushButton_19 = QtWidgets.QPushButton(self.widget_7)
        self.pushButton_19.setGeometry(QtCore.QRect(0, 0, 211, 40))
        self.pushButton_19.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_19.setStyleSheet("color: rgb(208, 208, 208);")
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_19.clicked.connect(self.compressionOndelette)
        self.widget_8 = QtWidgets.QWidget(self.widget)
        self.widget_8.setGeometry(QtCore.QRect(240, 512, 211, 201))
        self.widget_8.setStyleSheet("background-color: #323232;")
        self.widget_8.setObjectName("widget_8")
        self.pushButton_23 = QtWidgets.QPushButton(self.widget_8)
        self.pushButton_23.setGeometry(QtCore.QRect(0, 40, 211, 40))
        self.pushButton_23.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_23.setStyleSheet("color: rgb(208, 208, 208);")
        self.pushButton_23.setObjectName("pushButton_23")
        self.pushButton_23.clicked.connect(self.Dilatation)
        self.pushButton_24 = QtWidgets.QPushButton(self.widget_8)
        self.pushButton_24.setGeometry(QtCore.QRect(0, 80, 211, 40))
        self.pushButton_24.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_24.setStyleSheet("color: rgb(208, 208, 208);")
        self.pushButton_24.setObjectName("pushButton_24")
        self.pushButton_24.clicked.connect(self.Ouverture)
        self.pushButton_25 = QtWidgets.QPushButton(self.widget_8)
        self.pushButton_25.setGeometry(QtCore.QRect(0, 0, 211, 40))
        self.pushButton_25.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_25.setStyleSheet("color: rgb(208, 208, 208);")
        self.pushButton_25.setObjectName("pushButton_25")
        self.pushButton_25.clicked.connect(self.Erosien)
        self.pushButton_26 = QtWidgets.QPushButton(self.widget_8)
        self.pushButton_26.setGeometry(QtCore.QRect(0, 160, 211, 40))
        self.pushButton_26.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_26.setStyleSheet("color: rgb(208, 208, 208);")
        self.pushButton_26.setObjectName("pushButton_26")
        self.pushButton_26.clicked.connect(self.FiltrageMorphologique)
        self.pushButton_27 = QtWidgets.QPushButton(self.widget_8)
        self.pushButton_27.setGeometry(QtCore.QRect(0, 120, 211, 40))
        self.pushButton_27.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_27.setStyleSheet("color: rgb(208, 208, 208);")
        self.pushButton_27.setObjectName("pushButton_27")
        self.pushButton_27.clicked.connect(self.Fermeture)

        self.widget_5 = QtWidgets.QWidget(self.widget)
        self.widget_5.setGeometry(QtCore.QRect(240, 645, 211, 121))
        self.widget_5.setStyleSheet("background-color: #323232;")
        self.widget_5.setObjectName("widget_5")
        self.pushButton_16 = QtWidgets.QPushButton(self.widget_5)
        self.pushButton_16.setGeometry(QtCore.QRect(0, 40, 211, 40))
        self.pushButton_16.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_16.setStyleSheet("color: rgb(208, 208, 208);")
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_16.clicked.connect(self.PartitionD)
        self.pushButton_17 = QtWidgets.QPushButton(self.widget_5)
        self.pushButton_17.setGeometry(QtCore.QRect(0, 80, 211, 40))
        self.pushButton_17.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_17.setStyleSheet("color: rgb(208, 208, 208);")
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_17.clicked.connect(self.Kmean)
        self.pushButton_18 = QtWidgets.QPushButton(self.widget_5)
        self.pushButton_18.setGeometry(QtCore.QRect(0, 0, 211, 40))
        self.pushButton_18.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_18.setStyleSheet("color: rgb(208, 208, 208);\n"
                                         "")
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_18.clicked.connect(self.CroissanceRegionsD)
        self.widget_2 = QtWidgets.QLabel(self)
        # self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setGeometry(QtCore.QRect(500, 520, 761, 450))
        self.widget_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                    "border-top-left-radius: 20px;\n"
                                    "border-bottom-left-radius: 20px;\n"
                                    "border-top-right-radius: 20px;\n"
                                    "border-bottom-right-radius: 20px;\n"
                                    "")
        self.widget_2.setObjectName("widget_77")

        self.widget_77 = QtWidgets.QLabel(self)
        # self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_77.setGeometry(QtCore.QRect(500, 60, 761, 450))
        self.widget_77.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                     "border-top-left-radius: 20px;\n"
                                     "border-bottom-left-radius: 20px;\n"
                                     "border-top-right-radius: 20px;\n"
                                     "border-bottom-right-radius: 20px;\n"
                                     "")
        self.widget_77.setObjectName("widget_77")
        self.widget_3 = QtWidgets.QWidget(self.widget)

        self.widget_3.setGeometry(QtCore.QRect(240, 447, 211, 121))
        self.widget_3.setStyleSheet("background-color: #323232;")
        self.widget_3.setObjectName("widget_3")
        self.pushButton_9 = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_9.setGeometry(QtCore.QRect(0, 40, 211, 40))
        self.pushButton_9.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_9.setStyleSheet("color: rgb(208, 208, 208);")
        self.pushButton_9.setObjectName("pushButton_9")
        # self.pushButton_9.clicked.connect(self.open)
        self.pushButton_9.clicked.connect(self.open_dialogMoyenneur)
        self.pushButton_10 = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_10.setGeometry(QtCore.QRect(0, 80, 211, 40))
        self.pushButton_10.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_10.setStyleSheet("color: rgb(208, 208, 208);")
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_10.clicked.connect(self.open_dialogMedian)
        self.pushButton_33= QtWidgets.QPushButton(self.widget_3)
        self.pushButton_33.setGeometry(QtCore.QRect(0, 0, 211, 40))
        self.pushButton_33.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_33.setStyleSheet("color: rgb(208, 208, 208);\n"
                                         "")
        self.pushButton_33.setObjectName("pushButton_33")
        self.pushButton_33.clicked.connect(self.open_dialogGaussien)





        self.label1 = QtWidgets.QLabel(self.widget_77)
        self.label1.setGeometry(QtCore.QRect(330, 340, 101, 20))
        self.label1.setStyleSheet("\n"
                                 "font: 75 12pt \"Open Sans\";")
        self.label1.setObjectName("label1")

        self.pushButton_6 = QtWidgets.QPushButton(self.widget_77)
        self.pushButton_6.setGeometry(QtCore.QRect(230, 300, 311, 41))
        self.pushButton_6.setStyleSheet("\n"
                                        "\n"
                                        "QPushButton{\n"
                                        "\n"
                                        "background-color: #323232;\n"
                                        "color: #FFFFFF;\n"
                                        "\n"
                                        "\n"
                                        "\n"
                                        "font: 75 12pt \"Open Sans\";\n"
                                        "\n"
                                        "\n"
                                        "\n"
                                        "    \n"
                                        "}")

        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(self.open_file_dialog)
        self.widget_4 = QtWidgets.QWidget(self.widget)
        self.widget_4.setGeometry(QtCore.QRect(240, 580, 211, 161))
        self.widget_4.setStyleSheet("background-color: #323232;")
        self.widget_4.setObjectName("widget_4")
        self.pushButton_99 = QtWidgets.QPushButton(self.widget_4)
        self.pushButton_99.setGeometry(QtCore.QRect(0, 40, 211, 40))
        self.pushButton_99.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_99.setStyleSheet("color: rgb(208, 208, 208);")
        self.pushButton_99.setObjectName("pushButton_99")
        self.pushButton_99.clicked.connect(self.ContourRobert)
        self.pushButton_14 = QtWidgets.QPushButton(self.widget_4)
        self.pushButton_14.setGeometry(QtCore.QRect(0, 0, 211, 40))
        self.pushButton_14.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_14.setStyleSheet("color: rgb(208, 208, 208);")
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_14.clicked.connect(self.ContourGradient)
        self.pushButton_42 = QtWidgets.QPushButton(self.widget_4)
        self.pushButton_42.setGeometry(QtCore.QRect(0, 80, 211, 40))
        self.pushButton_42.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_42.setStyleSheet("color: rgb(208, 208, 208);")
        self.pushButton_42.setObjectName("pushButton_42")
        self.pushButton_42.clicked.connect(self.ContourSobel)
        self.pushButton_15 = QtWidgets.QPushButton(self.widget_4)
        self.pushButton_15.setGeometry(QtCore.QRect(0, 120, 211, 40))
        self.pushButton_15.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_15.setStyleSheet("color: rgb(208, 208, 208);")
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_15.clicked.connect(self.ContourLaplacien)
        self.pushButton_58= QtWidgets.QPushButton(self.widget)
        self.pushButton_58.setGeometry(QtCore.QRect(1420, 470, 311, 41))
        self.pushButton_58.setStyleSheet("\n"
                                        "\n"
                                        "QPushButton{\n"
                                        "\n"
                                        "background-color: #323232;\n"
                                        "color: #FFFFFF;\n"
                                        "\n"
                                        "\n"
                                        "\n"
                                        "font: 75 12pt \"Open Sans\";\n"
                                        "\n"
                                        "\n"
                                        "\n"
                                        "    \n"
                                        "}")
        self.pushButton_58.setObjectName("pushButton_58")
        self.pushButton_58.clicked.connect(self.annuler)
        self.pushButton_8 = QtWidgets.QPushButton(self.widget)
        self.pushButton_8.setGeometry(QtCore.QRect(1420, 400, 311, 41))
        self.pushButton_8.setStyleSheet("\n"
                                        "\n"
                                        "QPushButton{\n"
                                        "\n"
                                        "background-color: #323232;\n"
                                        "color: #FFFFFF;\n"
                                        "\n"
                                        "\n"
                                        "\n"
                                        "font: 75 12pt \"Open Sans\";\n"
                                        "\n"
                                        "\n"
                                        "\n"
                                        "    \n"
                                        "}")
        self.pushButton_8.clicked.connect(self.save_image)
        self.horizontalLayout.addWidget(self.widget)
        self.verticalLayout.addWidget(self.frame_inferior)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.widget_3.setVisible(False)
        self.widget_5.setVisible(False)
        self.widget_7.setVisible(False)
        self.widget_8.setVisible(False)
        self.widget_9.setVisible(False)
        self.widget_4.setVisible(False)
        test=0

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.bt_menu.setText(_translate("MainWindow", "    Traitement d'image "))
        self.pushButton_7.setText(_translate("MainWindow", "Telecharger Image"))
        self.label1.setText(_translate("MainWindow", "or drop a file"))
        self.bt_inicio.setText(_translate("MainWindow", "Image Negative"))
        self.bt_uno.setText(_translate("MainWindow", "Rotation"))
        self.bt_dos.setText(_translate("MainWindow", "Histogramme"))
        self.bt_tres.setText(_translate("MainWindow", "Egalisation"))
        self.bt_cuatro.setText(_translate("MainWindow", "Etirement"))
        self.bt_cinco.setText(_translate("MainWindow", "Redimentionner"))
        self.pushButton_12.setText(_translate("MainWindow", "Binarisation"))
        self.pushButton_13.setText(_translate("MainWindow", "Selectionner"))
        self.pushButton_11.setText(_translate("MainWindow", "Filtrage"))
        self.pushButton_21.setText(_translate("MainWindow", "LZW"))
        self.pushButton_19.setText(_translate("MainWindow", "Ondelette"))
        self.pushButton_22.setText(_translate("MainWindow", "Huffman"))
        self.pushButton_2.setText(_translate("MainWindow", " Morphologie"))
        self.pushButton_16.setText(_translate("MainWindow", "PartitionRegionD"))
        self.pushButton_17.setText(_translate("MainWindow", "K-means"))
        self.pushButton_18.setText(_translate("MainWindow", "CroissanceRegionD"))
        self.pushButton_23.setText(_translate("MainWindow", "Dilatation"))
        self.pushButton_24.setText(_translate("MainWindow", "Ouverture"))
        self.pushButton_25.setText(_translate("MainWindow", "Erosien"))
        self.pushButton_26.setText(_translate("MainWindow", "FiltrageMorphologique"))
        self.pushButton_27.setText(_translate("MainWindow", "Fermeture"))
        self.pushButton_9.setText(_translate("MainWindow", "Moyenneur"))
        self.pushButton_10.setText(_translate("MainWindow", "Median"))
        self.pushButton_33.setText(_translate("MainWindow", "Gaussien"))
        self.pushButton.setText(_translate("MainWindow", "Extraction Des Conteur"))
        self.pushButton_42.setText(_translate("MainWindow", "Sobel"))
        self.pushButton_14.setText(_translate("MainWindow", "Gradient"))
        self.pushButton_99.setText(_translate("MainWindow", "Robert"))
        self.pushButton_15.setText(_translate("MainWindow", "Laplacien"))

        self.pushButton_3.setText(_translate("MainWindow", "Segmentation"))

        self.pushButton_4.setText(_translate("MainWindow", "Detection Des point D\'interet"))
        self.pushButton_5.setText(_translate("MainWindow", "Compression"))
        path=""
        self.pushButton_29.setText(_translate("MainWindow", "Otsu"))
        self.pushButton_30.setText(_translate("MainWindow", "SeuillageManuel"))
        self.pushButton_6.setText(_translate("MainWindow", "Ouvrire Une Image"))
        self.pushButton_58.setText(_translate("MainWindow", "Annuller"))
        self.pushButton_8.setText(_translate("MainWindow", "Enregistrer"))
class MyLabel(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasImage:
            file_name = event.mimeData().urls()[0].toLocalFile()
            pixmap = QtGui.QPixmap(file_name)
            self.setPixmap(pixmap.scaled(self.size(), QtCore.Qt.KeepAspectRatio))

            # Set the pixmap of widget 2 with the dropped image
            widget_2.setPixmap(pixmap.scaled(widget_2.size(), QtCore.Qt.KeepAspectRatio))
            event.accept()
        else:
            event.ignore()

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):

        super().__init__(parent)
        self.setupUi(self)
        self.drag_image()



    def afficher(self):
        if  self.widget_3.isVisible():
         self.widget_3.setVisible(False)

        else:
            self.widget_3.setVisible(True)
            self.widget_5.setVisible(False)
            self.widget_7.setVisible(False)
            self.widget_8.setVisible(False)
            self.widget_9.setVisible(False)

    def afficher1(self):
        if self.widget_8.isVisible():
            self.widget_8.setVisible(False)

        else:
            self.widget_8.setVisible(True)
            self.widget_3.setVisible(False)
            self.widget_5.setVisible(False)
            self.widget_7.setVisible(False)
            self.widget_9.setVisible(False)
            self.widget_4.setVisible(False)
    def afficher2(self):
        if self.widget_5.isVisible():
            self.widget_5.setVisible(False)

        else:
            self.widget_5.setVisible(True)
            self.widget_3.setVisible(False)

            self.widget_7.setVisible(False)
            self.widget_8.setVisible(False)
            self.widget_9.setVisible(False)
            self.widget_4.setVisible(False)

    def afficher3(self):
        if self.widget_4.isVisible():
            self.widget_4.setVisible(False)

        else:
            self.widget_4.setVisible(True)
            self.widget_3.setVisible(False)
            self.widget_5.setVisible(False)
            self.widget_7.setVisible(False)
            self.widget_8.setVisible(False)

            self.widget_9.setVisible(False)

    def afficher4(self):
        if self.widget_8.isVisible():
            self.widget_8.setVisible(False)

        else:
            self.widget_8.setVisible(True)
            self.widget_3.setVisible(False)
            self.widget_5.setVisible(False)
            self.widget_7.setVisible(False)
            self.widget_4.setVisible(False)
            self.widget_9.setVisible(False)

    def afficher5(self):
        if self.widget_9.isVisible():
            self.widget_9.setVisible(False)

        else:
            self.widget_9.setVisible(True)
            self.widget_3.setVisible(False)
            self.widget_5.setVisible(False)
            self.widget_7.setVisible(False)
            self.widget_8.setVisible(False)
            self.widget_4.setVisible(False)

    def afficher6(self):
        if self.widget_7.isVisible():
            self.widget_7.setVisible(False)

        else:
            self.widget_7.setVisible(True)
            self.widget_3.setVisible(False)
            self.widget_5.setVisible(False)
            self.widget_9.setVisible(False)
            self.widget_8.setVisible(False)
            self.widget_4.setVisible(False)

    def open_file_dialog(self):
        # Ouvrir un dialogue pour sélectionner un fichier image
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getOpenFileName(None, "Sélectionner une image", "",
                                                   "Images (*.png *.xpm *.jpg *.bmp *.jpeg);;Tous les fichiers (*)",
                                                   options=options)
        if file_name:
            # Charger l'image sélectionnée dans le label
            print(file_name)
            self.path=file_name
            img = cv2.imread(file_name)
            if len(img.shape) == 2:
                    print("Image is grayscale")
            else:
                    print("Image is RGB")

            pixmap = QtGui.QPixmap(file_name)
            pixorigin= QtGui.QPixmap(file_name)
            # Set the pixmap of both the first and the second QLabel widgets
            # self.label.setPixmap(pixmap.scaled(self.label.size(), QtCore.Qt.KeepAspectRatio))
            self.widget_77.setPixmap(pixmap.scaled(self.widget_77.size(), QtCore.Qt.KeepAspectRatio))
            self.widget_2.setPixmap(pixmap.scaled(self.widget_2.size(), QtCore.Qt.KeepAspectRatio))
            self.label1.hide()
            self.pushButton_6.hide()

            self.imagenegative(pixmap)
            self.EgaliserImage(pixmap)
            self.EtirerImage(pixmap)
            self.FiltreGaussien(pixmap)
            self.FiltreMoyenneur(pixmap)
            self.FiltreMedian(pixmap)
            self.ContourGradient(pixmap)
            self.ContourSobel(pixmap)
            self.ContourRobert(pixmap)
            self.ContourLaplacien(pixmap)
            self.Erosien(pixmap)
            self.Dilatation(pixmap)
            self.Ouverture(pixmap)
            self.Fermeture(pixmap)
            self.FiltrageMorphologique(pixmap)
            self.Kmean(pixmap)
            self.CroissanceRegionsD(pixmap)
            self.DetectionPointInteret(pixmap)
            self.Ondelette(pixmap)
            self.Redimentionner(pixmap)
            self.PartitionD(pixmap)
            self.Histogramme(pixmap)
            self.selectionner(pixmap)
            # self.histogramme(pixmap)

    def ContourGradient(self):
        image = self.widget_2.pixmap().toImage()
        buffer = QtCore.QBuffer()
        buffer.open(QtCore.QIODevice.ReadWrite)
        image.save(buffer, "PNG")
        img_str = buffer.data()
        nparr = np.frombuffer(img_str, np.uint8)
        img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        if img_np is None:
            raise ValueError("Failed to decode image")
        print("Sbbbbbbbbb:")
        img_np = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
        img_format = QtGui.QImage.Format_RGB888

        n = 5
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (n, n))
        ##############Gradiant#######################################
        gradient = cv2.morphologyEx(img_np, cv2.MORPH_GRADIENT, kernel)
        height, width, channel = gradient.shape

        q_img = QtGui.QImage(gradient.data, width, height, width * channel, img_format)
        pixmap = QtGui.QPixmap.fromImage(q_img.convertToFormat(QtGui.QImage.Format_RGB888))
        self.widget_2.setPixmap(pixmap.scaled(self.widget_2.size(), QtCore.Qt.KeepAspectRatio))

    def Erosien(self):
        image = self.widget_2.pixmap().toImage()
        buffer = QtCore.QBuffer()
        buffer.open(QtCore.QIODevice.ReadWrite)
        image.save(buffer, "PNG")
        img_str = buffer.data()
        nparr = np.frombuffer(img_str, np.uint8)
        img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        if img_np is None:
            raise ValueError("Failed to decode image")
        print("Sbbbbbbbbb:")
        img_np = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
        img_format = QtGui.QImage.Format_RGB888

        n = 5
        k = cv2.getStructuringElement(cv2.MORPH_RECT, (n, n))
        i = 1
        output = cv2.erode(img_np, k, iterations=i)
        height, width, channel = output.shape

        q_img = QtGui.QImage(output.data, width, height, width * channel, img_format)
        pixmap = QtGui.QPixmap.fromImage(q_img.convertToFormat(QtGui.QImage.Format_RGB888))
        self.widget_2.setPixmap(pixmap.scaled(self.widget_2.size(), QtCore.Qt.KeepAspectRatio))

    def Dilatation(self):
        image = self.widget_2.pixmap().toImage()
        buffer = QtCore.QBuffer()
        buffer.open(QtCore.QIODevice.ReadWrite)
        image.save(buffer, "PNG")
        img_str = buffer.data()
        nparr = np.frombuffer(img_str, np.uint8)
        img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        if img_np is None:
            raise ValueError("Failed to decode image")
        print("Sbbbbbbbbb:")
        img_np = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
        img_format = QtGui.QImage.Format_RGB888

        n = 5
        k = cv2.getStructuringElement(cv2.MORPH_RECT, (n, n))
        i = 1
        output = cv2.dilate(img_np, k, iterations=i)
        height, width, channel = output.shape

        q_img = QtGui.QImage(output.data, width, height, width * channel, img_format)
        pixmap = QtGui.QPixmap.fromImage(q_img.convertToFormat(QtGui.QImage.Format_RGB888))
        self.widget_2.setPixmap(pixmap.scaled(self.widget_2.size(), QtCore.Qt.KeepAspectRatio))


    def Ouverture(self):
        image = self.widget_2.pixmap().toImage()
        buffer = QtCore.QBuffer()
        buffer.open(QtCore.QIODevice.ReadWrite)
        image.save(buffer, "PNG")
        img_str = buffer.data()
        nparr = np.frombuffer(img_str, np.uint8)
        img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        if img_np is None:
            raise ValueError("Failed to decode image")
        print("Sbbbbbbbbb:")
        img_np = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
        img_format = QtGui.QImage.Format_RGB888

        n = 5
        k = cv2.getStructuringElement(cv2.MORPH_RECT, (n, n))

        output = cv2.morphologyEx(img_np, cv2.MORPH_OPEN, k)
        height, width, channel = output.shape

        q_img = QtGui.QImage(output.data, width, height, width * channel, img_format)
        pixmap = QtGui.QPixmap.fromImage(q_img.convertToFormat(QtGui.QImage.Format_RGB888))
        self.widget_2.setPixmap(pixmap.scaled(self.widget_2.size(), QtCore.Qt.KeepAspectRatio))
    def Fermeture(self):
        image = self.widget_2.pixmap().toImage()
        buffer = QtCore.QBuffer()
        buffer.open(QtCore.QIODevice.ReadWrite)
        image.save(buffer, "PNG")
        img_str = buffer.data()
        nparr = np.frombuffer(img_str, np.uint8)
        img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        if img_np is None:
            raise ValueError("Failed to decode image")
        print("Sbbbbbbbbb:")
        img_np = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
        img_format = QtGui.QImage.Format_RGB888

        n = 5
        k = cv2.getStructuringElement(cv2.MORPH_RECT, (n, n))

        output = cv2.morphologyEx(img_np, cv2.MORPH_CLOSE, k)
        height, width, channel = output.shape

        q_img = QtGui.QImage(output.data, width, height, width * channel, img_format)
        pixmap = QtGui.QPixmap.fromImage(q_img.convertToFormat(QtGui.QImage.Format_RGB888))
        self.widget_2.setPixmap(pixmap.scaled(self.widget_2.size(), QtCore.Qt.KeepAspectRatio))
    def DetectionPointInteret(self):
        image = self.widget_2.pixmap().toImage()
        buffer = QtCore.QBuffer()
        buffer.open(QtCore.QIODevice.ReadWrite)
        image.save(buffer, "PNG")
        img_str = buffer.data()
        nparr = np.frombuffer(img_str, np.uint8)
        img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        if img_np is None:
            raise ValueError("Failed to decode image")
        print("Sbbbbbbbbb:")
        img_np = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
        img_format = QtGui.QImage.Format_RGB888

        orb = cv2.ORB_create()
        kp = orb.detect(img_np, None)

        # Marking the keypoint on the image using circles
        img = cv2.drawKeypoints(img_np, kp, img_np)
        height, width, channel = img.shape

        q_img = QtGui.QImage(img.data, width, height, width * channel, img_format)
        pixmap = QtGui.QPixmap.fromImage(q_img.convertToFormat(QtGui.QImage.Format_RGB888))
        self.widget_2.setPixmap(pixmap.scaled(self.widget_2.size(), QtCore.Qt.KeepAspectRatio))

    # def Ondelette(self):
    #     image = self.widget_2.pixmap().toImage()
    #     buffer = QtCore.QBuffer()
    #     buffer.open(QtCore.QIODevice.ReadWrite)
    #     image.save(buffer, "PNG")
    #     img_str = buffer.data()
    #     nparr = np.frombuffer(img_str, np.uint8)
    #     img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    #
    #     if img_np is None:
    #         raise ValueError("Failed to decode image")
    #     print("Sbbbbbbbbb:")
    #     img_np = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
    #     img_format = QtGui.QImage.Format_RGB888
    #
    #     coeffs = pywt.dwt2(img_np, 'haar')
    #
    #     # Quantifier les coefficients de la transformée
    #     coeffs_quant = [pywt.threshold(i, value=20, mode='soft') for i in coeffs]
    #
    #     # Reconstruire l'image à partir des coefficients quantifiés
    #     image_compress = pywt.idwt2(coeffs_quant, 'haar')
    #
    #     # Convertir le tableau numpy en une image PIL et l'afficher
    #     image_compress = Image.fromarray(np.uint8(image_compress))
    #     width, height = image_compress.size
    #
    #     q_img = QtGui.QImage(image_compress.data, width, height, width, img_format)
    #     pixmap = QtGui.QPixmap.fromImage(q_img.convertToFormat(QtGui.QImage.Format_RGB888))
    #     self.widget_2.setPixmap(pixmap.scaled(self.widget_2.size(), QtCore.Qt.KeepAspectRatio))

    def FiltrageMorphologique(self):
        image = self.widget_2.pixmap().toImage()
        buffer = QtCore.QBuffer()
        buffer.open(QtCore.QIODevice.ReadWrite)
        image.save(buffer, "PNG")
        img_str = buffer.data()
        nparr = np.frombuffer(img_str, np.uint8)
        img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        if img_np is None:
            raise ValueError("Failed to decode image")
        print("Sbbbbbbbbb:")
        img_np = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
        img_format = QtGui.QImage.Format_RGB888

        n = 5
        k = cv2.getStructuringElement(cv2.MORPH_RECT, (n, n))

        output = cv2.morphologyEx(img_np, cv2.MORPH_GRADIENT, k)
        height, width, channel = output.shape

        q_img = QtGui.QImage(output.data, width, height, width * channel, img_format)
        pixmap = QtGui.QPixmap.fromImage(q_img.convertToFormat(QtGui.QImage.Format_RGB888))
        self.widget_2.setPixmap(pixmap.scaled(self.widget_2.size(), QtCore.Qt.KeepAspectRatio))

    def Kmean(self):
        image = self.widget_2.pixmap().toImage()
        buffer = QtCore.QBuffer()
        buffer.open(QtCore.QIODevice.ReadWrite)
        image.save(buffer, "PNG")
        img_str = buffer.data()
        nparr = np.frombuffer(img_str, np.uint8)
        img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        if img_np is None:
            raise ValueError("Failed to decode image")
        print("Sbbbbbbbbb:")
        img_np = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
        img_format = QtGui.QImage.Format_RGB888

        img = cv2.resize(img_np, (300, 300))

        # Appliquer la segmentation par k-means
        pixel_vals = img.reshape((-1, 3))
        pixel_vals = np.float32(pixel_vals)

        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 200, 0.85)
        k = 3
        _, labels, centers = cv2.kmeans(pixel_vals, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

        # Réorganiser les pixels en fonction des clusters
        centers = np.uint8(centers)
        segmented_data = centers[labels.flatten()]
        segmented_image = segmented_data.reshape(img.shape)
        height, width, channel = segmented_image.shape

        q_img = QtGui.QImage(segmented_image.data, width, height, width * channel, img_format)
        pixmap = QtGui.QPixmap.fromImage(q_img.convertToFormat(QtGui.QImage.Format_RGB888))
        self.widget_2.setPixmap(pixmap.scaled(self.widget_2.size(), QtCore.Qt.KeepAspectRatio))


    def ContourSobel(self):
        image = self.widget_2.pixmap().toImage()
        buffer = QtCore.QBuffer()
        buffer.open(QtCore.QIODevice.ReadWrite)
        image.save(buffer, "PNG")
        img_str = buffer.data()
        nparr = np.frombuffer(img_str, np.uint8)
        img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        if img_np is None:
            raise ValueError("Failed to decode image")
        print("Sbbbbbbbbb:")
        img_np = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
        img_format = QtGui.QImage.Format_RGB888

        k = 3
        # noyau du filtre gaussien qui sera utilisé pour lisser l'image.
        img = cv2.GaussianBlur(img_np, (k, k), sigmaX=0, sigmaY=0)
        edge_sobelx = cv2.Sobel(src=img_np, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=k)
        edge_sobely = cv2.Sobel(src=img_np, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=k)
        cvx = cv2.convertScaleAbs(edge_sobelx)
        cvy = cv2.convertScaleAbs(edge_sobely)
        sobel = cv2.addWeighted(cvx, 0.5, cvy, 0.5, 0)
        height, width, channel = sobel.shape

        q_img = QtGui.QImage(sobel.data, width, height, width * channel, img_format)
        pixmap = QtGui.QPixmap.fromImage(q_img.convertToFormat(QtGui.QImage.Format_RGB888))
        self.widget_2.setPixmap(pixmap.scaled(self.widget_2.size(), QtCore.Qt.KeepAspectRatio))

    def ContourLaplacien(self):
        image = self.widget_2.pixmap().toImage()
        buffer = QtCore.QBuffer()
        buffer.open(QtCore.QIODevice.ReadWrite)
        image.save(buffer, "PNG")
        img_str = buffer.data()
        nparr = np.frombuffer(img_str, np.uint8)
        img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        if img_np is None:
            raise ValueError("Failed to decode image")
        print("Sbbbbbbbbb:")
        img_np = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
        img_format = QtGui.QImage.Format_RGB888

        laplacian = cv2.Laplacian(img_np, cv2.CV_64F)
        laplacian = cv2.convertScaleAbs(laplacian)
        height, width, channel = laplacian.shape

        q_img = QtGui.QImage(laplacian.data, width, height, width * channel, img_format)
        pixmap = QtGui.QPixmap.fromImage(q_img.convertToFormat(QtGui.QImage.Format_RGB888))
        self.widget_2.setPixmap(pixmap.scaled(self.widget_2.size(), QtCore.Qt.KeepAspectRatio))

    def ContourRobert(self):
        image = self.widget_2.pixmap().toImage()
        buffer = QtCore.QBuffer()
        buffer.open(QtCore.QIODevice.ReadWrite)
        image.save(buffer, "PNG")
        img_str = buffer.data()
        nparr = np.frombuffer(img_str, np.uint8)
        img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        if img_np is None:
            raise ValueError("Failed to decode image")
        print("Sbbbbbbbbb:")
        img_np = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
        img_format = QtGui.QImage.Format_RGB888
        img = img_np.astype('float32') / 255.0
        kernel_x = np.array([[1, 0], [0, -1]], dtype=np.float32)
        kernel_y = np.array([[0, 1], [-1, 0]], dtype=np.float32)
        # Application du filtre de Roberts en x et y
        dx = cv2.filter2D(img, -1, kernel_x).astype(np.float32)
        dy = cv2.filter2D(img, -1, kernel_y).astype(np.float32)
        # Calcul de la magnitude
        roberts = cv2.magnitude(dx, dy)
        roberts = (roberts * 255).astype(np.uint8)
        height, width, channel = roberts.shape

        q_img = QtGui.QImage(roberts.data, width, height, width * channel, img_format)
        pixmap = QtGui.QPixmap.fromImage(q_img.convertToFormat(QtGui.QImage.Format_RGB888))
        self.widget_2.setPixmap(pixmap.scaled(self.widget_2.size(), QtCore.Qt.KeepAspectRatio))

    def FiltreGaussien(self,ecart):
        image = self.widget_2.pixmap().toImage()
        buffer = QtCore.QBuffer()
        buffer.open(QtCore.QIODevice.ReadWrite)
        image.save(buffer, "PNG")
        img_str = buffer.data()
        nparr = np.frombuffer(img_str, np.uint8)
        img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        if img_np is None:
            raise ValueError("Failed to decode image")
        print("Sbbbbbbbbb:")
        img_np = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
        img_format = QtGui.QImage.Format_RGB888


        n = 15
        img_gaussian = cv2.GaussianBlur(img_np, (n, n), ecart)
        height, width, channel = img_gaussian.shape

        q_img = QtGui.QImage(img_gaussian.data, width, height, width * channel, img_format)
        pixmap = QtGui.QPixmap.fromImage(q_img.convertToFormat(QtGui.QImage.Format_RGB888))
        self.widget_2.setPixmap(pixmap.scaled(self.widget_2.size(), QtCore.Qt.KeepAspectRatio))

    def FiltreMoyenneur(self,taille):
        image = self.widget_2.pixmap().toImage()
        buffer = QtCore.QBuffer()
        buffer.open(QtCore.QIODevice.ReadWrite)
        image.save(buffer, "PNG")
        img_str = buffer.data()
        nparr = np.frombuffer(img_str, np.uint8)
        img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        if img_np is None:
            raise ValueError("Failed to decode image")
        print("Sbbbbbbbbb:")
        img_np = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
        img_format = QtGui.QImage.Format_RGB888
        img_mean = cv2.blur(img_np, (taille, taille))
        height, width, channel = img_mean.shape

        q_img = QtGui.QImage(img_mean.data, width, height, width * channel, img_format)
        pixmap = QtGui.QPixmap.fromImage(q_img.convertToFormat(QtGui.QImage.Format_RGB888))
        self.widget_2.setPixmap(pixmap.scaled(self.widget_2.size(), QtCore.Qt.KeepAspectRatio))

    def FiltreMedian(self,taille):
        image = self.widget_2.pixmap().toImage()
        buffer = QtCore.QBuffer()
        buffer.open(QtCore.QIODevice.ReadWrite)
        image.save(buffer, "PNG")
        img_str = buffer.data()
        nparr = np.frombuffer(img_str, np.uint8)
        img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        if img_np is None:
            raise ValueError("Failed to decode image")
        print("Sbbbbbbbbb:")
        img_np = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
        img_format = QtGui.QImage.Format_RGB888
        img_median = cv2.medianBlur(img_np, taille)
        height, width, channel = img_median.shape

        q_img = QtGui.QImage(img_median.data, width, height, width * channel, img_format)
        pixmap = QtGui.QPixmap.fromImage(q_img.convertToFormat(QtGui.QImage.Format_RGB888))
        self.widget_2.setPixmap(pixmap.scaled(self.widget_2.size(), QtCore.Qt.KeepAspectRatio))

    # def Histogramme(self):
    #         # Convertir le pixmap en une image numpy
    #         image = self.widget_2.pixmap().toImage()
    #         buffer = QtCore.QBuffer()
    #         buffer.open(QtCore.QIODevice.ReadWrite)
    #         image.save(buffer, "PNG")
    #         img_str = buffer.data()
    #         nparr = np.frombuffer(img_str, np.uint8)
    #         img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    #
    #         if img_np is None:
    #                 raise ValueError("Failed to decode image")
    #         print("Sbbbbbbbbb:")
    #         img_np = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
    #         img_format = QtGui.QImage.Format_RGB888
    #         # Calculer l'histogramme de l'image
    #         hist, bins = np.histogram(img_np.flatten(), 256, [0, 256])
    #         cdf = hist.cumsum()
    #         cdf_normalized = cdf * float(hist.max()) / cdf.max()
    #
    #         # Tracer l'histogramme
    #         plt.plot(cdf_normalized, color='b')
    #         plt.hist(img_np.flatten(), 256, [0, 256], color='r')
    #         plt.xlim([0, 256])
    #         plt.legend(('Fonction de distribution cumulative (CDF)', 'Histogramme'), loc='upper left')
    #         plt.xlabel('Intensité de pixel')
    #         plt.ylabel('Nombre de pixels')
    #         plt.title('Histogramme de l\'image')
    #
    #         # Convertir le graphe en image
    #         plt.tight_layout()
    #         buf = io.BytesIO()
    #         plt.savefig(buf, format='png')
    #         buf.seek(0)
    #         img_bytes = np.asarray(bytearray(buf.read()), dtype=np.uint8)
    #         buf.close()
    #         img = cv2.imdecode(img_bytes, cv2.IMREAD_COLOR)
    #
    #         # Convertir l'image en pixmap et l'afficher dans le widget_2
    #         height, width, channel = img.shape
    #         img_format = QtGui.QImage.Format_RGB888
    #         q_img = QtGui.QImage(img.data, width, height, width * channel, img_format)
    #         pixmap = QtGui.QPixmap.fromImage(q_img.convertToFormat(QtGui.QImage.Format_RGB888))
    #         self.widget_2.setPixmap(pixmap.scaled(self.widget_2.size(), QtCore.Qt.KeepAspectRatio))

    def Histogramme(self):
            # Convertir le pixmap en une image numpy
            image = self.widget_2.pixmap().toImage()
            buffer = QtCore.QBuffer()
            buffer.open(QBuffer.ReadWrite)
            image.save(buffer, "PNG")
            img_str = buffer.data()
            nparr = np.frombuffer(img_str, np.uint8)
            img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
            print("Histogramme")
            if img_np is None:
                    raise ValueError("Failed to decode image")

            img_np = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
            img_format = QImage.Format_RGB888
            # Calculer l'histogramme de l'image
            # hist, bins = np.histogram(img_np.flatten(), 256, [0, 256])
            # cdf = hist.cumsum()
            # cdf_normalized = cdf * float(hist.max()) / cdf.max()
            #
            # # Tracer l'histogramme
            # # plt.plot(cdf_normalized, color='b')
            # plt.hist(img_np.flatten(), 256, [0, 256], color='r')
            # plt.xlim([0, 256])
            channels = cv2.split(img_np)

            # Définir les paramètres de l'histogramme
            histSize = 256
            histRange = (0, 256)

            # Calculer l'histogramme pour chaque canal de couleur
            hist_r = cv2.calcHist([channels[0]], [0], None, [histSize], histRange)
            hist_g = cv2.calcHist([channels[1]], [0], None, [histSize], histRange)
            hist_b = cv2.calcHist([channels[2]], [0], None, [histSize], histRange)

            # Afficher l'histogramme
            plt.plot(hist_r, color='r')
            plt.plot(hist_g, color='g')
            plt.plot(hist_b, color='b')
            plt.xlim([0, 256])

            # plt.legend(('Fonction de distribution cumulative (CDF)', 'Histogramme'), loc='upper left')
            plt.xlabel('Intensité de pixel')
            plt.ylabel('Nombre de pixels')
            plt.title('Histogramme de l\'image')

            # Convertir le graphe en image
            plt.tight_layout()
            buf = BytesIO()
            plt.savefig(buf, format='png')
            buf.seek(0)
            img_bytes = np.asarray(bytearray(buf.read()), dtype=np.uint8)
            buf.close()
            img = cv2.imdecode(img_bytes, cv2.IMREAD_COLOR)
            plt.show()
            # Convertir l'image en pixmap et l'afficher dans le label
            height, width, channel = img.shape
            img_format = QImage.Format_RGB888
            q_img = QImage(img.data, width, height, width * channel, img_format)
            pixmap = QPixmap.fromImage(q_img.convertToFormat(QImage.Format_RGB888))
            self.widget_2.setPixmap(pixmap.scaled(self.widget_2.size(), QtCore.Qt.KeepAspectRatio))
    def EgaliserImage(self):
        # Convertir le pixmap en une image numpy
        image = self.widget_2.pixmap().toImage()
        buffer = QtCore.QBuffer()
        buffer.open(QtCore.QIODevice.ReadWrite)
        image.save(buffer, "PNG")
        img_str = buffer.data()
        nparr = np.frombuffer(img_str, np.uint8)
        img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        if img_np is None:
                raise ValueError("Failed to decode image")
        print("Sbbbbbbbbb:")
        img_np = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
        img_format = QtGui.QImage.Format_RGB888

        # Égaliser l'histogramme
        r, g, b = cv2.split(img_np)
        # Egaliser l'histogramme
        r = cv2.equalizeHist(r)
        g = cv2.equalizeHist(g)
        b = cv2.equalizeHist(b)
        img_eq = cv2.merge((r, g, b))

        # Convertir l'image égalisée en un pixmap et l'afficher dans le widget_2
        height, width, channel = img_eq.shape
        q_img = QtGui.QImage(img_eq.data, width, height, width * channel, img_format)
        pixmap = QtGui.QPixmap.fromImage(q_img.convertToFormat(QtGui.QImage.Format_RGB888))
        self.widget_2.setPixmap(pixmap.scaled(self.widget_2.size(), QtCore.Qt.KeepAspectRatio))

    def EtirerImage(self):
        # Convertir le pixmap en une image numpy
        image = self.widget_2.pixmap().toImage()
        buffer = QtCore.QBuffer()
        buffer.open(QtCore.QIODevice.ReadWrite)
        image.save(buffer, "PNG")
        img_str = buffer.data()
        nparr = np.frombuffer(img_str, np.uint8)
        img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        if img_np is None:
                raise ValueError("Failed to decode image")
        print("Sbbbbbbbbb:")
        img_np = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
        img_format = QtGui.QImage.Format_RGB888

        # Étirer l'histogramme
        r, g, b = cv2.split(img_np)
        # Egaliser l'histogramme
        r = cv2.normalize(r, None, 0, 255, cv2.NORM_MINMAX)
        g = cv2.normalize(g, None, 0, 255, cv2.NORM_MINMAX)
        b = cv2.normalize(b, None, 0, 255, cv2.NORM_MINMAX)
        img_stretched = cv2.merge((r, g, b))
        # Convertir l'image égalisée en un pixmap et l'afficher dans le widget_2
        height, width, channel = img_stretched.shape
        q_img = QtGui.QImage(img_stretched.data, width, height, width * channel, img_format)
        pixmap = QtGui.QPixmap.fromImage(q_img.convertToFormat(QtGui.QImage.Format_RGB888))
        self.widget_2.setPixmap(pixmap.scaled(self.widget_2.size(), QtCore.Qt.KeepAspectRatio))

    def imagenegative(self):
        # Get the current pixmap from the widget_2
        pixmap = self.widget_2.pixmap()
        # If there is no pixmap, return
        if pixmap is None:
            return
        # Convert the pixmap to a QImage
        image = pixmap.toImage()
        # Invert the pixels of the image
        image.invertPixels()
        # Convert the QImage back to a QPixmap and set it on the widget_2
        inverted_pixmap = QtGui.QPixmap.fromImage(image)
        self.widget_2.setPixmap(inverted_pixmap)

    def rotate_image1(self, pixmap, angle):
        # Convert the pixmap to a QImage
        image = pixmap.toImage()

        # Rotate the image by the specified angle
        transform = QTransform().rotate(angle)
        rotated_image = image.transformed(transform)

        # Convert the rotated image back to a pixmap
        rotated_pixmap = QPixmap.fromImage(rotated_image)

        return rotated_pixmap

    def rotate_image(self, angle):
        # Exemple d'angle de rotation
        current_pixmap = self.widget_2.pixmap()
        if current_pixmap is not None:
            rotated_pixmap = self.rotate_image1(current_pixmap, angle)
            self.widget_2.setPixmap(rotated_pixmap)

    def open_dialog(self):
        msg = QMessageBox()
        msg.setWindowTitle("Angle de Rotation")
        msg.setText("Choisir l'angle de rotation")

        # create a spin box widget
        spin_box = QSpinBox()
        spin_box.setRange(0, 360)
        spin_box.setValue(0)

        # add the spin box widget to the message box
        layout = msg.layout()
        layout.addWidget(spin_box)
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        # execute the message box and get the selected button
        button = msg.exec_()

        # get the selected angle from the spin box
        angle = spin_box.value()

        # handle the button click
        if button == QMessageBox.Ok:
            print("Selected angle:", angle)
            self.rotate_image(angle)
        else:
            print("Dialog canceled")

    def open_dialogSeuillage(self):
            msg = QMessageBox()
            msg.setWindowTitle("Seuillage Manuel")
            msg.setText("Donner Seuil")

            # create a spin box widget
            spin_box = QSpinBox()
            spin_box.setRange(0, 360)
            spin_box.setValue(0)

            # add the spin box widget to the message box
            layout = msg.layout()
            layout.addWidget(spin_box)
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            # execute the message box and get the selected button
            button = msg.exec_()

            # get the selected angle from the spin box
            Seuil = spin_box.value()

            # handle the button click
            if button == QMessageBox.Ok:
                    print("Selected seuil:", Seuil)
                    self.binarisationManuel(Seuil)

            else:
                    print("Dialog canceled")


    def open_dialogRedmesionner(self):
            # create message box widget
            msg = QMessageBox()
            msg.setWindowTitle("Redimensionner")

            # create a group box to hold the radio buttons
            group_box = QGroupBox("Méthode de redimensionnement")

            # create radio buttons for width/height and percentage options
            width_height_button = QRadioButton("Largeur/Hauteur")
            percentage_button = QRadioButton("Pourcentage")

            # set width/height button as default option
            width_height_button.setChecked(True)

            # create spin box widgets for width and height
            width_spin_box = QSpinBox()
            height_spin_box = QSpinBox()
            width_spin_box.setRange(1, 10000)
            height_spin_box.setRange(1, 10000)
            # width_spin_box.setValue(self.image.width())
            # height_spin_box.setValue(self.image.height())

            # create spin box widget for percentage
            percentage_spin_box = QSpinBox()
            percentage_spin_box.setRange(1, 1000)
            percentage_spin_box.setValue(100)

            # disable width/height spin boxes initially
            width_spin_box.setEnabled(True)
            height_spin_box.setEnabled(True)
            percentage_spin_box.setEnabled(False)

            # connect radio buttons to slot for enabling/disabling spin boxes
            def on_radio_button_clicked():
                    width_spin_box.setEnabled(width_height_button.isChecked())
                    height_spin_box.setEnabled(width_height_button.isChecked())
                    percentage_spin_box.setEnabled(percentage_button.isChecked())

            width_height_button.clicked.connect(on_radio_button_clicked)
            percentage_button.clicked.connect(on_radio_button_clicked)

            # create a layout for the group box and add the radio buttons and spin boxes
            group_layout = QVBoxLayout()
            group_layout.addWidget(width_height_button)
            group_layout.addWidget(width_spin_box)
            group_layout.addWidget(height_spin_box)
            group_layout.addWidget(percentage_button)
            group_layout.addWidget(percentage_spin_box)
            group_box.setLayout(group_layout)

            # add the group box to the message box
            layout = msg.layout()
            layout.addWidget(group_box)

            # add standard buttons to the message box
            msg.addButton(QMessageBox.Ok)
            msg.addButton(QMessageBox.Cancel)

            # execute the message box and get the selected button
            button = msg.exec_()

            # handle the button click
            if button == QMessageBox.Ok:
                    # get the selected option (width/height or percentage)
                    if width_height_button.isChecked():
                            width = width_spin_box.value()
                            height = height_spin_box.value()
                            print("Selected width and height:", width, height)
                            self.RedimentionnerWidth_Hieght(width,height)

                    else:
                            percentage = percentage_spin_box.value()
                            print("Selected percentage:", percentage)
                            self.Redimentionner(percentage)

            else:
                    print("Dialog canceled")
    def open_dialogGaussien(self):
        msg = QMessageBox()
        msg.setWindowTitle("Filtre Gaussien")
        msg.setText("Donner  une valeur pour L'ecart type")

        # create a spin box widget
        spin_box = QSpinBox()
        spin_box.setRange(0, 360)
        spin_box.setValue(0)

        # add the spin box widget to the message box
        layout = msg.layout()
        layout.addWidget(spin_box)
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        # execute the message box and get the selected button
        button = msg.exec_()

        # get the selected angle from the spin box
        ecart = spin_box.value()

        # handle the button click
        if button == QMessageBox.Ok:
            print("Selected angle:", ecart)
            self.FiltreGaussien(ecart)
        else:
            print("Dialog canceled")

    def open_dialogMoyenneur(self):
            msg = QMessageBox()
            msg.setWindowTitle("Filtre Moyyenneur")
            msg.setText("Donner la taille de filtre")

            # create a spin box widget
            spin_box = QSpinBox()
            spin_box.setRange(0, 360)
            spin_box.setValue(0)

            # add the spin box widget to the message box
            layout = msg.layout()
            layout.addWidget(spin_box)
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            # execute the message box and get the selected button
            button = msg.exec_()

            # get the selected angle from the spin box
            ecart = spin_box.value()

            # handle the button click
            if button == QMessageBox.Ok:
                    print("Selected angle:", ecart)
                    self.FiltreMoyenneur(ecart)
            else:
                    print("Dialog canceled")
    def open_dialogMedian(self):
            msg = QMessageBox()
            msg.setWindowTitle("Filtre Median")
            msg.setText("Donner  une valeur pour la taille du filtre")

            # create a spin box widget
            spin_box = QSpinBox()
            spin_box.setRange(0, 360)
            spin_box.setValue(0)

            # add the spin box widget to the message box
            layout = msg.layout()
            layout.addWidget(spin_box)
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            # execute the message box and get the selected button
            button = msg.exec_()

            # get the selected angle from the spin box
            taille = spin_box.value()

            # handle the button click
            if button == QMessageBox.Ok:
                    self.FiltreMedian(taille)

            else:
                    print("Dialog canceled")
    def RedimentionnerWidth_Hieght(self,width,height):
            image = self.widget_2.pixmap().toImage()
            buffer = QtCore.QBuffer()
            buffer.open(QtCore.QIODevice.ReadWrite)
            image.save(buffer, "PNG")
            img_str = buffer.data()
            nparr = np.frombuffer(img_str, np.uint8)
            img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

            if img_np is None:
                    raise ValueError("Failed to decode image")
            print("Sbbbbbbbbb:")
            img_np = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
            img_format = QtGui.QImage.Format_RGB888
            resized_image = cv2.resize(img_np, (width, height))
            height, width, channel = resized_image.shape
            q_img = QtGui.QImage(resized_image.data, width, height, width * channel, img_format)
            pixmap = QtGui.QPixmap.fromImage(q_img.convertToFormat(QtGui.QImage.Format_RGB888))
            self.widget_2.setPixmap(pixmap.scaled(self.widget_2.size(), QtCore.Qt.KeepAspectRatio))


    def Redimentionner(self,percent):
        image = self.widget_2.pixmap().toImage()
        buffer = QtCore.QBuffer()
        buffer.open(QtCore.QIODevice.ReadWrite)
        image.save(buffer, "PNG")
        img_str = buffer.data()
        nparr = np.frombuffer(img_str, np.uint8)
        img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        if img_np is None:
            raise ValueError("Failed to decode image")
        print("Sbbbbbbbbb:")
        img_np = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
        img_format = QtGui.QImage.Format_RGB888
        width = int(img_np.shape[1] * percent / 100)
        height = int(img_np.shape[0] * percent / 100)

        resized_image = cv2.resize(img_np, (width, height))
        height, width, channel = resized_image.shape
        q_img = QtGui.QImage(resized_image.data, width, height, width * channel, img_format)
        pixmap = QtGui.QPixmap.fromImage(q_img.convertToFormat(QtGui.QImage.Format_RGB888))
        self.widget_2.setPixmap(pixmap.scaled(self.widget_2.size(), QtCore.Qt.KeepAspectRatio))

    # def select_region(self):
    #         # Get the current pixmap of the label widget
    #         pixmap = self.widget_2.pixmap()
    #
    #         if pixmap:
    #                 # Create a copy of the pixmap
    #                 pixmap_copy = pixmap.copy()
    #
    #                 # Create a QPainter object to draw on the pixmap copy
    #                 painter = QtGui.QPainter(pixmap_copy)
    #                 painter.setPen(QtGui.QPen(QtGui.QColor("red"), 2))
    #
    #                 # Draw a rectangle on the pixmap copy using the current selection
    #                 if self.selection_rect:
    #                         painter.drawRect(self.selection_rect)
    #
    #                 # Set the modified pixmap as the new pixmap of the label widget
    #                 self.widget_2.setPixmap(pixmap_copy)
    #
    # def mousePressEvent(self, event):
    #         self.selection_rect = QtCore.QRectF(event.pos(), QtCore.QSizeF(0, 0))
    #
    # def mouseMoveEvent(self, event):
    #         if self.selection_rect:
    #                 self.selection_rect = QtCore.QRectF(self.selection_rect.topLeft(), event.pos()).normalized()
    #                 self.select_region()
    #
    # def mouseReleaseEvent(self, event):
    #         if self.selection_rect:
    #                 self.selection_rect = QtCore.QRectF(self.selection_rect.topLeft(), event.pos()).normalized()
    #                 self.select_region()
    #                 self.selection_rect = None

    def binarisationManuel(self,seuil):
            image = self.widget_2.pixmap().toImage()
            buffer = QtCore.QBuffer()
            buffer.open(QtCore.QIODevice.ReadWrite)
            image.save(buffer, "PNG")
            img_str = buffer.data()
            nparr = np.frombuffer(img_str, np.uint8)
            img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

            if img_np is None:
                    raise ValueError("Failed to decode image")
            print("Sbbbbbbbbb:")
            img_np = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
            img_format = QtGui.QImage.Format_RGB888

            r, g, b = cv2.split(img_np)

            # Appliquer la binarisation à chaque canal de couleur
            _, r_bin = cv2.threshold(r, seuil, 255, cv2.THRESH_BINARY)
            _, g_bin = cv2.threshold(g, seuil, 255, cv2.THRESH_BINARY)
            _, b_bin = cv2.threshold(b, seuil, 255, cv2.THRESH_BINARY)

            # Fusionner les canaux binarisés pour former une image en couleur binaire
            img_bin = cv2.merge((r_bin, g_bin, b_bin))

            height, width, channel = img_bin.shape
            q_img = QtGui.QImage(img_bin.data, width, height, width * channel, img_format)
            pixmap = QtGui.QPixmap.fromImage(q_img.convertToFormat(QtGui.QImage.Format_RGB888))
            self.widget_2.setPixmap(pixmap.scaled(self.widget_2.size(), QtCore.Qt.KeepAspectRatio))
    def binarisationOTSU(self):
            image = self.widget_2.pixmap().toImage()
            buffer = QtCore.QBuffer()
            buffer.open(QtCore.QIODevice.ReadWrite)
            image.save(buffer, "PNG")
            img_str = buffer.data()
            nparr = np.frombuffer(img_str, np.uint8)
            img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

            if img_np is None:
                    raise ValueError("Failed to decode image")
            print("Sbbbbbbbbb:")
            img_np = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
            img_format = QtGui.QImage.Format_RGB888

            r, g, b = cv2.split(img_np)

            # Appliquer la binarisation à chaque canal de couleur
            ret, r_bin = cv2.threshold(r, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
            ret, g_bin = cv2.threshold(g, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
            ret, b_bin = cv2.threshold(b, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

            # Fusionner les canaux binarisés pour former une image en couleur binaire
            img_bin = cv2.merge((r_bin, g_bin, b_bin))

            height, width, channel = img_bin.shape
            q_img = QtGui.QImage(img_bin.data, width, height, width * channel, img_format)
            pixmap = QtGui.QPixmap.fromImage(q_img.convertToFormat(QtGui.QImage.Format_RGB888))
            self.widget_2.setPixmap(pixmap.scaled(self.widget_2.size(), QtCore.Qt.KeepAspectRatio))
    def PartitionD(self):
            image = self.widget_2.pixmap().toImage()
            buffer = QtCore.QBuffer()
            buffer.open(QtCore.QIODevice.ReadWrite)
            image.save(buffer, "PNG")
            img_str = buffer.data()
            nparr = np.frombuffer(img_str, np.uint8)
            img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

            if img_np is None:
                    raise ValueError("Failed to decode image")
            print("Sbbbbbbbbb:")
            img_np = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
            img_format = QtGui.QImage.Format_RGB888

            region_mask = segmentation.felzenszwalb(color.rgb2gray(img_np), scale=100, sigma=0.5, min_size=50)
            region_mask=color.label2rgb(region_mask, img_np, kind='avg')
            height, width, channel = region_mask.shape
            q_img = QtGui.QImage(region_mask.data, width, height, width * channel, img_format)
            pixmap = QtGui.QPixmap.fromImage(q_img.convertToFormat(QtGui.QImage.Format_RGB888))
            self.widget_2.setPixmap(pixmap.scaled(self.widget_2.size(), QtCore.Qt.KeepAspectRatio))
    def CroissanceRegionsD(self):
        image = self.widget_2.pixmap().toImage()
        buffer = QtCore.QBuffer()
        buffer.open(QtCore.QIODevice.ReadWrite)
        image.save(buffer, "PNG")
        img_str = buffer.data()
        nparr = np.frombuffer(img_str, np.uint8)
        img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        if img_np is None:
            raise ValueError("Failed to decode image")
        print("Sbbbbbbbbb:")
        img_np = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
        img_format = QtGui.QImage.Format_RGB888
        b, g, r = cv2.split(img_np)

        # Appliquer la croissance de région à chaque canal de couleur
        for channel in [b, g, r]:
                # Convertir l'image en une image binaire
                thresh = cv2.threshold(channel, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

                # Créer une image de masque pour stocker les pixels segmentés
                mask = np.zeros((channel.shape[0] + 2, channel.shape[1] + 2), np.uint8)

                # Choisir un point de départ pour la croissance de la région
                seed_point = (img_np.shape[1] // 2, img_np.shape[0] // 2)

                # Appliquer la croissance de la région à partir du point de départ
                cv2.floodFill(thresh, mask, seed_point, 255)

                # Réaffecter le canal de couleur avec l'image segmentée
                channel[:] = cv2.bitwise_and(channel, channel, mask=thresh)

        # Fusionner les canaux de couleur ensemble pour produire l'image segmentée en couleur
        segmented_img = cv2.merge((b, g, r))
        height, width, channel1 = segmented_img.shape

        q_img = QtGui.QImage(segmented_img.data.tobytes(), width, height, width * channel1, img_format)

        pixmap = QtGui.QPixmap.fromImage(q_img.convertToFormat(QtGui.QImage.Format_RGB888))
        self.widget_2.setPixmap(pixmap.scaled(self.widget_2.size(), QtCore.Qt.KeepAspectRatio))

    def annuler(self):
            pixmap=self.widget_77.pixmap()
            self.widget_2.setPixmap(pixmap.scaled(self.widget_2.size(), QtCore.Qt.KeepAspectRatio))
    def save_image(self):
            # Ouvrir une boîte de dialogue pour sélectionner le nom de fichier
            file_name, _ = QFileDialog.getSaveFileName(self, "Enregistrer l'image", "",
                                                       "Images (*.png *.xpm *.jpg *.bmp);;Tous les fichiers (*.*)")

            if file_name:
                    # Enregistrer l'image
                    self.widget_2.pixmap().save(file_name)

    def compressionOndelette(self):
            image = self.widget_2.pixmap().toImage()
            buffer = QtCore.QBuffer()
            buffer.open(QtCore.QIODevice.ReadWrite)
            image.save(buffer, "PNG")
            img_str = buffer.data()
            nparr = np.frombuffer(img_str, np.uint8)
            img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

            if img_np is None:
                    raise ValueError("Failed to decode image")
            print("Sbbbbbbbbb:")
            img_np = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
            img_format = QtGui.QImage.Format_RGB888
            # Décomposer l'image en utilisant la transformée en ondelette de Haar
            coeffs = pywt.dwt2(img_np, 'haar')

            # Quantifier les coefficients de la transformée
            coeffs_quant = [pywt.threshold(i, value=1, mode='soft') for i in coeffs]

            # Reconstruire l'image à partir des coefficients quantifiés
            image_compress = pywt.idwt2(coeffs_quant, 'haar')
            pixels_compressed = np.uint8(image_compress)
            # pixels_compressed = cv2.cvtColor(pixels_compressed, cv2.COLOR_BGR2RGB)
            # cv2.imshow("Ondelette Image", pixels_compressed)
            # cv2.waitKey(0)
            # cv2.destroyAllWindows()
            # pixels_compressed = cv2.cvtColor(pixels_compressed, cv2.COLOR_BGR2RGB)
            image=pixels_compressed
            height, width, channel = image.shape
            # pixels_compressed = cv2.cvtColor(pixels_compressed, cv2.COLOR_BGR2RGB)
            q_img = QtGui.QImage(image.data.tobytes(), width, height, width * channel, img_format)

            pixmap = QtGui.QPixmap.fromImage(q_img.convertToFormat(QtGui.QImage.Format_BGR30))
            self.widget_2.setPixmap(pixmap.scaled(self.widget_2.size(), QtCore.Qt.KeepAspectRatio))

    def compress_huffman(self):
            # Récupérer l'image
            img = self.widget_2.pixmap().toImage()
            if img.isNull():
                    QMessageBox.warning(self, "Erreur", "Veuillez d'abord ouvrir une image.")
                    return

            # Ouvrir une boîte de dialogue pour sélectionner le nom de fichier de sortie
            output_file, _ = QFileDialog.getSaveFileName(self, "Enregistrer la version compressée", "",
                                                         "Fichiers compressés (*.huff);;Tous les fichiers (*.*)")
            if not output_file:
                    return

            # Convertir l'image en une matrice numpy de pixels
            buffer = img.bits()
            buffer.setsize(img.byteCount())
            pixels = bytearray(buffer)
            width, height = img.width(), img.height()

            # Calculer l'histogramme des fréquences d'apparition de chaque couleur
            freqs = defaultdict(int)
            for i in range(0, len(pixels), 4):
                    r, g, b, _ = pixels[i:i + 4]
                    freqs[(r, g, b)] += 1

            # Construire un arbre de Huffman à partir de l'histogramme
            heap = [[freq, [color, ""]] for color, freq in freqs.items()]
            heapq.heapify(heap)
            while len(heap) > 1:
                    lo, hi = heapq.heappop(heap), heapq.heappop(heap)
                    for pair in lo[1:]:
                            pair[1] = '0' + pair[1]
                    for pair in hi[1:]:
                            pair[1] = '1' + pair[1]
                    heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])

            # Construire un dictionnaire des codes de chaque couleur
            codes = dict(heapq.heappop(heap)[1:])

            # Convertir les pixels de l'image en une chaîne de bits
            bitstring = ""
            for i in range(0, len(pixels), 4):
                    r, g, b, _ = pixels[i:i + 4]
                    bitstring += codes[(r, g, b)]

            # Ajouter un marqueur de fin pour éviter les problèmes de padding
            bitstring += "0" * ((8 - len(bitstring) % 8) % 8)
            bitstring += "1" * 32

            # Convertir la chaîne de bits en une liste de bytes
            compressed_bytes = []
            for i in range(0, len(bitstring), 8):
                    byte = int(bitstring[i:i + 8], 2)
                    compressed_bytes.append(byte)

            # Écrire les bytes compressés dans le fichier de sortie
            with open(output_file, "wb") as f:
                    f.write(bytes(compressed_bytes))

            # Afficher un message de confirmation
            QMessageBox.information(self, "Compression",
                                    f"Image compressée avec succès. Taille du fichier : {os.path.getsize(output_file)} octets.")

    # def LZW(self):
    #         img = self.widget_2.pixmap().toImage()
    #         compressed_str = lzw.compress(img)
    #
    #
    #         file_name, _ = QFileDialog.getSaveFileName(self, "Enregistrer l'image compressée", "",
    #                                            "Images compressées (*.lzw);;Tous les fichiers (*.*)")
    #         if file_name:
    #          # Écrire la chaîne de pixels compressée dans un fichier
    #           with open(file_name, "wb") as f:
    #                 f.write(compressed_str)
    def LZW(self):

       image = Image.open(self.path)
       
    # Créer un objet io.BytesIO
       output = io.BytesIO()

    # Enregistrer l'image compressée dans l'objet io.BytesIO
       extension = 'png'
       image.save(output, format='TIFF', compression='tiff_lzw')

    # Ouvrir l'image compressée à partir de l'objet io.BytesIO
       compressed_image = Image.open(output)

    # Afficher l'image
       compressed_image.imshow()
    # Obtenir la taille de l'image compressée
       height, width = compressed_image.size

    # Convertir l'image compressée en QImage
       q_img = QtGui.QImage(compressed_image.tobytes(), width, height, QtGui.QImage.Format_RGBA8888)

    # Créer un QPixmap à partir de l'image QImage
       pixmap = QtGui.QPixmap.fromImage(q_img)

    # Afficher le QPixmap dans le widget
       self.widget_2.setPixmap(pixmap)
    def selectionner(self):
            image = self.widget_77.pixmap().toImage()
            buffer = QtCore.QBuffer()
            buffer.open(QtCore.QIODevice.ReadWrite)
            image.save(buffer, "PNG")
            img_str = buffer.data()
            nparr = np.frombuffer(img_str, np.uint8)
            img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

            if img_np is None:
                    raise ValueError("Failed to decode image")
            print("Sbbbbbbbbb:")
            img_np = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
            img_format = QtGui.QImage.Format_RGB888

            img_np1 = cv2.cvtColor(img_np, cv2.COLOR_RGB2BGR)
            # Attendre que l'utilisateur sélectionne une zone
            cv2.imshow('image', img_np1)

            rect = cv2.selectROI('image', img_np1, False)

            # Extraire la zone sélectionnée de l'image
            roi = img_np[int(rect[1]):int(rect[1] + rect[3]), int(rect[0]):int(rect[0] + rect[2])]

            # roi = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
            height, width, channel = roi.shape
            # pixels_compressed = cv2.cvtColor(pixels_compressed, cv2.COLOR_BGR2RGB)
            q_img = QtGui.QImage(roi.data.tobytes(), width, height, width * channel, img_format)
            pixmap = QtGui.QPixmap.fromImage(q_img.convertToFormat(QtGui.QImage.Format_RGB888))

            self.widget_2.setPixmap(pixmap.scaled(self.widget_2.size(), QtCore.Qt.KeepAspectRatio))
    def ComressionJPEG(self):
            image = self.widget_77.pixmap().toImage()
            buffer = QtCore.QBuffer()
            buffer.open(QtCore.QIODevice.ReadWrite)
            image.save(buffer, "PNG")
            img_str = buffer.data()
            nparr = np.frombuffer(img_str, np.uint8)
            img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

            if img_np is None:
                    raise ValueError("Failed to decode image")
            print("Sbbbbbbbbb:")
            img_np = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
            img_format = QtGui.QImage.Format_RGB888
            image = cv2.resize(img_np, (224, 224))

            R, G, B = cv2.split(image)

            # def transformation cosinus cdt
            def dct2(a):
                    return dct(dct(a.T, norm='ortho').T, norm='ortho')

            # def quantification Q

            def quantification(Q, cdt):
                    return np.round(cdt / Q)

            dtcR = dct2(R)
            print(dtcR)
            dtcG = dct2(G)
            print(dtcG)
            dtcB = dct2(B)
            print(dtcB)

            # Appliquer la quantification à chaque canal de couleur

            # Rassembler les canaux quantifiés en une seule matrice RGB

            jpegQuantizationMatrix = [
                    [16, 11, 10, 16, 24, 40, 51, 61],
                    [12, 12, 14, 19, 26, 58, 60, 55],
                    [14, 13, 16, 24, 40, 57, 69, 56],
                    [14, 17, 22, 29, 51, 87, 80, 62],
                    [18, 22, 37, 56, 68, 109, 103, 77],
                    [24, 35, 55, 64, 81, 104, 113, 92],
                    [49, 64, 78, 87, 103, 121, 120, 101],
                    [72, 92, 95, 98, 112, 100, 103, 99]
            ]

            R_blocks = np.zeros((image.shape[0] // 8, image.shape[1] // 8, 8, 8))
            G_blocks = np.zeros((image.shape[0] // 8, image.shape[1] // 8, 8, 8))
            B_blocks = np.zeros((image.shape[0] // 8, image.shape[1] // 8, 8, 8))
            for i in range(image.shape[0] // 8):
                    for j in range(image.shape[1] // 8):
                            R_block = image[i * 8:i * 8 + 8, j * 8:j * 8 + 8, 0]
                            G_block = image[i * 8:i * 8 + 8, j * 8:j * 8 + 8, 1]
                            B_block = image[i * 8:i * 8 + 8, j * 8:j * 8 + 8, 2]
                            R_dct = cv2.dct(R_block.astype(np.float32))
                            G_dct = cv2.dct(G_block.astype(np.float32))
                            B_dct = cv2.dct(B_block.astype(np.float32))
                            R_blocks[i, j] = R_dct
                            G_blocks[i, j] = G_dct
                            B_blocks[i, j] = B_dct

            R_quantized = np.round(R_blocks / jpegQuantizationMatrix)
            G_quantized = np.round(G_blocks / jpegQuantizationMatrix)
            B_quantized = np.round(B_blocks / jpegQuantizationMatrix)

            quantized_image = np.empty_like(image)
            for i in range(image.shape[0] // 8):
                    for j in range(image.shape[1] // 8):
                            R_block_quantized = R_quantized[i, j]
                            G_block_quantized = G_quantized[i, j]
                            B_block_quantized = B_quantized[i, j]
                            R_block_reconstructed = cv2.idct(R_block_quantized)
                            G_block_reconstructed = cv2.idct(G_block_quantized)
                            B_block_reconstructed = cv2.idct(B_block_quantized)
                            block_reconstructed = np.dstack(
                                    (B_block_reconstructed, G_block_reconstructed, R_block_reconstructed))
                            quantized_image[i * 8:i * 8 + 8, j * 8:j * 8 + 8] = block_reconstructed

            print(quantized_image)

            R_blocks = np.zeros((image.shape[0] // 8, image.shape[1] // 8, 8, 8))
            G_blocks = np.zeros((image.shape[0] // 8, image.shape[1] // 8, 8, 8))
            B_blocks = np.zeros((image.shape[0] // 8, image.shape[1] // 8, 8, 8))
            for i in range(image.shape[0] // 8):
                    for j in range(image.shape[1] // 8):
                            R_block = image[i * 8:i * 8 + 8, j * 8:j * 8 + 8, 0]
                            G_block = image[i * 8:i * 8 + 8, j * 8:j * 8 + 8, 1]
                            B_block = image[i * 8:i * 8 + 8, j * 8:j * 8 + 8, 2]
                            R_dct = cv2.dct(R_block.astype(np.float32))
                            G_dct = cv2.dct(G_block.astype(np.float32))
                            B_dct = cv2.dct(B_block.astype(np.float32))
                            R_blocks[i, j] = R_dct
                            G_blocks[i, j] = G_dct
                            B_blocks[i, j] = B_dct

            # Rassembler les matrices de couleurs reconstruites en une seule matrice RGB
            R_reconstructed = np.zeros_like(image[:, :, 0])
            G_reconstructed = np.zeros_like(image[:, :, 1])
            B_reconstructed = np.zeros_like(image[:, :, 2])
            for i in range(image.shape[0] // 8):
                    for j in range(image.shape[1] // 8):
                            R_block_dct = R_blocks[i, j]
                            G_block_dct = G_blocks[i, j]
                            B_block_dct = B_blocks[i, j]
                            R_block_reconstructed = cv2.idct(R_block_dct)
                            G_block_reconstructed = cv2.idct(G_block_dct)
                            B_block_reconstructed = cv2.idct(B_block_dct)
                            R_reconstructed[i * 8:i * 8 + 8, j * 8:j * 8 + 8] = R_block_reconstructed
                            G_reconstructed[i * 8:i * 8 + 8, j * 8:j * 8 + 8] = G_block_reconstructed
                            B_reconstructed[i * 8:i * 8 + 8, j * 8:j * 8 + 8] = B_block_reconstructed

            reconstructed_image = np.dstack((B_reconstructed, G_reconstructed, R_reconstructed))
            # reconstructed_image = cv2.cvtColor(reconstructed_image, cv2.COLOR_BGR2RGB)
            cv2.imshow("Reconstructed Image", reconstructed_image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            height, width, channel = reconstructed_image.shape
            # pixels_compressed = cv2.cvtColor(pixels_compressed, cv2.COLOR_BGR2RGB)
            q_img = QtGui.QImage(reconstructed_image.data.tobytes(), width, height, width * channel, img_format)

            pixmap = QtGui.QPixmap.fromImage(q_img.convertToFormat(QtGui.QImage.Format_BGR30))
            self.widget_2.setPixmap(pixmap.scaled(self.widget_2.size(), QtCore.Qt.KeepAspectRatio))

    def drag_image(self):
            file_path="null"
            def handle_drop(e):
                    if e.mimeData().hasImage:
                            file_path = e.mimeData().urls()[0].toLocalFile()
                            pixmap = QtGui.QPixmap(file_path)
                            self.widget_77.setPixmap(pixmap.scaled(self.widget_77.size(), QtCore.Qt.KeepAspectRatio))
                            self.widget_2.setPixmap(pixmap.scaled(self.widget_2.size(), QtCore.Qt.KeepAspectRatio))

                            e.accept()
                            self.label1.hide()
                            self.pushButton_6.hide()
                    else:
                            e.ignore()


            self.widget_77.setAcceptDrops(True)
            self.widget_77.dragEnterEvent = handle_drop
            self.widget_77.dropEvent = handle_drop







if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())