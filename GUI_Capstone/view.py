# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'view.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(368, 302)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setAcceptDrops(False)
        self.centralwidget.setStyleSheet(u"QMainWindow {\n"
"    background-color: #dfe7ee;\n"
"}\n"
"\n"
"QWidget {\n"
"    background-color: #dfe7ee;\n"
"    color: #2f3b46;\n"
"    font-family: \"Segoe UI\";\n"
"    font-size: 10pt;\n"
"}\n"
"\n"
"QFrame#converterFrame {\n"
"    background-color: #eef4f8;\n"
"    border: 1px solid #b7c7d6;\n"
"    border-radius: 14px;\n"
"}\n"
"\n"
"QLabel#titleLabel {\n"
"    color: #2e4a5f;\n"
"    font-size: 16pt;\n"
"    font-weight: bold;\n"
"    border: none;\n"
"    background: transparent;\n"
"}\n"
"\n"
"QLabel#descriptionLabel {\n"
"    color: #5f7282;\n"
"    font-size: 9pt;\n"
"    border: none;\n"
"    background: transparent;\n"
"}\n"
"\n"
"QLabel#inputLabel {\n"
"    color: #3a4b57;\n"
"    font-weight: 500;\n"
"    border: none;\n"
"    background: transparent;\n"
"}\n"
"\n"
"QLabel#resultLabel {\n"
"    color: #4f8a78;\n"
"    font-weight: bold;\n"
"    border: none;\n"
"    background: transparent;\n"
"}\n"
"\n"
"QLineEdit#fahrenheitInput {\n"
"    background-color: #f8fbfd;\n"
"    color: #2f3b46;\n"
""
                        "    border: 1px solid #b7c7d6;\n"
"    border-radius: 8px;\n"
"    padding: 7px;\n"
"}\n"
"\n"
"QLineEdit#fahrenheitInput:focus {\n"
"    border: 1px solid #6d97b8;\n"
"}\n"
"\n"
"QPushButton#convertButton {\n"
"    background-color: #6d97b8;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    padding: 8px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton#convertButton:hover {\n"
"    background-color: #7da5c4;\n"
"}\n"
"\n"
"QPushButton#convertButton:pressed {\n"
"    background-color: #5d88a9;\n"
"}")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.converterFrame = QFrame(self.centralwidget)
        self.converterFrame.setObjectName(u"converterFrame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.converterFrame.sizePolicy().hasHeightForWidth())
        self.converterFrame.setSizePolicy(sizePolicy)
        self.converterFrame.setMinimumSize(QSize(350, 230))
        self.converterFrame.setMaximumSize(QSize(400, 260))
        self.converterFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.converterFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.converterFrame)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(24, 20, 24, 20)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.titleLabel = QLabel(self.converterFrame)
        self.titleLabel.setObjectName(u"titleLabel")

        self.verticalLayout_2.addWidget(self.titleLabel, 0, Qt.AlignmentFlag.AlignHCenter)

        self.inputLabel = QLabel(self.converterFrame)
        self.inputLabel.setObjectName(u"inputLabel")

        self.verticalLayout_2.addWidget(self.inputLabel, 0, Qt.AlignmentFlag.AlignHCenter)

        self.fahrenheitInput = QLineEdit(self.converterFrame)
        self.fahrenheitInput.setObjectName(u"fahrenheitInput")
        self.fahrenheitInput.setMinimumSize(QSize(200, 32))
        self.fahrenheitInput.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.fahrenheitInput, 0, Qt.AlignmentFlag.AlignHCenter)

        self.resultLabel = QLabel(self.converterFrame)
        self.resultLabel.setObjectName(u"resultLabel")

        self.verticalLayout_2.addWidget(self.resultLabel, 0, Qt.AlignmentFlag.AlignHCenter)

        self.convertButton = QPushButton(self.converterFrame)
        self.convertButton.setObjectName(u"convertButton")
        self.convertButton.setMinimumSize(QSize(200, 34))

        self.verticalLayout_2.addWidget(self.convertButton, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout.addLayout(self.verticalLayout_2)


        self.gridLayout.addWidget(self.converterFrame, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 368, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Temperature Converter", None))
        self.titleLabel.setText(QCoreApplication.translate("MainWindow", u"Temperature Converter", None))
        self.inputLabel.setText(QCoreApplication.translate("MainWindow", u"Enter Farenheit:", None))
        self.fahrenheitInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Example: 72", None))
        self.resultLabel.setText(QCoreApplication.translate("MainWindow", u"Result will appear here", None))
        self.convertButton.setText(QCoreApplication.translate("MainWindow", u"Convert to Celsius", None))
    # retranslateUi

