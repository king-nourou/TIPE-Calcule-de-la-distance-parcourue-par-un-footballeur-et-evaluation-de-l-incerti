from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import random as rd
from ui_fenetre import Ui_MainWindow

nombre_points = 12
nombre_simulations = 10

class fenetreLignes(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setGeometry(600,100,1900,1000)
        self.canvas=ZoneG(self)
        self.canvas.setGeometry(450,100,853,567)

class ZoneG(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.qp=QPixmap(1000,1000)
        self.qp.fill(Qt.white)
        liste_abcisses1 = [52, 43.8, 36.8, 42.8, 49.6, 55.6, 75.2, 63.2, 46.8, 36.6, 28.4, 29.2, 29.8, 26.4, 27.4, 31.0,
                           33.2, 33.8, 33.4, 32.4, 33.2, 35.2, 38.4, 40.8, 41.8, 41.0, 41.0, 44.4, 48.2, 51.0, 50.0,
                           45.8, 37.4, 25.2, 16.8, 21.0, 26.4, 38.0, 47.2, 41.4, 39.2, 43.8, 36.8, 33.0, 29.4, 23.4,
                           17.6, 16.8, 19.8, 23.8, 24.8, 24.8, 23.6, 19.6, 15.6, 10.6, 5.0, 4.6, 9.0, 16.4]

        liste_ordonnees1 = [42.6, 38.4, 38.4, 48.6, 56.8, 66.4, 58.2, 55.8, 57.2, 50.6, 49.8, 50.8, 53.4, 52.4, 50.4,
                            52.2, 54.4, 56.4, 56.8, 55.0, 56.8, 58.0, 57.6, 56.6, 53.6, 51.2, 48.8, 48.0, 48.4, 51.6,
                            58.0, 65.0, 68.4, 67.6, 61.4, 58.0, 55.0, 51.8, 58.2, 60.0, 60.2, 58.6, 58.8, 60.4, 60.8,
                            62.0, 62.2, 59.6, 59.4, 60.2, 57.8, 56.8, 55.8, 58.6, 58.2, 51.6, 59.8, 62.2, 61.4, 58.2]
        self.liste_abcisses =[e * 7.6 for e in liste_abcisses1[:12]]
        self.liste_ordonnees = [e * 8 for e in liste_ordonnees1[:12]]

        self.matrice_abcisses, self.matrice_ordonnees = self.generateur_coordonnees_modele_1(self.liste_abcisses,
                                                                                             self.liste_ordonnees,
                                                                                             nombre_points,
                                                                                             nombre_simulations)

        p = QPainter(self.qp)
        p.setBrush(Qt.black)
        image = QImage()
        image.load("../terrain.jpg")
        p.drawImage(QRect(0, 0, 853, 567),image)
        p.drawEllipse(0, 0, 10, 10)
        p.drawEllipse(0, 554, 10, 10)
        p.drawEllipse(840, 0, 10, 10)

        self.joueur_reel(p)

    def paintEvent(self, QPaintEvent):
        p=QPainter(self)
        p.drawPixmap(0,0,self.qp)

    def generateur_coordonnees_modele_1(self, liste_abcisses, liste_ordonnees, nombre_points, nombre_simulations):
        matrice_abcisses = []  # Initialisation de l'ensemble des listes des abcisses
        matrice_ordonnees = []  # Initialisation de l'ensemble des listes des ordonnees

        for _ in range(nombre_simulations):
            matrice_abcisses.append([])
            matrice_ordonnees.append([])

        for i in range(nombre_points):  # Iteration pour chaque coordonnee
            x0 = liste_abcisses[i]  # Recuperation de la ieme abcisse
            y0 = liste_ordonnees[i]  # Recuperation de la ieme ordonnee

            for j in range(nombre_simulations):  # On releve n points coordonnes autour de chaque point
                x1 = rd.uniform(x0 - 1, x0 + 1)  # Aleatoirement
                y1 = rd.uniform(y0 - 1, y0 + 1)

                matrice_abcisses[j].append(x1)  # Ajout à la jeme liste des abcisses
                matrice_ordonnees[j].append(y1)  # Ajout à la jeme liste des ordonnees

        return matrice_abcisses, matrice_ordonnees

    def joueur_reel(self, p):
        pen = QPen(Qt.black)
        p.setBrush(Qt.white)
        pen.setWidth(2)
        p.setPen(pen)

        for i in range(nombre_points - 1):

            x0 = int(self.liste_abcisses[i])
            x1 = int(self.liste_abcisses[i + 1])
            y0 = int(self.liste_ordonnees[i])
            y1 = int(self.liste_ordonnees[i + 1])

            p.drawEllipse(x0, y0, 20, 20)
            p.drawEllipse(x1, y1, 20, 20)
            p.drawLine(x0, y0, x1, y1)

        self.update()

app = QApplication(sys.argv)
essai = fenetreLignes()
essai.show()
app.exec()

