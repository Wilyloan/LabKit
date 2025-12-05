# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(808, 297)
        MainWindow.setStyleSheet(u"QWidget {\n"
"    background-color: #121212;\n"
"    color: white;\n"
"    font-family: Verdana;\n"
"    font-size: 16pt;\n"
"    margin: 10px;\n"
"}\n"
"\n"
"QPushButton {\n"
"    border: 2px solid gray;\n"
"    border-radius: 5px;\n"
"	border-color: white;\n"
"}\n"
"\n"
"QPushButton#btn_add, #btn_save, #btn_gen_password, #btn_idk {\n"
"    padding: 3px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border-color: #090;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border: 4px solid #090;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	background-color: #006300;\n"
"	border-color: #090;\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.layout_main = QVBoxLayout()
        self.layout_main.setSpacing(0)
        self.layout_main.setObjectName(u"layout_main")
        self.btn_add = QPushButton(self.centralwidget)
        self.btn_add.setObjectName(u"btn_add")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_add.sizePolicy().hasHeightForWidth())
        self.btn_add.setSizePolicy(sizePolicy)

        self.layout_main.addWidget(self.btn_add)

        self.btn_passwords = QPushButton(self.centralwidget)
        self.btn_passwords.setObjectName(u"btn_passwords")
        sizePolicy.setHeightForWidth(self.btn_passwords.sizePolicy().hasHeightForWidth())
        self.btn_passwords.setSizePolicy(sizePolicy)

        self.layout_main.addWidget(self.btn_passwords)

        self.btn_gen_password = QPushButton(self.centralwidget)
        self.btn_gen_password.setObjectName(u"btn_gen_password")
        sizePolicy.setHeightForWidth(self.btn_gen_password.sizePolicy().hasHeightForWidth())
        self.btn_gen_password.setSizePolicy(sizePolicy)

        self.layout_main.addWidget(self.btn_gen_password)

        self.btn_calc = QPushButton(self.centralwidget)
        self.btn_calc.setObjectName(u"btn_calc")
        sizePolicy.setHeightForWidth(self.btn_calc.sizePolicy().hasHeightForWidth())
        self.btn_calc.setSizePolicy(sizePolicy)

        self.layout_main.addWidget(self.btn_calc)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.layout_main.addItem(self.verticalSpacer)


        self.horizontalLayout.addLayout(self.layout_main)

        self.layout_where = QVBoxLayout()
        self.layout_where.setObjectName(u"layout_where")
        self.tableWidget = QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName(u"tableWidget")

        self.layout_where.addWidget(self.tableWidget)


        self.horizontalLayout.addLayout(self.layout_where)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        MainWindow.setWindowFilePath("")
        self.btn_add.setText(QCoreApplication.translate("MainWindow", u"ADD", None))
        self.btn_passwords.setText(QCoreApplication.translate("MainWindow", u"PASSWORDS", None))
        self.btn_gen_password.setText(QCoreApplication.translate("MainWindow", u"Generate Password", None))
        self.btn_calc.setText(QCoreApplication.translate("MainWindow", u"CALCULATOR", None))
    # retranslateUi

