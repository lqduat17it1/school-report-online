# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainSearch.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(464, 356)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 20, 461, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 110, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 150, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(60, 190, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.SogiaoducCombobox = QtWidgets.QComboBox(self.centralwidget)
        self.SogiaoducCombobox.setGeometry(QtCore.QRect(190, 110, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.SogiaoducCombobox.setFont(font)
        self.SogiaoducCombobox.setObjectName("SogiaoducCombobox")
        self.MahocbaText = QtWidgets.QLineEdit(self.centralwidget)
        self.MahocbaText.setGeometry(QtCore.QRect(190, 150, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.MahocbaText.setFont(font)
        self.MahocbaText.setObjectName("MahocbaText")
        self.TenhocsinhText = QtWidgets.QLineEdit(self.centralwidget)
        self.TenhocsinhText.setGeometry(QtCore.QRect(190, 190, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.TenhocsinhText.setFont(font)
        self.TenhocsinhText.setObjectName("TenhocsinhText")
        self.TimButton = QtWidgets.QPushButton(self.centralwidget)
        self.TimButton.setGeometry(QtCore.QRect(180, 260, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.TimButton.setFont(font)
        self.TimButton.setAutoFillBackground(False)
        self.TimButton.setObjectName("TimButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 464, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tìm kiếm học bạ điện tử"))
        self.label.setText(_translate("MainWindow", "HỌC BẠ ĐIỆN TỬ"))
        self.label_2.setText(_translate("MainWindow", "Sở giáo dục: "))
        self.label_3.setText(_translate("MainWindow", "Mã học bạ: "))
        self.label_4.setText(_translate("MainWindow", "Tên học sinh: "))
        self.TimButton.setText(_translate("MainWindow", "Tìm"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
