# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'deleteinfo.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHBoxLayout, QHeaderView,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(768, 350)
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
"\n"
"QTableWidget {\n"
"    background-color: #1e1e1e;\n"
"    color: #f0f0f0;\n"
"    gridline-color: #3a3a3a;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #2c2c2c;\n"
"    color: #f0f0f0;\n"
"    font-weight: bold;\n"
"    padding: 4px;\n"
"    border: 1px solid #3a3a3a;\n"
"}\n"
"\n"
"QTableWidget::item:selected {\n"
"    background-color: #3a76f0;\n"
" "
                        "   color: white;\n"
"}\n"
"\n"
"QTableWidget {\n"
"    alternate-background-color: #2a2a2a;\n"
"}\n"
"QTableCornerButton::section {\n"
"    background-color: #2c2c2c;   /* \u0444\u043e\u043d \u043a\u043d\u043e\u043f\u043a\u0438 */\n"
"    border: 1px solid #3a3a3a;   /* \u0440\u0430\u043c\u043a\u0430 */\n"
"}\n"
"\n"
"QTableCornerButton::section:hover {\n"
"    background-color: #3a76f0;   /* \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"}\n"
"\n"
"QTableCornerButton::section:pressed {\n"
"    background-color: #2a5bc0;   /* \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"}\n"
"\n"
"\n"
"QLineEdit {\n"
"    background-color: #111;           /* \u0442\u0451\u043c\u043d\u044b\u0439 \u0444\u043e\u043d */\n"
"    color: #fff;                      /* \u0442\u0435\u043a\u0441\u0442 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f */\n"
"    border: 2px solid #444;           /* \u043e\u0431\u044b\u0447\u043d\u0430\u044f \u0440\u0430\u043c"
                        "\u043a\u0430 */\n"
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
"    color: #fff;                      /* \u0442\u0435\u043a\u0441\u0442 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f */\n"
"    border: 2px solid #444;           /* \u043e\u0431"
                        "\u044b\u0447\u043d\u0430\u044f \u0440\u0430\u043c\u043a\u0430 */\n"
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
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.input_site = QLineEdit(self.centralwidget)
        self.input_site.setObjectName(u"input_site")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_site.sizePolicy().hasHeightForWidth())
        self.input_site.setSizePolicy(sizePolicy)

        self.verticalLayout_4.addWidget(self.input_site)

        self.input_login = QLineEdit(self.centralwidget)
        self.input_login.setObjectName(u"input_login")
        sizePolicy.setHeightForWidth(self.input_login.sizePolicy().hasHeightForWidth())
        self.input_login.setSizePolicy(sizePolicy)

        self.verticalLayout_4.addWidget(self.input_login)

        self.input_password = QLineEdit(self.centralwidget)
        self.input_password.setObjectName(u"input_password")
        sizePolicy.setHeightForWidth(self.input_password.sizePolicy().hasHeightForWidth())
        self.input_password.setSizePolicy(sizePolicy)

        self.verticalLayout_4.addWidget(self.input_password)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.btn_add = QPushButton(self.centralwidget)
        self.btn_add.setObjectName(u"btn_add")

        self.verticalLayout_4.addWidget(self.btn_add)

        self.btn_delete = QPushButton(self.centralwidget)
        self.btn_delete.setObjectName(u"btn_delete")

        self.verticalLayout_4.addWidget(self.btn_delete)

        self.btn_back = QPushButton(self.centralwidget)
        self.btn_back.setObjectName(u"btn_back")

        self.verticalLayout_4.addWidget(self.btn_back)


        self.horizontalLayout.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setSelectionMode(QAbstractItemView.SelectionMode.ContiguousSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_5.addWidget(self.tableWidget)


        self.horizontalLayout.addLayout(self.verticalLayout_5)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.input_site.setPlaceholderText(QCoreApplication.translate("MainWindow", u"service", None))
        self.input_login.setPlaceholderText(QCoreApplication.translate("MainWindow", u"login", None))
        self.input_password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"password", None))
        self.btn_add.setText(QCoreApplication.translate("MainWindow", u"ADD", None))
        self.btn_delete.setText(QCoreApplication.translate("MainWindow", u"DELETE", None))
        self.btn_back.setText(QCoreApplication.translate("MainWindow", u"BACK", None))
    # retranslateUi

