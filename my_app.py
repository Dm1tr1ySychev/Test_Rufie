from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout,
    QGroupBox, QRadioButton, QPushButton,QLabel, QListWidget, QLineEdit)

from instruct import *
from set_win import *

class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_apper()
        self.initUI()
        self.connects()
        self.show()
    def set_apper(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self):
        self.hello_text = QLabel(txt_hello)
        self.instruction = QLabel(txt_instruction)
        self.butt_next = QPushButton(txt_next, self)

        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.hello_text, alignment=Qt.AlignLeft)
        self.layout_line.addWidget(self.instruction, alignment=Qt.AlignLeft)
        self.layout_line.addWidget(self.butt_next, alignment=Qt.AlignCenter)
        self.setLayout(self.layout_line)
    def next_click(self):
        self.testv = TestWin()
        self.hide()
        #print('почему ты не работаешь...')
    def connects(self):
        self.butt_next.clicked.connect(self.next_click)

app = QApplication([])
main_w = MainWin()
app.exec_()
