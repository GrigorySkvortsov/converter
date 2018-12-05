import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('converter.ui', self)
        self.value = 'Длина'
        self.pushButton_value.clicked.connect(self.bvalue)

    def bvalue(self):
        self.value = self.comboBox_value.currentText()
        if self.value == 'Длина':
            self.length()
        elif self.value == 'Площадь':
            self.area()
        elif self.value == 'Объём':
            self.volume()
        elif self.value == 'Темпратура':
            self.temperature()
        elif self.value == 'Время':
            self.time()
        elif self.value == 'Масса':
            self.mass()

    def length(self):
        pass

    def area(self):
        pass

    def volume(self):
        pass

    def temperature(self):
        pass

    def time(self):
        pass

    def mass(self):
        pass

app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
