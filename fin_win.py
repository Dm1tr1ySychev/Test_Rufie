from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout,
    QGroupBox, QRadioButton, QPushButton,QLabel, QListWidget, QLineEdit)

from instruct import *


class FinalWin(QWidget):
    def __init__(self, exp):
        super().__init__()
        self.exp = exp
        self.set_apper()
        self.initUI()
        self.show()
    def set_apper(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self):
        self.heart = QLabel(txt_workheart + self.results())
        self.index = QLabel(txt_index + str(self.index))
        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.index, alignment=Qt.AlignCenter)
        self.layout_line.addWidget(self.heart, alignment=Qt.AlignCenter)
        self.setLayout(self.layout_line)
    def results(self):
        self.index = (4 * (int(self.exp.res1) + int(self.exp.res2) + int(self.exp.res3)) - 200) / 10
        if self.exp.age < 7:
            return 'нет данных для Вашего возраста'
        elif self.exp.age <= 8:
            if self.index >= 21:
                return txt_res1
            elif self.index >= 17:
                return txt_res2
            elif self.index >= 12:
                return txt_res3
            elif self.index >= 6.5:
                return txt_res4
            else:
                return txt_res5
        elif self.exp.age <= 10:
            if self.index >= 19.5:
                return txt_res1
            elif self.index >= 15.5:
                return txt_res2
            elif self.index >= 10.5:
                return txt_res3
            elif self.index >= 5:
                return txt_res4
            else:
                return txt_res5

        elif self.exp.age <= 12:
            if self.index >= 18:
                return txt_res1
            elif self.index >= 14:
                return txt_res2
            elif self.index >= 9:
                return txt_res3
            elif self.index >= 3.5:
                return txt_res4
            else:
                return txt_res5

        elif self.exp.age <= 14:
            if self.index >= 16.5:
                return txt_res1
            elif self.index >= 12.5:
                return txt_res2
            elif self.index >= 7.5:
                return txt_res3
            elif self.index >= 2:
                return txt_res4
            else:
                return txt_res5

        elif self.exp.age <= 1000:
            if self.index >= 15:
                return txt_res1
            elif self.index >= 11:
                return txt_res2
            elif self.index >= 6:
                return txt_res3
            elif self.index >= 0.5:
                return txt_res4
            else:
                return txt_res5

