# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'setinfo.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(602, 229)
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
"}\n"
"\n"
"QPushButton#btn_lower, #btn_upper, #btn_digits, #btn_special {\n"
"    padding: 10px;\n"
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
"\n"
"QFrame {\n"
"    border: 2px solid gray;\n"
"    border-radius: 5px;\n"
"    margin-right: 0;\n"
"}\n"
"\n"
"QFrame:hover {\n"
"    border-color: #090;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    background-color: #111;           /* \u0442\u0451\u043c\u043d\u044b\u0439 \u0444\u043e\u043d */\n"
"    color: #fff;                      /* \u0442\u0435\u043a\u0441\u0442 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b"
                        "\u044f */\n"
"    border: 2px solid #444;           /* \u043e\u0431\u044b\u0447\u043d\u0430\u044f \u0440\u0430\u043c\u043a\u0430 */\n"
"    border-radius: 8px;\n"
"    padding: 6px 10px;\n"
"    font-size: 14px;\n"
"    selection-background-color: #555; /* \u0432\u044b\u0434\u0435\u043b\u0435\u043d\u0438\u0435 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #1E90FF;       /* \u0440\u0430\u043c\u043a\u0430 \u043f\u0440\u0438 \u0444\u043e\u043a\u0443\u0441\u0435 */\n"
"}\n"
"\n"
"QLineEdit::placeholder {\n"
"    color: #888;                      /* \u0441\u0432\u0435\u0442\u043b\u043e-\u0441\u0435\u0440\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 \u043f\u043b\u0435\u0439\u0441\u0445\u043e\u043b\u0434\u0435\u0440\u0430 */\n"
"    font-style: italic;\n"
"}\n"
"QLineEdit {\n"
"    background-color: #111;           /* \u0442\u0451\u043c\u043d\u044b\u0439 \u0444\u043e\u043d */\n"
"    color: #fff;                      /* \u0442\u0435\u043a\u0441\u0442 \u043f\u043e\u043b"
                        "\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f */\n"
"    border: 2px solid #444;           /* \u043e\u0431\u044b\u0447\u043d\u0430\u044f \u0440\u0430\u043c\u043a\u0430 */\n"
"    border-radius: 8px;\n"
"    padding: 6px 10px;\n"
"    font-size: 14px;\n"
"    selection-background-color: #555; /* \u0432\u044b\u0434\u0435\u043b\u0435\u043d\u0438\u0435 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #1E90FF;       /* \u0440\u0430\u043c\u043a\u0430 \u043f\u0440\u0438 \u0444\u043e\u043a\u0443\u0441\u0435 */\n"
"}\n"
"\n"
"QLineEdit::placeholder {\n"
"    color: #888;                      /* \u0441\u0432\u0435\u0442\u043b\u043e-\u0441\u0435\u0440\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 \u043f\u043b\u0435\u0439\u0441\u0445\u043e\u043b\u0434\u0435\u0440\u0430 */\n"
"    font-style: italic;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.layout_input = QHBoxLayout()
        self.layout_input.setObjectName(u"layout_input")
        self.input_site = QLineEdit(self.centralwidget)
        self.input_site.setObjectName(u"input_site")
        self.input_site.setMaxLength(75)

        self.layout_input.addWidget(self.input_site)

        self.input_login = QLineEdit(self.centralwidget)
        self.input_login.setObjectName(u"input_login")
        self.input_login.setMaxLength(25)

        self.layout_input.addWidget(self.input_login)

        self.input_password = QLineEdit(self.centralwidget)
        self.input_password.setObjectName(u"input_password")
        self.input_password.setMaxLength(100)

        self.layout_input.addWidget(self.input_password)


        self.verticalLayout.addLayout(self.layout_input)

        self.layout_main = QHBoxLayout()
        self.layout_main.setObjectName(u"layout_main")
        self.btn_save = QPushButton(self.centralwidget)
        self.btn_save.setObjectName(u"btn_save")

        self.layout_main.addWidget(self.btn_save)

        self.btn_back = QPushButton(self.centralwidget)
        self.btn_back.setObjectName(u"btn_back")

        self.layout_main.addWidget(self.btn_back)


        self.verticalLayout.addLayout(self.layout_main)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.input_site.setPlaceholderText(QCoreApplication.translate("MainWindow", u"key", None))
        self.input_login.setPlaceholderText(QCoreApplication.translate("MainWindow", u"login", None))
        self.input_password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"password", None))
        self.btn_save.setText(QCoreApplication.translate("MainWindow", u"SAVE", None))
        self.btn_back.setText(QCoreApplication.translate("MainWindow", u"BACK", None))
    # retranslateUi

