# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Hp\Desktop\информатика\dz13v.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(567, 623)
        MainWindow.setMinimumSize(QtCore.QSize(450, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.text_widget = QtWidgets.QWidget(self.widget)
        self.text_widget.setObjectName("text_widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.text_widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.textEdit = QtWidgets.QTextEdit(self.text_widget)
        self.textEdit.setMinimumSize(QtCore.QSize(450, 0))
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_2.addWidget(self.textEdit)
        self.verticalLayout.addWidget(self.text_widget)
        self.btn_widget = QtWidgets.QWidget(self.widget)
        self.btn_widget.setMaximumSize(QtCore.QSize(16777215, 90))
        self.btn_widget.setObjectName("btn_widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.btn_widget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.SaveButton = QtWidgets.QPushButton(self.btn_widget)
        self.SaveButton.setMinimumSize(QtCore.QSize(120, 50))
        self.SaveButton.setMaximumSize(QtCore.QSize(120, 50))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(15)
        font.setItalic(True)
        self.SaveButton.setFont(font)
        self.SaveButton.setStyleSheet("QPushButton {\n"
"    border:none;\n"
"}\n"
"\n"
"QPushButton: hover {\n"
"    border-radius:6px;\n"
"    border: 7px;\n"
"    border-color: rgb(0, 0, 182);\n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.SaveButton.setObjectName("SaveButton")
        self.horizontalLayout_2.addWidget(self.SaveButton)
        self.ExitButton = QtWidgets.QPushButton(self.btn_widget)
        self.ExitButton.setMinimumSize(QtCore.QSize(120, 50))
        self.ExitButton.setMaximumSize(QtCore.QSize(120, 50))
        self.ExitButton.setObjectName("ExitButton")
        self.horizontalLayout_2.addWidget(self.ExitButton)
        self.verticalLayout.addWidget(self.btn_widget)
        self.horizontalLayout.addWidget(self.widget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.SaveButton.setText(_translate("MainWindow", "Save File"))
        self.ExitButton.setText(_translate("MainWindow", "Exit"))
