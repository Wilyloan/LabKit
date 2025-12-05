# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calc.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(498, 517)
        MainWindow.setStyleSheet(u"/* \u041e\u0431\u0449\u0438\u0435 \u0441\u0442\u0438\u043b\u0438 \u0434\u043b\u044f \u043e\u043a\u043d\u0430 \u043a\u0430\u043b\u044c\u043a\u0443\u043b\u044f\u0442\u043e\u0440\u0430 */\n"
"QWidget {\n"
"    background-color: #f0f0f0;\n"
"    font-family: Arial, sans-serif;\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"/* \u0421\u0442\u0438\u043b\u0438 \u0434\u043b\u044f \u0434\u0438\u0441\u043f\u043b\u0435\u044f (QLabel) */\n"
"QLabel {\n"
"    background-color: #ffffff;\n"
"    border: 2px solid #cccccc;\n"
"    border-radius: 5px;\n"
"    padding: 10px;\n"
"    color: #333333;\n"
"    font-size: 24px;\n"
"    qproperty-alignment: 'AlignRight | AlignVCenter';\n"
"}\n"
"\n"
"/* \u0421\u0442\u0438\u043b\u0438 \u0434\u043b\u044f \u043a\u043d\u043e\u043f\u043e\u043a \u043a\u0430\u043b\u044c\u043a\u0443\u043b\u044f\u0442\u043e\u0440\u0430 */\n"
"QPushButton {\n"
"    background-color: #e0e0e0;\n"
"    border: 2px solid #bfbfbf;\n"
"    border-radius: 5px;\n"
"    padding: 15px;\n"
"    color: #000000;\n"
"    font-size:"
                        " 18px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #d0d0d0;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #c0c0c0;\n"
"}\n"
"\n"
"/* \u041e\u0442\u0434\u0435\u043b\u044c\u043d\u044b\u0435 \u0441\u0442\u0438\u043b\u0438 \u0434\u043b\u044f \u043e\u043f\u0435\u0440\u0430\u0446\u0438\u0439 (+, -, *, /) */\n"
"QPushButton.operator {\n"
"    background-color: #ffb74d;\n"
"    color: #ffffff;\n"
"}\n"
"\n"
"QPushButton.operator:hover {\n"
"    background-color: #ffa726;\n"
"}\n"
"\n"
"QPushButton.operator:pressed {\n"
"    background-color: #ff9800;\n"
"}\n"
"\n"
"/* \u0421\u0442\u0438\u043b\u0438 \u0434\u043b\u044f \u043a\u043d\u043e\u043f\u043a\u0438 \"\u0440\u0430\u0432\u043d\u043e\" */\n"
"QPushButton.equals {\n"
"    background-color: #4caf50;\n"
"    color: #ffffff;\n"
"}\n"
"\n"
"QPushButton.equals:hover {\n"
"    background-color: #43a047;\n"
"}\n"
"\n"
"QPushButton.equals:pressed {\n"
"    background-color: #388e3c;\n"
"}\n"
"\n"
"/* \u0421\u0442\u0438\u043b\u0438 \u0434\u043b"
                        "\u044f \u043a\u043d\u043e\u043f\u043a\u0438 \"C\" (\u043e\u0447\u0438\u0441\u0442\u043a\u0430) */\n"
"QPushButton.clear {\n"
"    background-color: #f44336;\n"
"    color: #ffffff;\n"
"}\n"
"\n"
"QPushButton.clear:hover {\n"
"    background-color: #e53935;\n"
"}\n"
"\n"
"QPushButton.clear:pressed {\n"
"    background-color: #d32f2f;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.layout_special1 = QHBoxLayout()
        self.layout_special1.setObjectName(u"layout_special1")

        self.verticalLayout.addLayout(self.layout_special1)

        self.layout_output = QHBoxLayout()
        self.layout_output.setObjectName(u"layout_output")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.layout_output.addWidget(self.label)


        self.verticalLayout.addLayout(self.layout_output)

        self.layout_5 = QHBoxLayout()
        self.layout_5.setObjectName(u"layout_5")
        self.btn_del = QPushButton(self.centralwidget)
        self.btn_del.setObjectName(u"btn_del")

        self.layout_5.addWidget(self.btn_del)

        self.btn_clear = QPushButton(self.centralwidget)
        self.btn_clear.setObjectName(u"btn_clear")

        self.layout_5.addWidget(self.btn_clear)

        self.btn_percent = QPushButton(self.centralwidget)
        self.btn_percent.setObjectName(u"btn_percent")

        self.layout_5.addWidget(self.btn_percent)

        self.btn_division = QPushButton(self.centralwidget)
        self.btn_division.setObjectName(u"btn_division")

        self.layout_5.addWidget(self.btn_division)


        self.verticalLayout.addLayout(self.layout_5)

        self.layout_4 = QHBoxLayout()
        self.layout_4.setObjectName(u"layout_4")
        self.btn_7 = QPushButton(self.centralwidget)
        self.btn_7.setObjectName(u"btn_7")

        self.layout_4.addWidget(self.btn_7)

        self.btn_8 = QPushButton(self.centralwidget)
        self.btn_8.setObjectName(u"btn_8")

        self.layout_4.addWidget(self.btn_8)

        self.btn_9 = QPushButton(self.centralwidget)
        self.btn_9.setObjectName(u"btn_9")

        self.layout_4.addWidget(self.btn_9)

        self.btn_multiplication = QPushButton(self.centralwidget)
        self.btn_multiplication.setObjectName(u"btn_multiplication")

        self.layout_4.addWidget(self.btn_multiplication)


        self.verticalLayout.addLayout(self.layout_4)

        self.layout_3 = QHBoxLayout()
        self.layout_3.setObjectName(u"layout_3")
        self.btn_4 = QPushButton(self.centralwidget)
        self.btn_4.setObjectName(u"btn_4")

        self.layout_3.addWidget(self.btn_4)

        self.btn_5 = QPushButton(self.centralwidget)
        self.btn_5.setObjectName(u"btn_5")

        self.layout_3.addWidget(self.btn_5)

        self.btn_6 = QPushButton(self.centralwidget)
        self.btn_6.setObjectName(u"btn_6")

        self.layout_3.addWidget(self.btn_6)

        self.btn_minus = QPushButton(self.centralwidget)
        self.btn_minus.setObjectName(u"btn_minus")

        self.layout_3.addWidget(self.btn_minus)


        self.verticalLayout.addLayout(self.layout_3)

        self.layout_2 = QHBoxLayout()
        self.layout_2.setObjectName(u"layout_2")
        self.btn_1 = QPushButton(self.centralwidget)
        self.btn_1.setObjectName(u"btn_1")

        self.layout_2.addWidget(self.btn_1)

        self.btn_2 = QPushButton(self.centralwidget)
        self.btn_2.setObjectName(u"btn_2")

        self.layout_2.addWidget(self.btn_2)

        self.btn_3 = QPushButton(self.centralwidget)
        self.btn_3.setObjectName(u"btn_3")

        self.layout_2.addWidget(self.btn_3)

        self.btn_plus = QPushButton(self.centralwidget)
        self.btn_plus.setObjectName(u"btn_plus")

        self.layout_2.addWidget(self.btn_plus)


        self.verticalLayout.addLayout(self.layout_2)

        self.layout_1 = QHBoxLayout()
        self.layout_1.setObjectName(u"layout_1")
        self.btn_number_sign = QPushButton(self.centralwidget)
        self.btn_number_sign.setObjectName(u"btn_number_sign")

        self.layout_1.addWidget(self.btn_number_sign)

        self.btn_0 = QPushButton(self.centralwidget)
        self.btn_0.setObjectName(u"btn_0")

        self.layout_1.addWidget(self.btn_0)

        self.btn_comma = QPushButton(self.centralwidget)
        self.btn_comma.setObjectName(u"btn_comma")

        self.layout_1.addWidget(self.btn_comma)

        self.btn_reslut = QPushButton(self.centralwidget)
        self.btn_reslut.setObjectName(u"btn_reslut")

        self.layout_1.addWidget(self.btn_reslut)


        self.verticalLayout.addLayout(self.layout_1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"output", None))
        self.btn_del.setText(QCoreApplication.translate("MainWindow", u"<-", None))
        self.btn_clear.setText(QCoreApplication.translate("MainWindow", u"AC", None))
        self.btn_percent.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.btn_division.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.btn_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.btn_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.btn_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.btn_multiplication.setText(QCoreApplication.translate("MainWindow", u"*", None))
        self.btn_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.btn_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.btn_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.btn_minus.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.btn_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.btn_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.btn_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.btn_plus.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.btn_number_sign.setText(QCoreApplication.translate("MainWindow", u"+/-", None))
        self.btn_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_comma.setText(QCoreApplication.translate("MainWindow", u",", None))
        self.btn_reslut.setText(QCoreApplication.translate("MainWindow", u"=", None))
    # retranslateUi

