import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('converter.ui', self)
        self.value = 'Длина'
        self.converter = [1000, 1, 0.1, 0.01, 0.001]
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
        self.converter = [1000, 1, 0.1, 0.01, 0.001]
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
        self.converter = [1000000, 1, 0.01, 0.0001, 0.000001]
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
        self.converter = [1000000000, 1, 0.001, 0.000001, 0.000000001]
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
        self.converter = [31536000, 604800, 86400, 3600, 60, 1, 0.001]
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
        self.converter = [1000, 100, 1, 0.001, 0.000001]
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
                    self.textBrowser_output.setText(str(c + 273.15))
                elif a_text == 'K' and b_text == '°C':
                    self.textBrowser_output.setText(str(c - 273.15))
                elif a_text == '°C' and b_text == '°F':
                    self.textBrowser_output.setText(str((c + 32) * 1.8))
                elif a_text == '°F' and b_text == '°C':
                    self.textBrowser_output.setText(str((c - 32) / 1.8))
                elif a_text == 'K' and b_text == '°F':
                    self.textBrowser_output.setText(str((c - 273.15) * 1.8 + 32))
                elif a_text == '°F' and b_text == 'K':
                    self.textBrowser_output.setText(str((c - 32) / 1.8 + 273.15))
            except ValueError:
                self.textBrowser_output.setText('Неверный формат ввода!')

app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
