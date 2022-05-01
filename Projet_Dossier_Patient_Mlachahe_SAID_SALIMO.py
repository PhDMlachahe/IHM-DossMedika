#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Mlachahe
"""

import pandas as pd
import datetime
import sys

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


# %%
class ViewAccueil(QWidget):
    """
    Cette classe est liée à la fenêtre Accueil.
    Dès lors qu'elle est instanciée, une fenêtre Accueil est ouverte.
    """
    def __init__(self, ctrl):
        # Initialisation des attributs de la classe mère
        super().__init__()

        # Initialisation du controller
        self.myCtrl = ctrl

        # Initialisation des QLabel
        self.slogan_label = QLabel("DossMedika, le E-dossier médical !")
        # Initialisation de l'image et de son Qlabel
        self.pixmap = QPixmap('DossMedika_logo.png').scaledToHeight(220)
        self.labelpix = QLabel(self)

        # Initialisation des boutons
        self.creerDossier_btn = QPushButton('📋  Créer un dossier')
        self.ouvrirDossier_btn = QPushButton('📁  Ouvrir un dossier')

        # Appel de la fonction qui implémenter l'user interfaces lié à la fenêtre Accueil
        self.init_ui()
        # Afficher la fenêtre ViewAccueil
        self.show()

    def init_ui(self):
        # WINDOW ################################
        self.setWindowTitle("DossMedika") # mettre un titre
        self.setWindowIcon(QIcon('DossMedika_logo.png')) # mettre une icone
        self.labelpix.setPixmap(self.pixmap) # mettre une image

        # LAYOUT ################################
        # Créer une layout verticale v_layout, et y ajouter les labels
        v_layout = QVBoxLayout()
        v_layout.addWidget(self.labelpix)
        v_layout.addWidget(self.slogan_label)
        # Créer une layout horizontale h_layout, et y ajouter les boutons
        h_layout = QHBoxLayout()
        h_layout.addWidget(self.creerDossier_btn)
        h_layout.addWidget(self.ouvrirDossier_btn)
        # Imbriquer toute les layouts
        v_layout.addLayout(h_layout)
        # Définir la layout principale de la fenêtre
        self.setLayout(v_layout)

        # CLICK ################################
        # Appel des fonctions clicked sur chaque bouton
        self.creerDossier_btn.clicked.connect(self.bouton_nouveauDossier_click)
        self.ouvrirDossier_btn.clicked.connect(self.bouton_ouvrirDossier_click)


    def bouton_nouveauDossier_click(self):
        # Ouvrir une fenêtre Dossier
        self.cams = ViewDossier(self.myCtrl)
        # Fermer la fenêtre Accueil
        self.close()

    def bouton_ouvrirDossier_click(self):
        # Ouvrir une fenêtre GestionnaireDossiers
        self.cams = ViewGestionnaireDossiers(self.myCtrl)
        # Fermer la fenêtre Accueil
        self.close()


class ViewDossier(QWidget):
    """
    Cette classe est liée à la fenêtre Dossier.
    Dès lors qu'elle est instanciée, une fenêtre Dossier est ouverte.
    """

    def __init__(self, ctrl,
                 titre_fenetre="Nouveau dossier médical",
                 nirID=None, date=None, nom=None, prenom=None, age=None, sexe=None, symptomes=None, propositionMed=None,
                 modifier_bool=False):
        # Initialisation des attributs de la classe mère
        super().__init__()

        # Initialisation du controller
        self.myCtrl = ctrl

        # Initialisation du titre de la fenêtre
        self.titre_fenetre = titre_fenetre
        # Initialisation du booléen permettant d'activer/désactiver la modification du Dossier'
        self.modifier_bool = modifier_bool

        # Initialisation des QGroupeBox
        self.groupbox1 = QGroupBox("👤 Informations personnelles")
        self.groupbox2 = QGroupBox("🩺 Notes médicales")
        self.groupbox3 = QGroupBox("📅 Date")

        # Initialisation des zone de textes
        self.nirID_edit = QLineEdit(nirID)
        self.date_edit = QLineEdit(date)
        self.nom_edit = QLineEdit(nom)
        self.prenom_edit = QLineEdit(prenom)
        self.age_edit = QLineEdit(age)
        self.symptomes_edit = QTextEdit(symptomes)
        self.propositionMed_edit = QLineEdit(propositionMed)
        # Initialisation des radios boutons
        self.rb1 = QRadioButton("M", self)
        self.rb2 = QRadioButton("F", self)
        self.rb1.setChecked(True) if sexe == self.rb1.text() else None  # si sexe=='M' alors appuyer, sinon rien faire
        self.rb2.setChecked(True) if sexe == self.rb2.text() else None  # si sexe=='F' alors appuyer, sinon rien faire

        # Initialisation des boutons
        self.sav_btn = QPushButton('💾  Enregistrer')
        self.mdf_btn = QPushButton('✍  Modifier')
        self.cls_btn = QPushButton('❌  Annuler')
        self.hst_btn = QPushButton('⏲️  Historique')

        # Appel de la fonction qui implémenter l'user interfaces lié à la fenêtre Dossier
        self.init_ui()
        # Afficher la fenêtre Dossier
        self.show()

    def init_ui(self):
        # WINDOW ################################
        self.setMinimumSize(350, 400)
        self.setWindowTitle(self.titre_fenetre)  # mettre un titre
        self.setWindowIcon(QIcon('DossMedika_logo.png'))  # mettre une icone

        self.sav_btn.setToolTip("Ce bouton vous permet d'enregistrer toutes les informations saisies dans votre base de données")
        self.symptomes_edit.setToolTip('Cette zone de texte est dédiée à la saisie des symptômes du patient')
        self.propositionMed_edit.setToolTip('Ici, vous sont suggérés des médicaments en fonction des symptômes que vous avez notés')

        # LAYOUT ################################

        # GROUPEBOX1 - INFORMATIONS PERSONNELLES
        # Créer une layout vertical v1_layout
        v1_layout = QVBoxLayout()
        v1_layout.addWidget(self.hst_btn)
        # Ajouter la groupbox1 à v1_layout
        v1_layout.addWidget(self.groupbox1)
        # Créer une form layout f1_layout, et y ajouter les zones de textes
        f1_layout = QFormLayout()
        f1_layout.addRow("N° Secu :", self.nirID_edit)
        f1_layout.addRow("Nom :", self.nom_edit)
        f1_layout.addRow("Prenom :", self.prenom_edit)
        f1_layout.addRow("Age :", self.age_edit)
        # Créer une layout horizontale h_rb_layout, et y ajouter les radios boutons
        h_rb_layout = QHBoxLayout()
        h_rb_layout.addWidget(self.rb1)
        h_rb_layout.addWidget(self.rb2)
        # Imbriquer toute les layouts, dans une layout verticale vbox1_layout
        vbox1_layout = QVBoxLayout()
        vbox1_layout.addLayout(f1_layout)
        vbox1_layout.addLayout(h_rb_layout)
        # Placer vbox1_layout dans la groupebox1
        self.groupbox1.setLayout(vbox1_layout)

        # GROUPEBOX2 - NOTES MEDICALES
        # Créer une layout vertical v2_layout
        v2_layout = QVBoxLayout()
        # Ajouter la groupbox1 à v2_layout
        v2_layout.addWidget(self.groupbox2)
        # Créer une form layout f2_layout, et y ajouter les zones de textes
        f2_layout = QFormLayout()
        f2_layout.addRow("Symptômes :", self.symptomes_edit)
        f2_layout.addRow("Médicaments :", self.propositionMed_edit)
        # Imbriquer toute les layouts, dans une layout verticale vbox2_layout
        vbox2_layout = QVBoxLayout()
        vbox2_layout.addLayout(f2_layout)
        # Placer vbox2_layout dans la groupebox2
        self.groupbox2.setLayout(vbox2_layout)

        # GROUPEBOX3 - DATE
        # Créer une layout vertical v3_layout
        v3_layout = QVBoxLayout()
        # Ajouter la groupbox1 à v3_layout
        v3_layout.addWidget(self.groupbox3)
        # Créer une form layout f3_layout, et y ajouter les zones de textes
        f3_layout = QFormLayout()
        f3_layout.addRow("Dernières modifications : ", self.date_edit)
        # Imbriquer toute les layouts, dans une layout verticale vbox3_layout
        vbox3_layout = QVBoxLayout()
        vbox3_layout.addLayout(f3_layout)
        # Placer vbox3_layout dans la groupebox3
        self.groupbox3.setLayout(vbox3_layout)

        # BOUTONS ENREGISTRER / MODIFIER ET ANNULER
        # Créer une layout horizontale h2_layout
        h2_layout = QHBoxLayout()
        h2_layout.addWidget(self.sav_btn) if not self.modifier_bool else None
        h2_layout.addWidget(self.mdf_btn) if self.modifier_bool else None
        h2_layout.addWidget(self.cls_btn)

        # JOINDRE v1_layout à v2_layout, v3_layout et h2_layout
        v1_layout.addLayout(v2_layout)
        v1_layout.addLayout(v3_layout)
        v1_layout.addLayout(h2_layout)
        # Définir la layout principale de la fenêtre
        self.setLayout(v1_layout)

        # CLICK ################################
        # Désactiver l'écriture dans ces zones de texte informatif
        self.propositionMed_edit.setDisabled(True)
        self.date_edit.setDisabled(True)
        # Désactiver l'écriture en fonction de l'action de l'option modification du Dossier
        self.nirID_edit.setDisabled(True) if self.modifier_bool else None
        self.nom_edit.setDisabled(True) if self.modifier_bool else None
        self.prenom_edit.setDisabled(True) if self.modifier_bool else None
        self.age_edit.setDisabled(True) if self.modifier_bool else None
        self.symptomes_edit.setDisabled(True) if self.modifier_bool else None
        self.propositionMed_edit.setDisabled(True) if self.modifier_bool else None

        # Appel des fonctions clicked sur chaque bouton
        self.cls_btn.clicked.connect(self.bouton_fermer_click)
        self.sav_btn.clicked.connect(self.bouton_enregistrer_click)
        self.mdf_btn.clicked.connect(self.bouton_modifier_click)
        self.rb1.toggled.connect(self.radiobouton_MaleFemelle_click)
        self.rb2.toggled.connect(self.radiobouton_MaleFemelle_click)
        self.symptomes_edit.mousePressEvent = self.suggerer_medicament

    def bouton_fermer_click(self):
        # Ouvrir une fenêtre Accueil
        self.cams = ViewAccueil(self.myCtrl)
        # Fermer la fenêtre Dossier
        self.close()

    def recuperer_edit_infos(self):
        # Récupérer les informations saisie dans les widgets du Dossier, et les stocker
        nirID = self.nirID_edit.text()
        date_time = self.date_edit.text()
        nom, prenom = self.nom_edit.text(), self.prenom_edit.text()
        age, sexe = self.age_edit.text(), self.radiobouton_MaleFemelle_click()
        symptomes = self.symptomes_edit.toPlainText()
        propositionMed = self.propositionMed_edit.text()
        # Retourner ces informations
        return nirID, date_time, nom, prenom, age, sexe, symptomes, propositionMed

    def bouton_modifier_click(self):
        # Ecrire le titre de la fenêtre, et y inclure le Nom et le Prenom récupéré
        titre_fenetre = "Modifier 📋 " + " ".join(self.recuperer_edit_infos()[2:4])
        # Réouvrir une fenêtre Dossier, avec les informations récupéré sur le Dossier et le mode 'Modifier' désactivé
        self.cams = ViewDossier(self.myCtrl, titre_fenetre, *self.recuperer_edit_infos(), False)
        # Fermer la fenêtre Dossier courant
        self.close()

    def bouton_enregistrer_click(self):
        try:
            # Récupérer les informations saisie dans le Dossier
            nirID, d, nom, prenom, age, sexe, symptomes, propositionMed = self.recuperer_edit_infos()
            # Récupérer la date, l'heure, la minute et la seconde courante, avec un format lisible
            date_time = datetime.datetime.now().strftime("%m/%d/%Y - %H:%M:%S")

            # Appel de la fonction qui ajoute le Dossier dans la DF, via le Controller
            self.myCtrl.ajout(nirID, date_time, nom, prenom, age, sexe, symptomes, propositionMed)
            # Appel de la fonction qui ferme le Dossier
            self.bouton_fermer_click()

        except:
            QMessageBox.about(self, "Erreur", "Impossible de sauvegarder le dossier saisie !")

    def radiobouton_MaleFemelle_click(self):
        if self.rb1.isChecked():  # Si le bouton rb1 est activé
            return self.rb1.text()  # Retourner 'M'
        if self.rb2.isChecked():  # Si le bouton rb2 est activé
            return self.rb2.text()  # Retourner 'F'


    def suggerer_medicament(self, event):
        # Récupérer le texte de la zone de texte symptomes_edit
        symptomes = self.symptomes_edit.toPlainText()
        # Tokeniser prosaïquement le text ; placer chaque mot du texte dans une liste
        symptomes = set(symptomes.split(" "))
        # Transformer chaque mot de la liste en minuscule
        symptomes = [s.lower() for s in list(symptomes)]
        # Initialiser le string med_text contenant les médicaments à prescrire
        med_text = ""
        for s in symptomes:
            # Si un mot de la liste des symptomes est compris dans la liste ci-dessous, alors ajouter le médicaments à prescrire
            if s in "fièvre grippe rhume maux douleur".split(" "):
                med_text += "/Doliprane/Dafalgan"
            if s in "cardiaques artères coeur".split(" "):
                med_text += "/Kardegic"
            if s in "intestin ventre brûlures aigreurs estomac remontées acides gastro".split(" "):
                med_text += "/Gaviscon/Spasfon"
            if s in "peau sécheresse cutanée irritation dermatoses dermatite atopique ichtyose".split(" "):
                med_text += "/Dexeryl"
            if s in "bouche buccale".split(" "):
                med_text += "/Eludril"

        # Afficher med_text dans la zone de texte propositionMed_edit
        self.propositionMed_edit.setText(med_text)


class ViewGestionnaireDossiers(QWidget):
    """
    Cette classe est liée à la fenêtre GestionDossier.
    Dès lors qu'elle est instanciée, une fenêtre GestionDossier est ouverte.
    """

    def __init__(self, ctrl):
        # Initialisation des attributs de la classe mère
        super().__init__()

        # Initialisation du controller
        self.myCtrl = ctrl

        # Initialisation des QGroupeBox
        self.groupbox1 = QGroupBox("👤 Stockage des dossiers patients")

        # Initialisation des zone de textes
        self.recherche_edit = QLineEdit()
        # Initialisation de la QlistWidget, qui affichera les dossiers dans la DF
        self.qlistewidget = QListWidget()

        # Initialisation des boutons
        self.new_btn = QPushButton('📋  Nouveau')
        self.opn_btn = QPushButton('📁  Ouvrir')
        self.spr_btn = QPushButton('🗑️  Supprimer')
        self.sav_btn = QPushButton('💾  Enregistrer (en local)')
        self.cls_btn = QPushButton('❌  Fermer')

        # Appel de la fonction qui implémenter l'user interfaces lié à la fenêtre GestionDossier
        self.init_ui()
        # Actualiser la QListWidget, contenant les dossiers
        self.action_afficher_qliste()
        # Afficher la fenêtre GestionDossier
        self.show()

    def init_ui(self):
        # WINDOW ################################
        self.setMinimumSize(350, 300)
        self.setWindowTitle("Ouvrir un dossier médical")  # mettre un titre
        self.setWindowIcon(QIcon('DossMedika_logo.png'))  # mettre une icone

        # LAYOUT ################################

        # GROUPEBOX1 - STOCKAGE DES DOSSIERS PATIENTS
        # Créer une layout vertical v1_layout
        v1_layout = QVBoxLayout()
        # Ajouter la groupbox1 à la v1_layout
        v1_layout.addWidget(self.groupbox1)
        # Créer une form layout f1_layout, et y ajouter des widgets
        f1_layout = QFormLayout()
        f1_layout.addRow("Recherche N° Secu :", self.recherche_edit)
        f1_layout.addRow(self.qlistewidget)
        # Créer une layout horizontale h1_layout
        h1_layout = QHBoxLayout()
        h1_layout.addWidget(self.new_btn)
        h1_layout.addWidget(self.opn_btn)
        h1_layout.addWidget(self.spr_btn)
        # Imbriquer toute les layouts, dans une layout verticale vbox1_layout
        vbox1_layout = QVBoxLayout()
        vbox1_layout.addLayout(f1_layout)
        vbox1_layout.addLayout(h1_layout)
        # Placer la vbox1_layout dans la groupebox1
        self.groupbox1.setLayout(vbox1_layout)
        # Ajouter des boutons à v1_layout
        v1_layout.addWidget(self.sav_btn)
        v1_layout.addWidget(self.cls_btn)

        # Joindre v1_layout et vbox1_layout
        v1_layout.addLayout(vbox1_layout)
        # Définir la layout principale de la fenêtre
        self.setLayout(v1_layout)

        # CLICK ################################
        # Appel des fonctions clicked sur chaque bouton
        self.cls_btn.clicked.connect(self.bouton_fermer_click)
        self.new_btn.clicked.connect(self.bouton_nouveauDossier_click)
        self.opn_btn.clicked.connect(self.bouton_ouvrir_click)
        self.spr_btn.clicked.connect(self.bouton_supprimer_click)
        self.sav_btn.clicked.connect(self.bouton_sauverLocal_click)

        self.qlistewidget.itemClicked.connect(self.bouton_selectionnerItem_click)

    def bouton_fermer_click(self):
        # Ouvrir une fenêtre Accueil
        self.cams = ViewAccueil(self.myCtrl)
        # Fermer la fenêtre GestionnaireDossiers
        self.close()

    def bouton_nouveauDossier_click(self):
        # Ouvrir une fenêtre Dossier
        self.cams = ViewDossier(self.myCtrl)
        # Fermer la fenêtre GestionnaireDossiers
        self.close()


    def action_afficher_qliste(self):
        # Stocker les dossiers patients contenu dans la DF, via le Controller
        classeur = self.myCtrl.listage()
        # Stocker la liste des nirID, des noms et prenom contenu dans le classeur
        nirID_list = list(list(classeur.values())[0].keys())
        nom_list = list(list(classeur.values())[1].values())
        prenom_list = list(list(classeur.values())[2].values())

        # Au préalable, vider la QListWidget
        self.qlistewidget.clear()
        # Ajouter les nirID, les noms et les prenoms associés à chaque dossier patient, dans la QListWidget
        self.qlistewidget.addItems([str(id)+' : '+str(n).upper()+' '+str(p) for (id, n, p) in zip(nirID_list, nom_list, prenom_list)])

        # Effacer la QLineEdit-recherche_edit
        self.recherche_edit.clear()


    def bouton_supprimer_click(self):
        try:
            # Recupérer le numéro de sécurité sociale
            nirID = self.recherche_edit.text().split(" : ")[0]
            # Appel de la fonction qui enleve l'élements (saisie dans la recherche_edit) de la DF, via le Controller
            self.myCtrl.retrait(nirID)
            # Actualiser la QListWidget
            self.action_afficher_qliste()
        except:
            QMessageBox.about(self, "Erreur", "Impossible de supprimer le dossier patient !")


    def rechercher_infos_patient(self, nirID):
        # Stocker les dossiers patients contenu dans la DF, via le Controller
        classeur = self.myCtrl.listage()
        # Stocker les informations des patients, dans un dictionnaire. Chaque informations (values) est lié au nirID de son patient (key).
        liste_dico = list(classeur.values())
        # Retrouver grâce à son nirID, puis stoker dans une liste, les informations du patient recherché
        liste = [d[nirID] for d in liste_dico]
        # Retourner les infos du patient recherché
        return liste

    def bouton_ouvrir_click(self):
        try:
            # Recupérer le numéro de sécurité sociale du dossier patient recherché saisie
            nirID = self.recherche_edit.text().split(" : ")[0]
            # Ecrire le titre de la fenêtre, et y inclure le Nom et le Prenom récupéré
            titre_fenetre = "Aperçu 📋 " + " ".join(self.rechercher_infos_patient(nirID)[1:3])

            # Ouvrir une fenêtre Dossier, avec les informations du dossier patient recherché
            self.cams = ViewDossier(self.myCtrl, titre_fenetre, nirID, *self.rechercher_infos_patient(nirID), True)
            # Fermer la fenêtre GestionnaireDossiers
            self.close()
        except:
            QMessageBox.about(self, "Erreur", "Impossible d'ouvrir le dossier patient !")

    def bouton_sauverLocal_click(self):
        # Appel de la fonction qui sauvegarder la DF, via le Controller
        self.myCtrl.sauvetage()

    def bouton_selectionnerItem_click(self, item):
        # Recupérer le numéro de sécurité sociale du dossier patient selectionné
        nirID = item.text().split(" : ")[0]
        # Renter l'item selectionner dans la zone de texte
        self.recherche_edit.setText(nirID)


# %%
class Controller:
    def __init__(self, model):
        self.myModel = model

    def ajout(self, nirID, date_time, nom, prenom, age, sexe, symptomes, propositionMed):
        # Retourne la fonction du Model qui ajoute le dossier patient dans la DF
        return self.myModel.ajouterPatient(nirID, date_time, nom, prenom, age, sexe, symptomes, propositionMed)

    def retrait(self, nirID):
        # Retourne la fonction du Model qui retire le dossier patient via son nirID dans la DF
        return self.myModel.retirerPatient(nirID)

    def sauvetage(self):
        # Retourne la fonction du Model qui sauvegarde la DF
        return self.myModel.sauverDF()

    def listage(self):
        # Retourne le résultat de la fonction du Model qui dictionnarise la DF
        return self.myModel.listerDF()


# %%
class Model:
    def __init__(self):
        # Initialisation de la DF
        self.df = pd.DataFrame({'Date': [], 'Nom': [], 'Prénom': [], 'Âge': [], 'Sexe': [], 'Symptômes': [], 'Médicaments': []})

    def ajouterPatient(self, nirID, date_time, nom, prenom, age, sexe, symptomes, propositionMed):
        # Ajouter les informations du dossier indexé par son nirID, dans la DF
        self.df.loc[nirID] = [date_time, nom, prenom, age, sexe, symptomes, propositionMed]

    def retirerPatient(self, nirID):
        # Enlever la ligne indexé par nirID dans la DF
        self.df.drop(nirID, inplace=True)

    def sauverDF(self):
        # Convertir la DF en CSV, et déposer le fichier en local
        self.df.to_csv("DossMedika_files.csv", sep = ';')

    def listerDF(self):
        # Stocker la DF dans un dictionnaire
        classeur = self.df.to_dict()
        # Retourner le dictionnaire
        return classeur


# %%
print(__name__)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    model = Model()
    ctrl = Controller(model)
    view = ViewAccueil(ctrl)
    sys.exit(app.exec_())
