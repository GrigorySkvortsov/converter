import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('converter.ui', self)
        self.value = 'Длина'
        self.converter = [1000, 1, 0.1,
                          0.01, 0.001]
        self.comboBox_input.addItem('km')
        self.comboBox_input.addItem('m')
        self.comboBox_input.addItem('dm')
        self.comboBox_input.addItem('cm')
        self.comboBox_input.addItem('mm')

        self.comboBox_output.addItem('km')
        self.comboBox_output.addItem('m')
        self.comboBox_output.addItem('dm')
        self.comboBox_output.addItem('cm')
        self.comboBox_output.addItem('mm')
        self.pushButton_value.clicked.connect(self.bvalue)
        self.pushButton_result.clicked.connect(self.bresult)

    def bvalue(self):
        if self.value == self.comboBox_value.currentText():
            pass
        else:
            self.value = self.comboBox_value.currentText()
            if self.value == 'Длина':
                self.length()
            elif self.value == 'Площадь':
                self.area()
            elif self.value == 'Объём':
                self.volume()
            elif self.value == 'Температура':
                self.temperature()
            elif self.value == 'Время':
                self.time()
            elif self.value == 'Масса':
                self.mass()

    def length(self):
        self.comboBox_input.clear()
        self.comboBox_output.clear()
        self.converter = [1000, 1, 0.1,
                          0.01, 0.001]
        self.comboBox_input.addItem('km')
        self.comboBox_input.addItem('m')
        self.comboBox_input.addItem('dm')
        self.comboBox_input.addItem('cm')
        self.comboBox_input.addItem('mm')

        self.comboBox_output.addItem('km')
        self.comboBox_output.addItem('m')
        self.comboBox_output.addItem('dm')
        self.comboBox_output.addItem('cm')
        self.comboBox_output.addItem('mm')

    def area(self):
        self.comboBox_input.clear()
        self.comboBox_output.clear()
        self.converter = [1000000, 1, 0.01,
                          0.0001, 0.000001]
        self.comboBox_input.addItem('km²')
        self.comboBox_input.addItem('m²')
        self.comboBox_input.addItem('dm²')
        self.comboBox_input.addItem('cm²')
        self.comboBox_input.addItem('mm²')

        self.comboBox_output.addItem('km²')
        self.comboBox_output.addItem('m²')
        self.comboBox_output.addItem('dm²')
        self.comboBox_output.addItem('cm²')
        self.comboBox_output.addItem('mm²')

    def volume(self):
        self.comboBox_input.clear()
        self.comboBox_output.clear()
        self.comboBox_output.clear()
        self.converter = [1000000000, 1, 0.001,
                          0.000001, 0.000000001]
        self.comboBox_input.addItem('km³')
        self.comboBox_input.addItem('m³')
        self.comboBox_input.addItem('dm³')
        self.comboBox_input.addItem('cm³')
        self.comboBox_input.addItem('mm³')

        self.comboBox_output.addItem('km³')
        self.comboBox_output.addItem('m³')
        self.comboBox_output.addItem('dm³')
        self.comboBox_output.addItem('cm³')
        self.comboBox_output.addItem('mm³')

    def temperature(self):
        self.comboBox_input.clear()
        self.comboBox_output.clear()
        self.converter = []
        self.comboBox_input.addItem('°C')
        self.comboBox_input.addItem('°F')
        self.comboBox_input.addItem('K')
        self.comboBox_output.addItem('°C')
        self.comboBox_output.addItem('°F')
        self.comboBox_output.addItem('K')

    def time(self):
        self.comboBox_input.clear()
        self.comboBox_output.clear()
        self.converter = [31536000, 604800, 86400,
                          3600, 60, 1, 0.001]
        self.comboBox_input.addItem('y')
        self.comboBox_input.addItem('wk')
        self.comboBox_input.addItem('d')
        self.comboBox_input.addItem('h')
        self.comboBox_input.addItem('min')
        self.comboBox_input.addItem('s')
        self.comboBox_input.addItem('ms')

        self.comboBox_output.addItem('y')
        self.comboBox_output.addItem('wk')
        self.comboBox_output.addItem('d')
        self.comboBox_output.addItem('h')
        self.comboBox_output.addItem('min')
        self.comboBox_output.addItem('s')
        self.comboBox_output.addItem('ms')

    def mass(self):
        self.comboBox_input.clear()
        self.comboBox_output.clear()
        self.converter = [1000, 100, 1,
                          0.001, 0.000001]
        self.comboBox_input.addItem('t')
        self.comboBox_input.addItem('q')
        self.comboBox_input.addItem('kg')
        self.comboBox_input.addItem('g')
        self.comboBox_input.addItem('mg')

        self.comboBox_output.addItem('t')
        self.comboBox_output.addItem('q')
        self.comboBox_output.addItem('kg')
        self.comboBox_output.addItem('g')
        self.comboBox_output.addItem('mg')

    def bresult(self):
        if self.lineEdit_input.text() == '':
            self.textBrowser_output.setText('')
        elif self.comboBox_value.currentText() != 'Температура':
            a = self.converter[self.comboBox_input.currentIndex()]
            b = self.converter[self.comboBox_output.currentIndex()]
            try:
                c = a / b * float(self.lineEdit_input.text())
                self.textBrowser_output.setText(str(c))

            except ValueError:
                self.textBrowser_output.setText('Неверный формат ввода!')

        elif self.comboBox_value.currentText() == 'Температура':
            a_text = self.comboBox_input.currentText()
            b_text = self.comboBox_output.currentText()
            try:
                c = float(self.lineEdit_input.text())
                if a_text == b_text:
                    self.textBrowser_output.setText(str(c))
                elif a_text == '°C' and b_text == 'K':
                    a = str(c + 273.15)
                    self.textBrowser_output.setText(a)
                elif a_text == 'K' and b_text == '°C':
                    a = str(c - 273.15)
                    self.textBrowser_output.setText(a)
                elif a_text == '°C' and b_text == '°F':
                    a = str((c + 32) * 1.8)
                    self.textBrowser_output.setText(a)
                elif a_text == '°F' and b_text == '°C':
                    a = str((c - 32) / 1.8)
                    self.textBrowser_output.setText(a)
                elif a_text == 'K' and b_text == '°F':
                    a = str((c - 273.15) * 1.8 + 32)
                    self.textBrowser_output.setText(a)
                elif a_text == '°F' and b_text == 'K':
                    a = str((c - 32) / 1.8 + 273.15)
                    self.textBrowser_output.setText()
            except ValueError:
                self.textBrowser_output.setText('Неверный формат ввода!')

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(410, 208)
        font = QtGui.QFont()
        font.setPointSize(8)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 408, 181))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setVerticalSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_input = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_input.setMaximumSize(QtCore.QSize(16777215, 23))
        self.lineEdit_input.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.lineEdit_input.setObjectName("lineEdit_input")
        self.gridLayout.addWidget(self.lineEdit_input, 2, 1, 1, 1)
        self.comboBox_output = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox_output.setMaximumSize(QtCore.QSize(16777215, 23))
        self.comboBox_output.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.comboBox_output.setObjectName("comboBox_output")
        self.gridLayout.addWidget(self.comboBox_output, 3, 0, 1, 1)
        self.label_title = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setObjectName("label_title")
        self.gridLayout.addWidget(self.label_title, 0, 0, 1, 2)
        self.comboBox_value = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox_value.setMaximumSize(QtCore.QSize(16777215, 23))
        self.comboBox_value.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.comboBox_value.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.comboBox_value.setObjectName("comboBox_value")
        self.comboBox_value.addItem("")
        self.comboBox_value.addItem("")
        self.comboBox_value.addItem("")
        self.comboBox_value.addItem("")
        self.comboBox_value.addItem("")
        self.comboBox_value.addItem("")
        self.gridLayout.addWidget(self.comboBox_value, 1, 0, 1, 1)
        self.pushButton_value = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_value.setMaximumSize(QtCore.QSize(16777215, 23))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_value.setFont(font)
        self.pushButton_value.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_value.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.pushButton_value.setObjectName("pushButton_value")
        self.gridLayout.addWidget(self.pushButton_value, 1, 1, 1, 1)
        self.comboBox_input = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox_input.setMaximumSize(QtCore.QSize(16777215, 23))
        self.comboBox_input.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.comboBox_input.setObjectName("comboBox_input")
        self.gridLayout.addWidget(self.comboBox_input, 2, 0, 1, 1)
        self.textBrowser_output = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        self.textBrowser_output.setMaximumSize(QtCore.QSize(16777215, 23))
        self.textBrowser_output.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.textBrowser_output.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.textBrowser_output.setObjectName("textBrowser_output")
        self.gridLayout.addWidget(self.textBrowser_output, 3, 1, 1, 1)
        self.pushButton_result = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_result.setMaximumSize(QtCore.QSize(16777215, 23))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_result.setFont(font)
        self.pushButton_result.setStyleSheet("background-color: rgb(170, 255, 127);")
        self.pushButton_result.setObjectName("pushButton_result")
        self.gridLayout.addWidget(self.pushButton_result, 4, 0, 1, 2)
        self.gridLayout.setColumnMinimumWidth(0, 160)
        self.gridLayout.setColumnMinimumWidth(1, 200)
        self.gridLayout.setRowMinimumHeight(0, 30)
        self.gridLayout.setRowMinimumHeight(1, 30)
        self.gridLayout.setRowMinimumHeight(2, 30)
        self.gridLayout.setRowMinimumHeight(3, 30)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 410, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Конвертер"))
        self.label_title.setText(_translate("MainWindow", "Конвертер единиц измерения"))
        self.comboBox_value.setItemText(0, _translate("MainWindow", "Длина"))
        self.comboBox_value.setItemText(1, _translate("MainWindow", "Площадь"))
        self.comboBox_value.setItemText(2, _translate("MainWindow", "Объём"))
        self.comboBox_value.setItemText(3, _translate("MainWindow", "Температура"))
        self.comboBox_value.setItemText(4, _translate("MainWindow", "Время"))
        self.comboBox_value.setItemText(5, _translate("MainWindow", "Масса"))
        self.pushButton_value.setText(_translate("MainWindow", "Применить"))
        self.pushButton_result.setText(_translate("MainWindow", "Рассчитать"))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
